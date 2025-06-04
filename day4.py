"""
Day 4 Debugging Problems

Easy: Array - Remove Even Numbers
Problem Statement:
Write a function that removes all even numbers from an array and returns the new array.
Bug: The function does not remove all even numbers correctly.
"""
def remove_evens(arr):
    # Buggy implementation
    return [x for x in arr if x % 2 == 1] #I think this implementation seems to work

    #standard implementation:
    oddArr = []
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            oddArr.append(arr[i])
    
    return oddArr

# Test cases
print(remove_evens([1, 2, 3, 4, 5, 6]))  # Expected: [1, 3, 5]
print(remove_evens([2, 4, 6]))           # Expected: []
print(remove_evens([1, 3, 5]))           # Expected: [1, 3, 5]
print(remove_evens([]))                  # Expected: []

# ------------------------------------------------------------------------

"""
Medium: Searching - Linear Search with Index
Problem Statement:
Write a function that returns the index of the first occurrence of a target in an array, or -1 if not found.
Bug: The function does not always return the correct index.
"""
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Test cases
print(linear_search([5, 3, 7, 1, 9], 7))   # Expected: 2
print(linear_search([1, 2, 3], 4))         # Expected: -1
print(linear_search([], 1))                # Expected: -1
print(linear_search([2, 2, 2], 2))         # Expected: 0

# ------------------------------------------------------------------------

"""
Hard: Linked List - Reverse a Linked List
Problem Statement:
Given the head of a singly linked list, reverse the list and return the new head.
Bug: The function does not reverse the list correctly.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# Helper to build and print linked list
def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

# Test cases
head1 = build_list([1, 2, 3, 4, 5])
print_list(reverse_list(head1))  # Expected: [5, 4, 3, 2, 1]
head2 = build_list([1])
print_list(reverse_list(head2))  # Expected: [1]
head3 = build_list([])
print_list(reverse_list(head3))  # Expected: []