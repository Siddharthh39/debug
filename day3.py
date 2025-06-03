"""
Day 3 Debugging Problems

Easy: Array - Find Maximum Element
Problem Statement:
Write a function that returns the maximum element in an array.
Bug: The function does not handle empty arrays or negative numbers correctly.
"""
def find_max(arr):
    max_val = None
    
    if len(arr) == 0:
        return None

    for num in arr:
        if max_val is None:
            max_val = num

        elif num > max_val:
            max_val = num
    
    return max_val


# Test cases
print(find_max([1, 2, 3, 4, 5]))      # Expected: 5
print(find_max([-1, -2, -3, -4]))     # Expected: -1
print(find_max([]))                   # Expected: None

------------------------------------------------------------------------

"""
Medium: Queue - Implement with Two Stacks
Problem Statement:
Implement a queue using two stacks with enqueue and dequeue operations.
Bug: The dequeue operation does not always return the correct element.
"""
class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x):
        self.stack_in.append(x)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
       
        if self.stack_out:
            return self.stack_out.pop()
        return None

# Test cases
q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Expected: 1
print(q.dequeue())  # Expected: 2
q.enqueue(4)
print(q.dequeue())  # Expected: 3
print(q.dequeue())  # Expected: 4
print(q.dequeue())  # Expected: None

# ------------------------------------------------------------------------

"""
Hard: Binary Search - Find First Occurrence
Problem Statement:
Given a sorted array and a target value, return the index of the first occurrence of the target. If not found, return -1.
Bug: The function does not always return the first occurrence.
"""
def binary_search_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
   
    while left <= right:
        mid = (left + right) // 2
       
        if arr[mid] == target:
            result = mid
            right = mid - 1
       
        elif arr[mid] < target:
            left = mid + 1
       
        else:
            right = mid - 1
    
    return result

# Test cases
print(binary_search_first([1, 2, 2, 2, 3, 4], 2))  # Expected: 1
print(binary_search_first([1, 1, 1, 1], 1))        # Expected: 0
print(binary_search_first([1, 2, 3, 4], 5))        # Expected: -1