# Is Subsequence: https://leetcode.com/problems/is-subsequence/

# Solution 1 | O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)
  
 
# Solution 2 | O(n) Time | O(1) Space
def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)


s = "abc"
t = "ahbgdc"
print(isValidSubsequence(s, t))  # Expected output: True

s = "axc"
t = "ahbgdc"
print(isValidSubsequence(s, t))  # Expected output: False