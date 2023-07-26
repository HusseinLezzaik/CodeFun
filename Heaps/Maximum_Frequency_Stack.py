# Maximum Frequency Stack: https://leetcode.com/problems/maximum-frequency-stack/

"""
The time complexity of both push() and pop() operations is O(1) because we use a dictionary to keep track of the frequency of each element and a list to keep track of the elements at each frequency.
The space complexity is O(n), where n is the number of elements in the stack, because in the worst-case scenario, we might have to store all elements in the dictionary and the list.
"""

from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = Counter()
        self.group = defaultdict(list)
        self.maxfreq = 0

    def push(self, val):
        freq, group = self.freq, self.group
        freq[val] += 1
        self.maxfreq = max(self.maxfreq, freq[val])
        group[freq[val]].append(val)

    def pop(self):
        freq, group, maxfreq = self.freq, self.group, self.maxfreq
        val = group[maxfreq].pop()
        if not group[maxfreq]:
            self.maxfreq = maxfreq - 1
        freq[val] -= 1
        return val

# Test the FreqStack class
freqStack = FreqStack()

freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)

print(freqStack.pop())  # return 5, as it is the most frequent and the latest to be pushed
print(freqStack.pop())  # return 7
print(freqStack.pop())  # return 5
print(freqStack.pop())  # return 4