# O(nlog(n)) time | O(n) space
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves.
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves.
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_ptr, right_ptr = 0, 0

    # Compare elements from both halves and merge them in ascending order.
    while left_ptr < len(left) and right_ptr < len(right):
        if left[left_ptr] < right[right_ptr]:
            merged.append(left[left_ptr])
            left_ptr += 1
        else:
            merged.append(right[right_ptr])
            right_ptr += 1

    # Add any remaining elements from the left and right halves.
    merged.extend(left[left_ptr:])
    merged.extend(right[right_ptr:])

    return merged

# Test case 1
arr1 = [5, 2, 9, 1, 5, 6]
print(merge_sort(arr1))  # Output: [1, 2, 5, 5, 6, 9]

# Test case 2
arr2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(merge_sort(arr2))  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Test case 3 (Already sorted)
arr3 = [1, 2, 3, 4, 5]
print(merge_sort(arr3))  # Output: [1, 2, 3, 4, 5]

# Test case 4 (Reverse sorted)
arr4 = [5, 4, 3, 2, 1]
print(merge_sort(arr4))  # Output: [1, 2, 3, 4, 5]
