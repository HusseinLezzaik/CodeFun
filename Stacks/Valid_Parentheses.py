# This is the "Valid Parentheses" problem on LeetCode: https://leetcode.com/problems/valid-parentheses/

# Time Complexity: O(n) | Space Complexity: O(n)
def isValid(s: str) -> bool:
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []
    for i in s:
        if i in open_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
        else:
            return False
    return stack == []

s = "()"
print(isValid(s)) # True

s = "()[]{}"
print(isValid(s)) # True

s = "(]"
print(isValid(s)) # False