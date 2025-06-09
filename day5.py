"""
Day 5 Debugging Problems

Easy: Array - Find Second Largest Element
Problem Statement:
Write a function that returns the second largest element in an array.
Bug: The function does not handle arrays with duplicate values or arrays with fewer than two elements correctly.
"""
def find_second_largest(arr):
    if len(arr) < 2:
        return None
    
    if len(set(arr)) < 2:
        return None
        
    largest = float('-inf')
    second_largest = float("-inf")
    
    for num in arr:
        
        if num > largest:
            second_largest = largest
            largest = num
        
        if num > second_largest and num < largest:
            second_largest = num
    
    return second_largest
# Test cases
print(find_second_largest([1, 2, 3, 4, 5]))  # Expected: 4
print(find_second_largest([5, 5, 5]))        # Expected: None
print(find_second_largest([1]))              # Expected: None
print(find_second_largest([]))               # Expected: None
print(find_second_largest([-1, -2, -3, -4])) # Expected: -2
print(find_second_largest([1, -2, 3, -4, 5])) # Expected: 3
print(find_second_largest([5, 5, 4, 4, 3]))  # Expected: 4

# ------------------------------------------------------------------------

"""
Medium: Stack - Implement Min Stack
Problem Statement:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Bug: The function does not always return the correct minimum element after pop operations.
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()
        return None

    def top(self):
        return self.stack[-1] if self.stack else None

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

# Test cases
min_stack = MinStack()
min_stack.push(5)
min_stack.push(3)
min_stack.push(7)
print(min_stack.get_min())  # Expected: 3
min_stack.pop()
print(min_stack.get_min())  # Expected: 3
min_stack.pop()
print(min_stack.get_min())  # Expected: 5

# ------------------------------------------------------------------------

"""
Hard: Sorting - Merge Intervals
Problem Statement:
Given a list of intervals, merge all overlapping intervals and return the result.
Bug: The function does not handle edge cases like intervals that are already sorted or intervals with no overlap correctly.
"""
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if merged[-1][1] >= intervals[i][0]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
    return merged

# Test cases
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Expected: [[1, 6], [8, 10], [15, 18]]
print(merge_intervals([[1, 4], [4, 5]]))                    # Expected: [[1, 5]]
print(merge_intervals([]))                                  # Expected: []
print(merge_intervals([[1, 2]]))                            # Expected: [[1, 2]]