# O(k*N) time, O(N) space
def radix_sort(arr):
    # Find the maximum number to determine the number of digits.
    max_num = max(arr)
    exp = 1

    # Perform counting sort for each digit, starting from the least significant digit.
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count the occurrences of each digit.
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Calculate the cumulative count.
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array in sorted order based on the current digit.
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the sorted elements back to the original array.
    for i in range(n):
        arr[i] = output[i]

# Test case
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)  # Output: [2, 24, 45, 66, 75, 90, 170, 802]
