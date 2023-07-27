"""
Outline of how Heap Sort works:

1. Build a Max Heap from the input data. In a Max Heap, the parent node is always larger than or equal to its child nodes. The largest element is at the root of the heap.
2. Swap the root (maximum value) of the Max Heap with the last element of the Heap. This puts the maximum value in its correct position in the sorted array.
3. Reduce the size of the Heap by 1. The last element has been sorted, so it's no longer part of the heap.
4. Heapify the root of the tree. This ensures that the root of the heap is the largest element.
5. Repeat steps 2, 3, and 4 until the size of the heap is 1.

The time complexity of Heap Sort is O(nlogn) in all cases (worst, average, and best) because heapify, which is O(logn), is called n times.

The space complexity is O(1) because Heap Sort is an in-place sorting algorithm and does not use extra space for sorting.
However, due to the recursive nature of heapify, the algorithm is not strictly in-place - the space for the recursive function call stack is O(logn) in the worst case (when the binary tree is perfectly balanced).

"""

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
