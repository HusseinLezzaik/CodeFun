# O(N^2) time, O(1) space
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the index of the minimum element in the unsorted part.
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the minimum element with the first element of the unsorted part.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Test case 1
arr1 = [5, 2, 9, 1, 5, 6]
print(selection_sort(arr1))  # Output: [1, 2, 5, 5, 6, 9]

# Test case 2
arr2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(selection_sort(arr2))  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Test case 3 (Already sorted)
arr3 = [1, 2, 3, 4, 5]
print(selection_sort(arr3))  # Output: [1, 2, 3, 4, 5]

# Test case 4 (Reverse sorted)
arr4 = [5, 4, 3, 2, 1]
print(selection_sort(arr4))  # Output: [1, 2, 3, 4, 5]
