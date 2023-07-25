# O(N^2) time, O(1) space
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swaps are made in this pass.
        swapped = False
        
        # Last i elements are already in place, so we don't need to compare them.
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements if they are in the wrong order.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps are made in this pass, the list is already sorted.
        if not swapped:
            break

    return arr

# Test case 1
arr1 = [5, 2, 9, 1, 5, 6]
print(bubble_sort(arr1))  # Output: [1, 2, 5, 5, 6, 9]

# Test case 2
arr2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(bubble_sort(arr2))  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Test case 3 (Already sorted)
arr3 = [1, 2, 3, 4, 5]
print(bubble_sort(arr3))  # Output: [1, 2, 3, 4, 5]

# Test case 4 (Reverse sorted)
arr4 = [5, 4, 3, 2, 1]
print(bubble_sort(arr4))  # Output: [1, 2, 3, 4, 5]
