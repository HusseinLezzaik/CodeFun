```
LeetCode Palindrome Number #9

Link: https://leetcode.com/problems/palindrome-number/description/
```

# 1st Solution | O(n) time | O(n) space
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
          return False # negative numbers are not palindrome
        num = x
        num_str = str(num)
        if num_str == num_str[::-1]:
            return True
        return False
        
# 2nd Solution | O(logn) time | O(1) space
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False # negative numbers are not palindrome
        original_x = x
        reverse_x = 0
        while x > 0:
            reverse_x = reverse_x * 10 + x % 10
            x = x // 10
        return original_x == reverse_x
