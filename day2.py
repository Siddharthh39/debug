# """
# Easy: HashMap (Dictionary) Value Counter
# Problem Statement:
# Write a function that counts the frequency of each element in an array and returns a dictionary.
# Bug: The function does not count correctly for repeated elements.
# """
# def count_frequencies(arr):
#     freq = {}
#     for num in arr:
#         if num not in freq:
#             freq[num] = 1
        
#         else:
#             freq[num] += 1
            
#     return freq

# # Test cases
# print(count_frequencies([1, 2, 2, 3, 2, 1]))  # Expected: {1: 2, 2: 2, 3: 1}
# print(count_frequencies([]))               # Expected: {}

# ----------------------------------------------------------------------------------------------------------------
# """
# Medium: Stack - Balanced Parentheses
# Problem Statement:
# Write a function that checks if a string of parentheses is balanced using a stack.
# Bug: The function returns True for some unbalanced strings.
# """
# def is_balanced(s):
#     stack = []
#     for char in s:
#         if char == '(':
#             stack.append(char)
        
#         elif len(stack) == 0 and char == ")":
#             return False
        
#         elif char == ')':
#             stack.pop()
        
        
#     return len(stack) == 0

# # Test cases
# print(is_balanced("()()"))      # Expected: True
# print(is_balanced("((())())"))  # Expected: True
# print(is_balanced("(()"))       # Expected: False
# print(is_balanced("())("))      # Expected: False
# ----------------------------------------------------------------------------------------------------------------
"""
Hard: Linked List - Remove Duplicates (Sorted List)
Problem Statement:
Given the head of a sorted linked list, remove all duplicates such that each element appears only once. Return the head of the updated list.
Bug: The function does not remove all duplicates.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        
        else:
            curr = curr.next

    return head

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
head1 = build_list([1, 1, 2, 3, 3])
print_list(remove_duplicates(head1))  # Expected: [1, 2, 3]
head2 = build_list([1, 1, 1, 1])
print_list(remove_duplicates(head2))  # Expected: [1]