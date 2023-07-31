# O(n^2) time | O(1) space
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        # Store the current element to be inserted.
        current = arr[i]
        j = i - 1

        # Move elements of the sorted part that are greater than the current element to one position ahead.
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the current element into its correct position in the sorted part.
        arr[j + 1] = current

    return arr

# Test case 1
arr1 = [5, 2, 9, 1, 5, 6]
print(insertion_sort(arr1))  # Output: [1, 2, 5, 5, 6, 9]

# Test case 2
arr2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(insertion_sort(arr2))  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Test case 3 (Already sorted)
arr3 = [1, 2, 3, 4, 5]
print(insertion_sort(arr3))  # Output: [1, 2, 3, 4, 5]

# Test case 4 (Reverse sorted)
arr4 = [5, 4, 3, 2, 1]
print(insertion_sort(arr4))  # Output: [1, 2, 3, 4, 5]
