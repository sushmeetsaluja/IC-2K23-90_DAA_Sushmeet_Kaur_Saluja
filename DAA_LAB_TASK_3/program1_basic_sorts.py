"""Bubble, Selection, Insertion sorts. All in-place, returning the same list."""


def bubble_sort(arr, verbose=False):
    a = arr[:]
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if verbose:
            print(f"  pass {i + 1}: {a}")
        if not swapped:
            break
    return a


def selection_sort(arr, verbose=False):
    a = arr[:]
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        if verbose:
            print(f"  step {i + 1}: {a}")
    return a


def insertion_sort(arr, verbose=False):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        if verbose:
            print(f"  step {i}: {a}")
    return a


if __name__ == "__main__":
    sample = [5, 2, 8, 1, 9, 3, 7, 4, 6]

    print("Bubble sort:")
    print(f"  input: {sample}")
    print(f"  output: {bubble_sort(sample, verbose=True)}\n")

    print("Selection sort:")
    print(f"  input: {sample}")
    print(f"  output: {selection_sort(sample, verbose=True)}\n")

    print("Insertion sort:")
    print(f"  input: {sample}")
    print(f"  output: {insertion_sort(sample, verbose=True)}")
