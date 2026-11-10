"""Iterative binary search. Returns index or -1."""


def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    sorted_arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
    print(f"array: {sorted_arr}")
    print(f"search 23 -> index {binary_search(sorted_arr, 23)}")
    print(f"search 50 -> index {binary_search(sorted_arr, 50)}")
