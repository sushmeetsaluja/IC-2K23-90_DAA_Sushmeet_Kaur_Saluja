# Given list
numbers = [8, 3, 15, 6, 2]

print("Given list:", numbers)

# -------------------------
# Find the largest number
# -------------------------

largest = numbers[0]
comparisons = 0

print("\nFinding the largest number:")

for i in range(1, len(numbers)):
    comparisons = comparisons + 1

    if numbers[i] > largest:
        largest = numbers[i]

    print("i =", i,
          "A[i] =", numbers[i],
          "max =", largest,
          "comparisons =", comparisons)

print("\nLargest number:", largest)
print("Comparisons made:", comparisons)


# -------------------------
# Sort using Selection Sort
# -------------------------

print("\nSorting using Selection Sort:")

sorted_numbers = numbers.copy()

for i in range(len(sorted_numbers) - 1):

    min_index = i

    for j in range(i + 1, len(sorted_numbers)):

        if sorted_numbers[j] < sorted_numbers[min_index]:
            min_index = j

    # Swap the numbers
    temp = sorted_numbers[i]
    sorted_numbers[i] = sorted_numbers[min_index]
    sorted_numbers[min_index] = temp

    print("Step", i + 1, ":", sorted_numbers)

print("\nSorted list:", sorted_numbers)