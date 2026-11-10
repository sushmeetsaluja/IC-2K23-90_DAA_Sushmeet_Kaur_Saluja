"""Plot timing results from CSV into two graphs."""

import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def load_results(path="timing_results.csv"):
    data = defaultdict(lambda: defaultdict(dict))  # [input_type][algo][n] = t
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row["time_seconds"]:
                continue
            algo = row["algorithm"]
            kind = row["input_type"]
            n = int(row["n"])
            t = float(row["time_seconds"])
            data[kind][algo][n] = t
    return data


def plot_input_type(data, kind, title, outpath):
    plt.figure(figsize=(10, 6))
    for algo in ("Bubble", "Selection", "Insertion", "Merge", "Quick", "Heap"):
        if algo not in data[kind]:
            continue
        ns = sorted(data[kind][algo].keys())
        ts = [data[kind][algo][n] for n in ns]
        plt.plot(ns, ts, marker="o", label=algo)
    plt.xlabel("Input size (n)")
    plt.ylabel("Time (seconds)")
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.yscale("log")
    plt.tight_layout()
    plt.savefig(outpath, dpi=120)
    plt.close()
    print(f"Saved {outpath}")


if __name__ == "__main__":
    data = load_results()
    plot_input_type(data, "random", "Sorting algorithms — random input", "graph_random.png")
    plot_input_type(data, "sorted", "Sorting algorithms — already-sorted input", "graph_sorted.png")
