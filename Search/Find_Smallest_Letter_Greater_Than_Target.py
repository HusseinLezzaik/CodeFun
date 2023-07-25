# Find Smallest L<etter Greater Than Target: https://leetcode.com/problems/find-smallest-letter-greater-than-target/

# O(logN) time, O(1) space
def nextGreatestLetter(letters, target):
    low, high = 0, len(letters)

    while low < high:
        mid = low + (high - low) // 2
        if letters[mid] <= target:
            low = mid + 1
        else:
            high = mid

    return letters[low % len(letters)]


# Test Cases
print(nextGreatestLetter(["c", "f", "j"], "a"))  # Expected output: "c"
print(nextGreatestLetter(["c", "f", "j"], "c"))  # Expected output: "f"