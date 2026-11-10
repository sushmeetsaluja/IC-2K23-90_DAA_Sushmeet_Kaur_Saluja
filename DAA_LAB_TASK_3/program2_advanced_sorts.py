"""Merge, Quick (last-element pivot), Heap sorts. All return a new sorted list."""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# Quick sort — pivot strategy: LAST element (Lomuto partition)
def quick_sort(arr):
    a = arr[:]
    _quick(a, 0, len(a) - 1)
    return a


def _quick(a, lo, hi):
    if lo < hi:
        p = _partition(a, lo, hi)
        _quick(a, lo, p - 1)
        _quick(a, p + 1, hi)


def _partition(a, lo, hi):
    pivot = a[hi]
    i = lo - 1
    for j in range(lo, hi):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[hi] = a[hi], a[i + 1]
    return i + 1


def heap_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        _heapify(a, i, 0)
    return a


def _heapify(a, n, i):
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        _heapify(a, n, largest)


if __name__ == "__main__":
    sample = [8, 3, 5, 4, 7, 6, 1, 2]
    print(f"input: {sample}")
    print(f"merge_sort: {merge_sort(sample)}")
    print(f"quick_sort (last-element pivot): {quick_sort(sample)}")
    print(f"heap_sort:  {heap_sort(sample)}")
