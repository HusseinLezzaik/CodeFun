# O(NlogN) time, O(N) space
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Choose the pivot element (can be any element, here we choose the middle element).
    pivot_idx = len(arr) // 2
    pivot = arr[pivot_idx]

    # Partition the array into two subarrays.
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort each subarray and combine the results.
    return quick_sort(left) + middle + quick_sort(right)


# Test case 1
arr1 = [5, 2, 9, 1, 5, 6]
print(quick_sort(arr1))  # Output: [1, 2, 5, 5, 6, 9]

# Test case 2
arr2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(quick_sort(arr2))  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Test case 3 (Already sorted)
arr3 = [1, 2, 3, 4, 5]
print(quick_sort(arr3))  # Output: [1, 2, 3, 4, 5]

# Test case 4 (Reverse sorted)
arr4 = [5, 4, 3, 2, 1]
print(quick_sort(arr4))  # Output: [1, 2, 3, 4, 5]
