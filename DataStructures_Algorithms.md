## Strategies
1) Invert Binary Tree
2) Reverse Linked List
3) Binary Search
4) Sliding Window (2 pointers)
5) Recursion (trees, graphs, backtracking, DP)
6) Dynamic Programming 
7) Merge & Quick Sort
8) Bit Operations
9) DFS & BFS (usually O(V+E) time/space complexity)
10) Heaps
11) Hash Maps

## Data Structures
1) Arrays:
- Accessing a value at a given index: O(1) 
- Updating a value at a given index: O(1)
- Traverse: O(n) Time, O(1) Space 
- Inserting a value at the beginning: O(n) 
- Inserting a value in the middle: O(n) 
- Inserting a value at the end:
a) Dynamic Array: O(1)
b) Static Array: O(n)
- Removing a value at the beginning: O(n)
- Removing a value in the middle: O(n)
- Removing a value at the end: O(1)
- Copying the array: O(n)

2) Strings:
- Most programming languages (C++ is exception), strings are immutable = can't be edited after creation
- Traverse: O(n) T, O(1) S
- Copy: O(n) TS
- Get: O(1) TS
- newString += character is O(n^2) each addition creates an entirely new string

3) Hash Tables:
- Extremely useful to any problem requiring some sort of lookup operation, array of Linked Lists
- Worse case = Collision of values, assume hash functions optimized and constant-time operations are guranteed
- Uses dynamic array of linked lists to efficiently store Key/Value pairs (hash function)
- Inserting a key/value pair: O(1) average, O(n) worse
- Removing a key/value pair: O(1) average, O(n) worse
- Looking up a key: O(1) average, O(n) worse

4) Stacks and Queues:
4.1. Stacks:
- LIFO (Last In First Out), stack of books on table, dynamic array or with a singly linked list
- Pushing an element onto stack: O(1)
- Popping an element off the stack: O(1)
- Peeking at the element on the top of the stack: O(1)
- Searching for an element in the stack: O(n)

4.2. Queue:
- FIFO (First In, First Out), line of people, doubly linked list
- Enqueuing an element into queue: O(1)
- Dequeuing an elemt out of the queue: O(1)
- Peeking at the element at the front of the queue: O(1)
- Searching for an element in the queue: O(n)

5) Linked Lists:
- Node with some value and a pointer to the next node in the linked list (Singly Linked list)
- Accessing the head: O(1)
- Accessing the tail: O(n) (with O(1) for doubly linked list)
- Accessing a middle node: O(n)
- Inserting/Removing the head: O(1)
- Inserting/Removing the tail: O(n) to access + O(1) (with O(1) for doubly linked list)
- Inserting/Removing a middle node: O(n) to access + O(1)
- Searching for a value: O(n)

6) Graphs:
- Collection of nodes called vertices that might be related with edges
- Graph Cycle, Acyclic Graph, Cyclic Graph, Directed Graph, Undirected Graph, Connected Graph

7) Trees:
- Useful at storing data hierarchically, useful for recursion problems
- Root, subtrees, branches, leaf nodes

7.1. Binary Trees:
- interior nodes all have two child-nodes, leaf nodes all have the same depth
- can use algos like BFS or DFS, values are ordered
- Insert: log(n)
- Remove: log(n)
- Search: log(n)

7.2. Min/Max Heaps:
- Special case of binary tree, with root smaller/greater or equal to children nodes
- currentNode = i, childOne -> 2i + 1, childTwo -> 2i + 2, parentNode -> floor((i - 1)/2)
- Tree but implemented as array with first element empty, main advantage u can get min/max value in constant time
- Node[i], leftChild[2i], rightChild[2i+1]
- Insert: log(n)
- Pop: log(n)
- Min/Max: O(1)
- Heapify: O(n)
- Building heap iteratively: O(nlogn)

7.3 Tries/Prefix Trees:
- each node can have up to 26 children, one of the characters of the alphabet
- benefit of prefix, easy to search for words that start with a, useful for autocomplete
- Insert: O(n)
- Search: O(n)

## Math
- 2^0 + 2^1 + 2^2 + 2^3 + .... + 2^n-1 = 2^n - 1 which is O(2^n)
- 1 + 2 + 3 + 4 + .. + n-1 = sum of 1 through n-1 = n(n-1)/2 which is O(n^2)

## Complexity
- *O(1)* < *O(logn)* < *O(n)* < *O(nlogn)* < *O(n^2)* < *O(n^3)* < *O(2^n)* < *O(n!)*
- Constant: *O(1)*, constant regardless of input size
- Logarithmic: *O(log(n))*, binary search, as input doubles, operations increment by one unit
- Linear: *O(n)*, scales linearily with input size
- O(ab): traversing through two arrays in two for-loops is not O(n^2) if they are not of same size. 
- Log-Linear: *O(nlog(n))*, sort an array of size n
- Quadratic: *O(n^2)*
- Cubic: *O(n^3)*
- Exponential: *O(2^n)*, recursive runtimes
- Factorial: *O(n!)*

## Power of 2 Tables
| Power | Exact Value | Approx Value | Bytes |
| :---- |                  ----: |         ----: |         ----:|
| 7     |                   128  |               |              |
| 8     |                   256  |               |              |
| 10    |                  1024  | 1 thousand    |         1 KB |
| 16    |                65,536  |               |        64 KB |
| 20    |             1,048,576  | 1 million     |         1 MB |
| 30    |         1,073,741,824  | 1 billion     |         1 GB |
| 32    |         4,294,967,296  |               |         4 GB |
| 40    |    1,099,511,627,776   | 1 trillion    |         1 TB |
| 50    | 1,125,899,906,842,624  | 1 quadrillion |         1 PB |

## Popular Algorithms
1) Traveling Salesman Problem:
- Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?

2) Floyd-Warshall Algorithm:
- Is an algorithm for finding shortest paths in a directed weighted graph with positive or negative edge weights.
- A single execution of the algorithm will find the lengths of shortest-paths between all pairs of vertices.
