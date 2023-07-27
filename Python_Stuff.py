# Python Terminologies
"""
1. Decorators @
2. List Comprehension: [expression for item in iterable] or [expression for item in iterable if condition]
3. f-strings
4. Type Hints: The nums: List[int] -> int part is a type hint. nums: List[int] suggests that the nums parameter should be a list of integers, and -> int suggests that the function should return an integer. Type hints like these are optional in Python and are often used to make the code more readable and self-explanatory.
5. Continue
6. Operator Overloads
"""

# Bits

# Arrays
array = [[0 for i in range(cols)] for j in range(rows)]] # Initialize a 2D array
array = [[0] * cols] * rows # Initialize a 2D array
array = [1] * n # Initialize an array of size n with all 1s
array = []
array.append(1)
array.insert(0, 0)  # Insert 0 at the first position
array.remove(2)  # Remove the first occurrence of 2
array.pop(1)  # Remove and return the second element

# Strings
name = "Alice"
print(f"Hello, {name}!") # You can put any Python expression inside the curly braces {} in an f-string, and it will be evaluated and inserted into the string.
num_str = num_str[::-1] # Reverse a string
str = "abc"
newstring = ''.join(reversed(str))  # Reverse a string
newstring = ''.join(sorted(str))  # Sort a string
newstring = ''.join(sorted(str, reverse=True))  # Sort a string in descending order

# Sets
set = set()
set.add(1)
set.remove(1)
set.discard(1)

# Hash Tables
node = {}
node[key] = value
node[key] = node.get(key, 0) + 1 # Increment the value of key by 1
node.get(x, -1) # Return -1 if x is not found

# Tuples
tup = (1, 2)

# Dictionary
dic = {}
dic = {'a': 1, 'b': 2}
dic['a'] = 1
dic['a'] = dic.get('a', 0) + 1 # Increment the value of key by 1

# Stacks
stack = []
stack_new = stack.pop()
stack_new = stack.append()

# Queues
from collections import deque
queue = []
queue_new = queue.popleft()
queue_new = queue.append()

# Heaps
import heapq
heap = []
heapq.heapify(heap)
heapq.heappush(heap, -duration)
heapq.heappop(heap)

# Math
x = float('-inf') # Negative infinity
import random
x = random.uniform(0, 1) # Random float between 0 and 1
x = 2 ** 3  # 2^3 = 8
x = pow(2, 3)  # 2^3 = 8
x % 2 == 0  # Check if x is even
middle = (left + right) // 2

# Sort
array.sort()  # Sorts in ascending order
array.sort(reverse=True)  # Sorts in descending order

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

# Python Truthiness
if not matrix:
    return result #This "truthiness" property of Python objects is an example of Python's high-level, abstracted design, which is intended to make the language more intuitive and easier to use.

# List Comprehension
window_vowels = sum(1 for i in range(k) if s[i] in vowels)

# Assert
assert 1 == 1  # No output
assert 1 == 2  # AssertionError
assert stack.peek() == 'cherry'

# Lambda Functions
array.sort(key=lambda x: x[1])
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
