# Group Anagrams: https://leetcode.com/problems/group-anagrams/

"""
The time complexity of this algorithm is O(NMlogM), where N is the number of words, and M is the maximum length of a word.
This is because each word is sorted in O(MlogM) time, and this is done N times.

The space complexity is O(NM), because we are storing all the words in the hash table. 
In the worst case, if all words are the same, the length of the words will contribute to the space complexity.
"""

def groupAnagrams(strs):
    anagram_map = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_map:
            anagram_map[sorted_word] = [word]
        else:
            anagram_map[sorted_word].append(word)
    return list(anagram_map.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Expected output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(groupAnagrams([""]))  # Expected output: [[""]]
print(groupAnagrams(["a"]))  # Expected output: [["a"]]