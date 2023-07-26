# Reorganize Strings: https://leetcode.com/problems/reorganize-string/

"""
The time complexity of the reorganizeString function is O(nlogn), where n is the length of the string. 
This is because we use a max heap to store the frequency and character, and both insertion and deletion in a heap take O(logn) time.

The space complexity is O(n) because we store the characters of the string in a max heap, which takes O(n) space.
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""
        
        counter = Counter(s)
        max_heap = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(max_heap)
        
        prev_char = None
        prev_freq = 0
        result = []
        
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)
            
            if prev_char and prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
                
            prev_char, prev_freq = char, freq + 1
            
        reorganized = ''.join(result)
        
        if len(reorganized) != len(s):
            return ""
        
        return reorganized

# Test the reorganizeString function
sol = Solution()

s = "aaab"
print("The reorganized string is:", sol.reorganizeString(s))  # return ""