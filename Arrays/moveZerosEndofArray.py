"""
Move Zeros to End of Array:
Given an array of integers, move all zeros to the end of the array while maintaining the relative order of non-zero elements.
"""

def moveZerosToEnd(arr):
    # Initialize two pointers
    non_zero = 0  # Pointer for placing non-zero elements

    # Traverse the array
    for i in range(len(arr)):
        if arr[i] != 0:
            # Swap the current non-zero element with the element at non_zero pointer
            arr[i], arr[non_zero] = arr[non_zero], arr[i]
            non_zero += 1
    
    return arr

# Test the function
arr = [0, 1, 0, 3, 12]
print("Original array:", arr)
result = moveZerosToEnd(arr)
print("Array after moving zeros to end:", result)