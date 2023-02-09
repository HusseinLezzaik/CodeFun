```
LeetCode Palindrome Number #9

Link: https://leetcode.com/problems/palindrome-number/description/
```

# 1st Solution | O(n) time | O(n) space
def isPalindrome(self, x: int) -> bool:
    if x<0:
      return False # negative numbers are not palindrome
    num = x
    num_str = str(num)
    if num_str == num_str[::-1]:
        return True
    return False
        
# 2nd Solution | O(logn) time | O(1) space -- logn_10 because we're dividing input by 10 each iteration
def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False # negative numbers are not palindrome
    original_x = x
    reverse_x = 0
    while x > 0:
        reverse_x = reverse_x * 10 + x % 10
        x = x // 10
    return original_x == reverse_x

# 3rd Solution | O(logn) time | O(1) space -- log_10
def isPalindrome(self, x: int) -> bool:
    # When x < 0, x is not a palindrome.
    # Also if the last digit of the number is 0, in order to be a palindrome,
    # the first digit of the number also needs to be 0.
    # Only 0 satisfy this property.
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    revertedNumber = 0
    while x > revertedNumber:
        revertedNumber = revertedNumber * 10 + x % 10
        x //= 10

    # When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
    # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
    # since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
    return x == revertedNumber or x == revertedNumber//10
