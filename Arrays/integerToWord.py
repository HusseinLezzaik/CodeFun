class Solution:
    def numberToWords(self, num: int) -> str:
        # Define dictionaries for number-to-word mappings
        ones = {
            1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'
        }
        tens = {
            10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'
        }
        twenties = {
            2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty',
            6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'
        }
        thousands = ['', 'Thousand', 'Million', 'Billion']

        def helper(n):
            if n == 0:
                return []
            elif n < 10:
                return [ones[n]]
            elif n < 20:
                return [tens[n]]
            elif n < 100:
                return [twenties[n // 10]] + helper(n % 10)
            else:
                return [ones[n // 100], 'Hundred'] + helper(n % 100)

        if num == 0:
            return 'Zero'

        result = []
        for i in range(len(thousands)):
            if num % 1000 != 0:
                result = helper(num % 1000) + ([thousands[i]] if i > 0 else []) + result
            num //= 1000
            if num == 0:
                break

        return ' '.join(result)

# Example usage
solution = Solution()
print(solution.numberToWords(123456789))  # Output: "One Hundred Twenty Three Million Four Hundred Fifty Six Thousand Seven Hundred Eighty Nine"
print(solution.numberToWords(1234567891))  # Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

# Time Complexity: O(log n), where n is the input number.
# The number of digits in n is proportional to log n, and we process each group of three digits.

# Space Complexity: O(1)
# The space used is constant as the output string's length is bounded
# (the longest word representation is for numbers just below 1 billion).
# The recursion depth is also constant as it only goes up to 3 levels deep for each thousands group.