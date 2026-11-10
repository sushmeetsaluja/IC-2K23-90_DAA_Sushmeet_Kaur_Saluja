"""Student record manager with configurable sort + binary search."""

import time
from program1_basic_sorts import bubble_sort, selection_sort, insertion_sort
from program2_advanced_sorts import merge_sort, quick_sort, heap_sort
from program4_binary_search import binary_search

ALGORITHMS = {
    "1": ("Bubble",    bubble_sort),
    "2": ("Selection", selection_sort),
    "3": ("Insertion", insertion_sort),
    "4": ("Merge",     merge_sort),
    "5": ("Quick",     quick_sort),
    "6": ("Heap",      heap_sort),
}

SAMPLE = [
    {"roll": 23, "name": "Priya",   "marks": 78},
    {"roll": 7,  "name": "Arjun",   "marks": 92},
    {"roll": 41, "name": "Meera",   "marks": 65},
    {"roll": 12, "name": "Rahul",   "marks": 88},
    {"roll": 3,  "name": "Zoya",    "marks": 74},
    {"roll": 56, "name": "Kabir",   "marks": 81},
    {"roll": 19, "name": "Isha",    "marks": 69},
    {"roll": 34, "name": "Dev",     "marks": 95},
    {"roll": 28, "name": "Sana",    "marks": 72},
    {"roll": 50, "name": "Omar",    "marks": 60},
]


def sort_records(records, key, algo_fn):
    # Decorate -> sort by extracted key -> undecorate
    paired = [(r[key], i, r) for i, r in enumerate(records)]
    # Convert the sort to operate on the tuple's first element
    # Trick: wrap records in a list that comparisons use via keys
    keys = [p[0] for p in paired]
    sorted_keys = algo_fn(keys)
    # Rebuild by matching sorted keys with originals (stable w.r.t. original order)
    buckets = {}
    for k, _, r in paired:
        buckets.setdefault(k, []).append(r)
    out = []
    for k in sorted_keys:
        out.append(buckets[k].pop(0))
    return out


def search_by_roll(records_sorted_by_roll, target):
    rolls = [r["roll"] for r in records_sorted_by_roll]
    idx = binary_search(rolls, target)
    return records_sorted_by_roll[idx] if idx != -1 else None


def comparative_report(records, key):
    print(f"\nComparative timing — sorting by {key!r}:")
    timings = {}
    for _, (name, fn) in ALGORITHMS.items():
        start = time.perf_counter()
        for _ in range(200):          # loop so small-n timings are measurable
            sort_records(records, key, fn)
        timings[name] = time.perf_counter() - start

    fastest = min(timings, key=timings.get)
    slowest = max(timings, key=timings.get)
    for name, t in sorted(timings.items(), key=lambda x: x[1]):
        print(f"  {name:10s} {t*1000:.3f} ms")
    ratio = timings[slowest] / timings[fastest]
    print(f"\n  fastest: {fastest} ({timings[fastest]*1000:.3f} ms)")
    print(f"  slowest: {slowest} ({timings[slowest]*1000:.3f} ms)")
    print(f"  slowest / fastest ratio: {ratio:.2f}x")
    return timings


def print_records(records):
    print(f"  {'Roll':<6}{'Name':<12}{'Marks':<6}")
    for r in records:
        print(f"  {r['roll']:<6}{r['name']:<12}{r['marks']:<6}")


def menu():
    records = SAMPLE[:]
    while True:
        print("\n--- Student Record Manager ---")
        print("1. Show records")
        print("2. Sort records")
        print("3. Search by roll (binary search)")
        print("4. Run comparative sort report")
        print("5. Quit")
        choice = input("> ").strip()

        if choice == "1":
            print_records(records)
        elif choice == "2":
            print("Sort by: 1) roll  2) name  3) marks")
            k = {"1": "roll", "2": "name", "3": "marks"}.get(input("> ").strip())
            if not k:
                print("invalid"); continue
            print("Algorithm:")
            for key, (n, _) in ALGORITHMS.items():
                print(f"  {key}) {n}")
            a = ALGORITHMS.get(input("> ").strip())
            if not a:
                print("invalid"); continue
            records = sort_records(records, k, a[1])
            print(f"Sorted by {k} using {a[0]}:")
            print_records(records)
        elif choice == "3":
            by_roll = sort_records(records, "roll", merge_sort)
            try:
                target = int(input("Roll no: ").strip())
            except ValueError:
                print("invalid"); continue
            found = search_by_roll(by_roll, target)
            print("Found:" if found else "Not found")
            if found:
                print(f"  {found}")
        elif choice == "4":
            comparative_report(records, "roll")
        elif choice == "5":
            break
        else:
            print("invalid")


if __name__ == "__main__":
    import sys
    if "--demo" in sys.argv:
        print("Initial records:")
        print_records(SAMPLE)
        sorted_by_roll = sort_records(SAMPLE, "roll", merge_sort)
        print("\nSorted by roll (merge sort):")
        print_records(sorted_by_roll)
        print(f"\nBinary search for roll 28: {search_by_roll(sorted_by_roll, 28)}")
        print(f"Binary search for roll 99: {search_by_roll(sorted_by_roll, 99)}")
        comparative_report(SAMPLE, "roll")
    else:
        menu()
