# Backspace String Compare: https://leetcode.com/problems/backspace-string-compare/

# O(n) time | O(1) space
def backspace_compare(s: str, t: str) -> bool:
    def find_next_valid_char(string: str, pointer: int) -> int:
        backspace_count = 0
        while pointer >= 0:
            if string[pointer] == '#':
                backspace_count += 1
            elif backspace_count > 0:
                backspace_count -= 1
            else:
                break
            pointer -= 1
        return pointer

    pointer_s = len(s) - 1
    pointer_t = len(t) - 1

    while pointer_s >= 0 or pointer_t >= 0:
        pointer_s = find_next_valid_char(s, pointer_s)
        pointer_t = find_next_valid_char(t, pointer_t)

        if pointer_s < 0 and pointer_t < 0:
            return True
        if pointer_s < 0 or pointer_t < 0:
            return False
        if s[pointer_s] != t[pointer_t]:
            return False

        pointer_s -= 1
        pointer_t -= 1

    return True


# Test cases
print(backspace_compare('xy#z', 'xzz#'))  # Expected output: True
print(backspace_compare('xy#z', 'xyz#'))  # Expected output: False