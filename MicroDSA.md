## MicroDSA: Data Structures and Algorithms 

Data structures and algorithms represent the core fundamentals of computer science and software design.  Below is a minimal reference for a refresher on the topic.

## Data Structures

## Bits
- **Bitwise AND** *('&')*: Takes two numbers as operands and does an AND operation on every bit of the two numbers.
- **Bitwise OR** <i>('|')</i>: Takes two numbers as operands and does an OR operation on every bit of the two numbers.
- **Bitwise XOR** *('^')*: Takes two numbers as operands and does an XOR operation on every bit of the two numbers.
- **Bitwise NOT** *('~')*: Takes one number as an operand and inverts all the bits of its binary representation.
- **Left Shift** *('<<')*: Takes two numbers as operands and shifts the bits of the first operand to the left by the number of positions given by the second operand. New bits on the right side are filled with zeros.
- **Right Shift** *('>>')*: Takes two numbers as operands and shifts the bits of the first operand to the right by the number of positions given by the second operand.

### Arrays
- **Access:** *O(1)* 
- **Update:** *O(1)*
- **Traverse:** *O(n) Time, O(1) Space* 
- **Insert Beginning:** *O(n)* 
- **Insert Middle:** *O(n)* 
- **Insert End:**
    - *Dynamic Array: O(1)*
    - *Static Array: O(n)*
- **Remove Beginning:** *O(n)*
- **Remove Middle:** *O(n)*
- **Remove End:** *O(1)*
- **Copy Array:** *O(n)*

### Stacks and Queues
#### Stacks
- **LIFO (Last In, First Out)**
- **Push:** *O(1)*
- **Pop:** *O(1)*
- **Peek:** *O(1)*
- **isEmpty:** *O(1)*
- **Search:** *O(n)*
- **Data Structures:** Singly Linked List
- **Examples:** Stack of Books on Table

#### Queue
- **FIFO (First In, First Out)**
- **Enqueuing:** *O(1)*
- **Dequeuing:** *O(1)*
- **Peek:** *O(1)*
- **isEmpty:** *O(1)*
- **Search:** *O(n)*
- **Data Structures:** Doubly Linked List
- **Examples:** Line of People

### Strings
- **Traverse:** *O(n) Time & O(1) Space*
- **Copy:** *O(n)*
- **Get:** *O(1)*
- **Note:** In most programming languages (C++ exception), strings are **immutable** = can't be edited after creation: **newString += character** is *O(n^2)* each addition creates an entirely new string

### Hash Tables
- **Insert:** *O(1)*
- **Remove:** *O(1)*
- **Search:** *O(1)*
- **Data Structures:** Dynamic Array of Linked Lists

### Linked Lists
- **Access Head:** *O(1)*
- **Access Tail:** *O(n)* (*O(1)* for Doubly Linked List)
- **Access Middle:** *O(n)*
- **Insert/Remove Head:** *O(1)*
- **Insert/Remove Tail:** *O(n) to access* + *O(1)* (with *O(1)* for doubly linked list)
- **Insert/Remove Middle:** *O(n)* to access + *O(1)*
- **Search:** *O(n)*
- **Types:** Singly List, Doubly List, Circular List, Skip List, Multilevel Lists

### Graphs
- **Definition:** Collection of **Nodes** called **Vertices** that might be related with **Edges**
- **Types:** Graph Cycle, Acyclic Graph, Cyclic Graph, Directed Graph, Undirected Graph, Connected Graph
- **Algorithms:** Depth First Search, Breadth First Search O(V+E)

### Trees
- **Use Cases:** Useful at **storing data hierarchically**, and **recursion** problems
- **Terminology:** Root, Subtrees, Leaf Nodes

#### 1. Binary Trees
- **Insert:** *log(n)*
- **Remove:** *log(n)*
- **Search:** *log(n)*
- **Data Structure:** Interior **nodes** at most have **two child-nodes** (Balanced tree has exactly two nodes)
- **Algorithms:** Invert Binary Tree, Find Max Depth

#### 2. Binary Search Trees (BST)
- **Definition:** For any given node, all nodes in its **left subtree** have values that are **less than** the node's value, and all nodes in its **right subtree** have values that are **greater than** the node's value.
- **Algorithms:** Search for Value, Check Whether a BST, Insert Node
- **Use Cases:** You can rule out half the tree on a single comparison

#### 3. Heaps
- For any element at index i in the array:
    - Its left child is located at *2i + 1*
    - Its right child is at *2i + 2*
    - Its parent is at *(i - 1) // 2*

#### 3.1 Min Heap
- **Min Heap:** In a min heap, for any given node I, the value of I is less than or equal to the values of its children. This means that the minimum value is located at the root of the tree.
- **Min:** *O(1)*
- **Insert:** *log(n)*
- **Pop:** *log(n)*
- **Heapify:** *O(n)*
- **Building heap iteratively:** *O(nlogn)*

#### 3.2 Max Heap
- **Max Heap:** In a max heap, for any given node I, the value of I is greater than or equal to the values of its children. This means that the maximum value is located at the root of the tree.
- **Max:** *O(1)*
- **Insert:** *log(n)*
- **Pop:** *log(n)*
- **Heapify:** *O(n)*
- **Building heap iteratively:** *O(nlogn)*

#### 4. Tries (Prefix Tree)
- **Definition:** Tree-like data structure that is used to store a **dynamic set** or **associative array** where the **keys** are usually **strings**
- **Insert:** *O(n)*
- **Search:** *O(n)*
- **Use Cases:** 
    - Typically used for efficient retrieval of data associated with keys. Very suitable for tasks such as **word lookups**, providing **auto-complete** suggestions, **spell-checking**, and **IP routing**
    - It's most commonly used to store a collection of strings where quick prefix queries are required.

## Math
- **2^0 + 2^1 + 2^2 + 2^3 + .... + 2^n-1 = 2^n - 1** which is *O(2^n)*
- **1 + 2 + 3 + 4 + .. + n-1 =** sum of 1 through n-1 = **n(n-1)/2** which is *O(n^2)*

## Complexity
- **O(1) < *O(logn)* < *O(n)* < *O(nlogn)* < *O(n^2)* < *O(n^3)* < *O(2^n)* < O(n!)**
- **Constant:** *O(1)*, constant regardless of input size
- **Logarithmic:** *O(log(n))*, binary search, as input doubles, operations increment by one unit
- **Linear:** *O(n)*, scales linearily with input size
- **O(ab):** traversing through two arrays in two for-loops is not O(n^2) if they are not of same size. 
- **Log-Linear:** *O(nlog(n))*, sort an array of size n
- **Quadratic:** *O(n^2)*
- **Cubic:** *O(n^3)*
- **Exponential:** *O(2^n)*, recursive runtimes
- **Factorial:** *O(n!)*

## Power of Two Tables
![](/images/power-2.webp "Multiples of two, useful for memory estimation")

## LeetCode Patterns
**1. Arrays**
- **Common techniques:** Hash Tables, Sets
- **Common problems:** Duplicates, Numbers Retrieval and Insertion, 2D-Arrays (Traversal, Rotation, Spiral, Product Except Self), Longest Consecutive Sequence

**2. Two Pointers**
- **Common techniques:** Linkedlist, Hash Tables, Array Traversal, Two Indexes, Reduce Time Complexity from O(n^2) to O(n)
- **Common problems:** Sorted Lists (Square, Merge), N-sum, Subsequence, Sub-array Product, Sort Colors, Trapping Rain Water, Container With Most Water

**3. Sliding Window**
- **Common techniques:** Traverse with Sub-arrays that Shrink or Expand
- **Common problems:** Maximum Average Subarray I, Minimum Size Subarray Sum, Fruit Into Baskets, Permutatino in String, Longest Repeating Character Replacement, Longest Substring Without Repeating Characters

**4. Intervals**
- **Common techniques:** Involve some kind of Interval, Range, or Period of Time
- **Common problems:** Merge/Insert/Non-overlapping Intervals, Meeting Rooms

**5. Greedy**
- **Common techniques:** Local Optimal solution to evolve into Global Optimal
- **Common problems:** Optimization, BEST Time to: Buy/Sell Stocks, Schedules, Calendar

**6. Dynamic Programming**
- **Common techniques:** Arrays, Strings, Hash Tables, Trees
- **Common problems:** Target Sum, Climbing Stairs, Maximum Product/Subarray, Longest Subsequence/Substring

**7. Binary Search**
- **Common techniques:** Recursive or Iterative
- **Common problems:** FIND Smallest Letter/Duplicate/Peak Element/K-Closest Element, SEARCH a 2D/Rotated Matrix

**8. Fast & Slow Pointers**
- **Common techniques:** Traverse Linked-list, Two pointers are initialized at the start of the list. One pointer, the “slow” pointer, moves one step at a time, while the other pointer, the “fast” pointer, moves two steps at a time
- **Common problems:** Detecting Cycles in a Linked List, Finding The Middle Element or Kth Element from the End, Remove Linked List Elements

**9. Linked Lists**
- **Common techniques:** Iterative, Recursive, Traversal, Bi-directional, Backward
- **Common problems:** Reverse Linked Lists, Rotate Lists, Swap Nodes in Pairs, Reverse Nodes In K-Group

**10. Bit Manipulation**
- **Common techniques:** Shifting Bits Left or Right, Flipping Bits (changing 0 to 1 or 1 to 0), or Combining Numbers with bitwise operations such as AND, OR, XOR, and NOT
- **Common problems:** Missing/Counting Numbers, Reverse/Count Bits

**11. Graph**
- **Common techniques**: Traversal, Modification, or Analysis of a Graph
- **Common problems:** Clone Graph, Course Schedule, All Paths From Source to Target, Network Delay Time, Minimum Height Tree

**12. Depth-First Search**
- **Common techniques:** Traversing or Searching Trees or Graphs. The algorithm starts at the root and explores as far as possible along each branch before backtracking
- **Common problems:** Invert Binary Tree, Path/Target Sum, Min/Max Depth of Binary Tree, Diameter of Binary Tree, Merge Two Binary Trees, Binary Tree Paths, Kth Smallest Element in a BST, Course Schedule, Lowest Common Ancestor of a Binary Tree, Validate Binary Tree Search, Word Search

**13. Breadth-First Search**
- **Common techniques:** Traversing or Searching Trees or Graphs. It starts at the root and explores all the neighbor nodes at the present depth before moving on to nodes at the next depth level
- **Common problems:** Invert Binary Tree, Average of Levels In Binary Tree, Min Depth of Binary Tree, Clone Graph, Number of Islands, Minimum Height Trees, Binary Tree Level Order Traversal, Populating Next Right Pointers In Each Node, Course Schedule, Pacific Atlantic Water Flow

**14. Sort**
- **Common techniques:** Bubble, Selection, Insertion, Merge, Quick, Heap, Bucket, Radix, Counting
- **Common problems:** Majority Element, Re-order Data in Log Files, Group/Valid Anagrams, Largest Number

**15. Stacks**
- **Common Operations:** Push, Pop, Peek, isEmpty
- **Common problems:** Valid Parentheses, Reverse String, Implementing Stack using Queues & Singly Linked List, Largest Rectangle in Histogram, Next Greater Element I

**16. Queues**
- **Common techniques:** Enqueue, Dequeue, Peek, isEmpty
- **Common problems:** Design Circular Queue, Implement Queue using Stacks & Doubly Linked List, Binary Tree Level Order Traversal

**17. Heap**
- **Common techniques:** Min/Max Heap, Insertion/Deletion, usually implemented as Binary Trees
- **Common problems:** Kth Smallest Element in Sorted Matrix, Find K Pairs with Smallest Sums, K Closest Points to Origin, Top K Frequent Elements, Kth Largest Element in an Array, Reorganize String, Merge K Sorted Lists, Smallest Range Covering Elements from K Lists, Maximum Frequency Stack, Sliding Window Median, Find Median from Data Stream

**18. Trie**
- **Common techniques:** Known as Prefix Tree, used to store associative data structures, main operations are Insertion/Search/Delete
- **Common problems:** Index Pairs of a String, Implement Trie, Longest Word in Dictionary, Word Search II, Maximum XOR of Two Numbers in an Array, Word Search II, Concatenated Words, Prefix and Suffix Search, Palindrome Pairs, Design Search Autocomplete System, Word Squares

## Popular Algorithm Problems
**1. Traveling Salesman**
- **Problem Description:** Given a list of cities and the distances between each pair of cities, the problem is to find the shortest possible route that visits each city exactly once and returns to the origin city.
- **Techniques Used:** Classic problem in Combinatorial Optimization. Dynamic Programming, Genetic Algorithms, Simulated Annealing, 2-opt and 3-opt heuristics, Graph Theory, and Integer Linear Programming.

**2. Floyd-Warshall**
- **Problem Description:** Given a directed, weighted graph with positive or negative edge weights, the problem is to find the shortest paths between all pairs of vertices in the graph.
- **Techniques Used:** Classic problem in Graph Theory and is typically solved using dynamic programming. The Floyd-Warshall algorithm itself is a specific instance of dynamic programming. The key idea is to progressively improve an estimate of the shortest path between any two vertices by considering all possible intermediate vertices.

**3. Dijkstra's**
- **Problem Description:** Given a graph with non-negative weights and a source vertex, the problem is to find the shortest paths from the source to all other vertices in the graph.
- **Techniques Used:** Classic example of a Greedy Algorithm. The algorithm uses a priority Queue data structure to continuously select the Vertex with the smallest tentative distance to process next. It also makes use of the property of Relaxation, which ensures that if a path A→B→C is shorter than the known path A→C, it updates the shortest path to A→B→C.

**4. Topological Sort**
- **Problem Description:** Given a directed acyclic graph (DAG), the problem is to find a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.
- **Techniques Used:** Common problem in Graph Theory and is typically solved using Depth-First Search (DFS) or Breadth-First Search (BFS) with a Queue or Stack data structure to keep track of the ordering. The Kahn's algorithm and the DFS-based algorithm are two commonly used methods to solve this problem.

**5. Knapsack Problem**
- **Problem Description:** Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
- **Techniques Used:** Classic problem in Combinatorial Optimization. Dynamic programming is the most common technique used to solve it. Both the 0/1 version and the fractional version can be solved with variations of dynamic programming.

**6. Bellman-Ford Algorithm**
- **Problem Description:** Given a graph and a source vertex, find the shortest paths from the source vertex to all vertices in the graph. The graph may contain negative weight edges.
- **Techniques Used:** The Bellman-Ford algorithm is a single-source shortest-path algorithm. It uses dynamic programming to relax and update the shortest paths.

## Links
1. Coding Interviews [Resources](https://gist.github.com/HusseinLezzaik/8c72ae33caa9dcbeef884a2b79c0419f)
2. Design Patterns [Resources](https://gist.github.com/HusseinLezzaik/64c5760d12a8e97503787cd0d104986d)
3. Systems Design [Resources](https://gist.github.com/HusseinLezzaik/99cfa85b7f1667fd8b3c56021ebbc2c0)
4. Systems Design [Cheatsheet](https://gist.github.com/HusseinLezzaik/fa320c305e185c9099ffb8ac0e357323)
5. Data Structures and Algorithms [Resources](https://gist.github.com/HusseinLezzaik/8139feb0e4eee1ff5f0c8a04c12ac2be)
6. Minimal Python [Code](https://gist.github.com/HusseinLezzaik/7ef12c78a6c09c8726d2b7a3154f4d3b)
7. My Solution to Coding Problems [CodeFun](https://github.com/HusseinLezzaik/CodeFun)
8. MLOps [Resources](https://gist.github.com/HusseinLezzaik/178c5b628b472469475bb9d55de58230)
9. MLOps [Tools](https://gist.github.com/HusseinLezzaik/d925e919e9b9f9204c4974746c5ecfa8)
10. Machine Learning Interviews [Resources](https://gist.github.com/HusseinLezzaik/0d9874d618740a02942098d8884116ab)
11. Machine Learning [Fundamentals](https://gist.github.com/HusseinLezzaik/07eac29776005256402f43fb3b371820)
12. Hacker Culture [Resources](https://gist.github.com/HusseinLezzaik/6819e631bed667d27e466087035f55ef)
13. Machine Learning Interview [Structure](https://gist.github.com/HusseinLezzaik/1160164a01f3307c78fdbc371fd323ca)
14. Some [cheatsheets](https://github.com/HusseinLezzaik/random-cheatsheets/tree/main) for software/robotics/AI
