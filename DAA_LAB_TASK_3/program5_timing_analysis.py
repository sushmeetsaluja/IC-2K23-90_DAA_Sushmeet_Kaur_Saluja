"""Timing analysis of all six sorting algorithms across input types and sizes."""

import random
import time
import csv
import sys

from program1_basic_sorts import bubble_sort, selection_sort, insertion_sort
from program2_advanced_sorts import merge_sort, quick_sort, heap_sort

sys.setrecursionlimit(10000)

ALGORITHMS = {
    "Bubble":    bubble_sort,
    "Selection": selection_sort,
    "Insertion": insertion_sort,
    "Merge":     merge_sort,
    "Quick":     quick_sort,
    "Heap":      heap_sort,
}

SIZES = [100, 500, 1000, 2000]
# Skip O(n^2) algorithms and quick sort (recursion blowup on sorted input) at high n
SKIP_AT = {
    "Bubble":    3000,
    "Selection": 3000,
    "Insertion": 3000,
}


def make_input(n, kind):
    if kind == "random":
        random.seed(42)
        return [random.randint(0, 10000) for _ in range(n)]
    if kind == "sorted":
        return list(range(n))
    if kind == "reversed":
        return list(range(n, 0, -1))
    raise ValueError(kind)


def time_sort(fn, data):
    start = time.perf_counter()
    fn(data)
    return time.perf_counter() - start


def run_analysis():
    results = []
    for n in SIZES:
        for kind in ("random", "sorted", "reversed"):
            data = make_input(n, kind)
            for name, fn in ALGORITHMS.items():
                if name in SKIP_AT and n >= SKIP_AT[name]:
                    results.append((name, kind, n, None))
                    continue
                # Quick sort hits recursion depth on sorted/reversed with last-pivot
                if name == "Quick" and kind in ("sorted", "reversed") and n >= 2000:
                    results.append((name, kind, n, None))
                    continue
                t = time_sort(fn, data)
                results.append((name, kind, n, t))
                print(f"{name:10s} {kind:9s} n={n:5d}  {t:.5f}s")
    return results


def save_csv(results, path="timing_results.csv"):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["algorithm", "input_type", "n", "time_seconds"])
        for row in results:
            name, kind, n, t = row
            w.writerow([name, kind, n, "" if t is None else f"{t:.6f}"])
    print(f"\nSaved {path}")


def print_table(results):
    print("\n" + "=" * 60)
    print(f"{'Algorithm':<12}{'Input':<12}{'n':>8}{'Time (s)':>14}")
    print("=" * 60)
    for name, kind, n, t in results:
        tstr = "skipped" if t is None else f"{t:.5f}"
        print(f"{name:<12}{kind:<12}{n:>8}{tstr:>14}")


if __name__ == "__main__":
    results = run_analysis()
    print_table(results)
    save_csv(results)
