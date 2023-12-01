# Python Terminologies
"""
1. Decorators @
2. List Comprehension: [expression for item in iterable] or [expression for item in iterable if condition]
3. f-strings
4. Type Hints: The nums: List[int] -> int part is a type hint. nums: List[int] suggests that the nums parameter should be a list of integers, and -> int suggests that the function should return an integer. Type hints like these are optional in Python and are often used to make the code more readable and self-explanatory.
5. Continue
6. Operator Overloads
7. Primitive Types: int, float, bool, str, None
"""

# Bits
a = 5
b = 3

print(bin(a)) # 00000101
print(bin(b)) # 00000011

# Bitwise AND
"""
If you AND a bit with 0, the result is always 0
If you AND a bit with 1, the result is the original bit
This is often used to create a mask to "turn off" certain bits 

You can check if a number is even or odd using AND operation
num & 1 will be 0 if num is even (the last bit of an even number is always 0)
num & 1 will be 1 if num is odd (the last bit of an odd number is always 1)
"""
and_result = a & b
print(bin(and_result)) # 00000001 (1)

even = a & 1 == 0 # True
odd = a & 1 == 1 # False

# Bitwise OR
"""
If you OR a bit with 0, the result is the original bit. 
If you OR a bit with 1, the result is always 1. 
This can be used to create a mask to "turn on" certain bits.
"""
or_result = 5 | 3
print(bin(or_result)) # 00000111  (7)

# Bitwise XOR
"""
XOR is true whenever an odd number of bits are true.
If you XOR a bit with 0, the result is the original bit. 
If you XOR a bit with 1, the result is the inverted bit.
This can be used to toggle certain bits.

A XOR A = 0
A XOR 0 = A
A XOR B XOR A = B (can be used for swapping two numbers)
"""
xor_result = 5 ^ 3
print(bin(xor_result)) # 00000110 (6)

A = 5
B = 3
# XOR property
A_XOR_A = A ^ A
A_XOR_B_XOR_A = A ^ B ^ A

# Swap numbers using XOR
A ^= B # A = A ^ B
B ^= A # B = B ^ (A ^ B) = A
A ^= B # A = (A ^ B) ^ A = B

# Bitwise NOT
"""
The NOT operation inverts each bit.
This is equivalent to adding one to the number and then changing its sign.
"""
not_result = ~5
print(not_result) # -00000110 (-6)

# Left shift
"""
Each left shift multiplies the number by 2. 
"""

left_shift_result = 5 << 1
print(bin(left_shift_result)) # 0b1010 (10)

left_shift_steps = [a << i for i in range(5)] # each left shift multiplies the number by 2
left_shift_binaries = [bin(val)[2:].zfill(8) for val in left_shift_steps]
print(left_shift_binaries) # ['00000101', '00001010', '00010100', '00101000', '01010000']

# Right shift
"""
Each right shift divides the number by 2.
"""
right_shift_result = 5 >> 1
print(bin(5)) # 00000101
print(bin(right_shift_result)) # 0b10 (2)

right_shift_steps = [a >> i for i in range(5)] # each right shift divides the number by 2
right_shift_binaries = [bin(val)[2:].zfill(8) for val in right_shift_steps] 
print(right_shift_binaries) # ['00000101', '00000010', '00000001', '00000000', '00000000']

# Arrays
array = [[0 for i in range(cols)] for j in range(rows)]] # Initialize a 2D array
array = [[0] * cols] * rows # Initialize a 2D array
array = [1] * n # Initialize an array of size n with all 1s
array = []
length = len(array)
combined = array1 + array2
count = array.count(3) # Count the number of occurrences of 3
array1.extend(array2) # Append array2 to array1
sub_array = array[1:3]
reversed_array = array[::-1]
reversed_array = array.reverse()
array.sort()
array.sort(reverse=True)
array.sort(key=lambda x: x[1])
array.append(1)
array.insert(0, 0)  # Insert 0 at the first position
array.remove(2)  # Remove the first occurrence of 2
array.pop(1)  # Remove and return the second element

# Strings
name = "Alice"
print(f"Hello, {name}!") # You can put any Python expression inside the curly braces {} in an f-string, and it will be evaluated and inserted into the string.
num_str = num_str[::-1] # Reverse a string
str = "abc"
unicode = ord(str[0]) # Get the unicode of the first character
print(ord('a'))  # Output: 97
print(chr(97))  # Output: 'a'
print(ord('z')) # Output: 122
print(ord('A')) # Output: 65
print(ord('Z')) # Output: 90
newstring = ''.join(reversed(str))  # Reverse a string
newstring = ''.join(sorted(str))  # Sort a string
newstring = ''.join(sorted(str, reverse=True))  # Sort a string in descending order
character = string[2]
length = len(string)
substring = string[1:3]
combined
count = string.count('a') # Count the number of occurrences of 'a'
string1 = string1 + string2
string1 += string2
string1 = string1 * 3
new_string = string.replace('a', 'b') # Replace all occurrences of 'a' with 'b'
start = string.startswith('a') # Returns True if string starts with 'a'
ends = string.endswith('a') # Returns True if string ends with 'a'
upper_string = string.upper() # Convert string to uppercase
lower_string = string.lower() # Convert string to lowercase
split_string = string.split(',') # Split string by comma
stripped_string = string.strip() # Remove leading and trailing whitespaces

# Sets
set = set()
set.add(1)
set.remove(1)
set.discard(1)
exists = 1 in set
set1 = set1.union(set2) # set1 | set2
set1 = set1.intersection(set2) # set1 & set2
set1 = set1.difference(set2) # set1 - set2
set1 = set1.symmetric_difference(set2) # set1 ^ set2
set.clear() # Remove all elements from the set
new_set = set.copy() # Create a copy of the set
is_subet = set1.issubset(set2) # Returns True if set1 is a subset of set2
is_superset = set1.issuperset(set2) # Returns True if set1 is a superset of set2

# Hash Tables
hash_table = {}
hash_table[key] = value
hash_table[key] = hash_table.get(key, 0) + 1 # Increment the value of key by 1
hash_table.get(x, -1) # Return -1 if x is not found
value = hash_table['key']
exists = 'key' in hash_table
del hash_table['key'] # Delete key from hash_table
hash_table.clear() # Remove all elements from the hash table
new_hash_table = hash_table.copy() # Create a copy of the hash table
keys = hash_table.keys() # Return a list of keys
values = hash_table.values() # Return a list of values
items = hash_table.items() # Return a list of key-value pairs
hash_table.pop('key') # Remove and return the value of key
hash_table.popitem() # Remove and return an arbitrary key-value pair

# Tuples (List but Immutable)
tup = (1, 2)
element = tup[1]
length = len(tup)
combined = tup1 + tup2
count = tup.count(3) # Count the number of occurrences of 3
index = tup.index(3) # Return the index of the first occurrence of 3
sub_tup = tup[1:3]
sorted_list = sorted(tup)
combined = tup1 + tup2
tup1 += tup2
tup1 = tup1 * 3
nested_tup = ((1, 2), (3, 4))

# Dictionary
dic = {}
dic = {'a': 1, 'b': 2}
dic['a'] = 1
dic['a'] = dic.get('a', 0) + 1 # Increment the value of key by 1
value = dic['key']
exists = 'key' in dic
del dic['key'] # Delete key from dic
dic.clear() # Remove all elements from the dictionary
new_dic = dic.copy() # Create a copy of the dictionary
keys = dic.keys() # Return a list of keys
values = dic.values() # Return a list of values
items = dic.items() # Return a list of key-value pairs
dic.pop('key') # Remove and return the value of key
dic.popitem() # Remove and return an arbitrary key-value pair

# Stacks (LIFO)
stack = []
stack_new = stack.pop() # Remove and return the top element
stack_new = stack.append()
is_empty = not stack
size = len(stack)
stack.clear()

# Queues (FIFO)
from collections import deque
queue = []
queue_new = queue.popleft()
queue_new = queue.append()
first_element = queue[0]
is_empty = not queue
size = len(queue)
queue.clear()

# Heaps
import heapq # Min Heap, add -ve sign to make it a Max Heap
heap = []
heapq.heapify(heap)
heapq.heappush(heap, 'element') # ensures that the smallest element is always at the front
heapq.heappop(heap) # Remove and return the smallest element
heapq._heapify_max(stones) # There's a private _heapify_max method, Transform list into a maxheap, in-place, in O(len(x)) time: https://github.com/python/cpython/blob/1170d5a292b46f754cd29c245a040f1602f70301/Lib/heapq.py#L198
smallest_element = heapq.heappop(heap) # Remove and return the smallest element
heappushpop_element = heapq.heappushpop(heap, 'element') # Push element on the heap, then pop and return the smallest element
heapreplace_element = heapq.heapreplace(heap, 'element') # Pop and return the smallest element, then push element
n_smaallest_elements = heapq.nsmallest(3, heap) # Return a list with the 3 smallest elements
n_largeest_elements = heapq.nlargest(3, heap) # Return a list with the 3 largest elements

# Trie (prefix tree)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Linked Lists
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
"""
1. Insert an element at the front of the linked list
2. Insert an element at the end of the linked list
3. Insert an element after a given node
4. Remove an element from the linked list
5. Find the length of the linked list
6. Search for an element in the linked list
"""

# Binary Tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Directed Graph
class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, from_node, to_node):
        if from_node in self.graph:
            self.graph[from_node].append(to_node)
        else:
            self.graph[from_node] = [to_node]

G = DirectedGraph()

G.add_node('A')
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'C')
G.add_edge('C', 'A')

print(G.graph) # {'A': ['B', 'C'], 'B': ['C'], 'C': ['A']}

# Math
x = float('-inf') # Negative infinity
import random
x = random.uniform(0, 1) # Random float between 0 and 1
x = 2 ** 3  # 2^3 = 8
x = pow(2, 3)  # 2^3 = 8
x % 2 == 0  # Check if x is even
middle = (left + right) // 2

# Padding
number = 5.1234
formatted_number = "%08.3f" % number # 8 characters long include decimal point '.', 3 decimals
print(formatted_number)  # Output: "0005.123

# For Loops
for i in range(0, 10):
    print(i)
for i in range(0, 10, 2):
    print(i)
for i in range(10, 0, -1):
    print(i)
for i in reversed(range(0, 10)):
    print(i)   
for idx, duration in enumerate(queries):
    print(idx, duration)   
for _ in range(10):
    print("Hello") 
for x,y in zip(list1, list2):
    print(x,y)

# Python Truthiness
if not matrix:
    return result #This "truthiness" property of Python objects is an example of Python's high-level, abstracted design, which is intended to make the language more intuitive and easier to use.

# List Comprehension
window_vowels = sum(1 for i in range(k) if s[i] in vowels)

# Assert
assert 1 == 1  # No output
assert 1 == 2  # AssertionError
assert stack.peek() == 'cherry'

# Sort
array.sort()  # Sorts in ascending order
array.sort(reverse=True)  # Sorts in descending order
sorted_array = sorted(array)  # Returns a sorted array
sorted_array = sorted(array, reverse=True)  # Returns a sorted array in descending order
array.sort(key=len)  # Sorts based on string length

# Lambda Functions
lambda arguments: expression

add = lambda x, y: x + y
print(add(5, 3)) # 8

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

numbers = [1, 2, 3, 4, 5, 6]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25, 36]

array = [(1, 'b'), (2, 'a'), (3, 'c')] # Sort the array based on the second element of each tuple
array.sort(key=lambda x: x[1]) # [('2', 'a'), ('1', 'b'), ('3', 'c')]

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 25}
]
people.sort(key=lambda x: x['age']) # Sort list of dictionaries by age

# Operator Overloading
class Person:
    def __init__(self, name):
        self.name = name
    def __add__(self, other):
        return self.name + other.name
    def __mul__(self, other):
        return self.name * other
    def __pow__(self, other):
        return self.name * other
    
# Positional and KeyWord Argumements
"""
1. Positional Arguments (*args): Positional arguments are passed in a specific order, and the order matters. 
A tuple is an ordered collection, so it's a natural choice for capturing additional positional arguments. 
When you use *args, all extra positional arguments are packed into a tuple, preserving their order.

2. Keyword Arguments (**kwargs): Keyword arguments are passed by explicitly naming the parameter along with its value, like key=value. 
Since dictionaries are collections of key-value pairs, they are a suitable choice for capturing extra keyword arguments.
When you use **kwargs, all extra keyword arguments are packed into a dictionary, with the parameter names as keys and the corresponding values as values.
"""
def example_function(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)   # Prints extra positional arguments
    print("kwargs:", kwargs) # Prints extra keyword arguments

# Calling the function with extra positional and keyword arguments
example_function(1, 2, 3, 4, 5, extra_param1="value1", extra_param2="value2")
# Output
       # a: 1
       # b: 2
       # args: (3, 4, 5)
       # kwargs: {'extra_param1': 'value1', 'extra_param2': 'value2'}