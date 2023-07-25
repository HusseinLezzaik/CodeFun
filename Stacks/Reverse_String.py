# Reverse a string using a stack https://leetcode.com/problems/reverse-string/

# Time Complexity: O(n^2) | Space Complexity: O(n)
def reverse_string(s: str) -> str:
    stack = list(s)
    result = ''
    while stack:
        result += stack.pop()
    return result

# Time Complexity: O() | Space Complexity: O(n)
def reverse_string(s: str) -> str:
    stack = list(s)
    result = []
    while stack:
        result.append(stack.pop())
    return ''.join(result)


s = ["h","e","l","l","o"]
print(reverse_string(s)) # "olleh"
      
s = ["H","a","n","n","a","h"]
print(reverse_string(s)) # "hannaH"