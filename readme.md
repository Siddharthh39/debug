# Python Debugging Practice

This repository is dedicated to improving Python debugging skills through daily problem-solving. Each day, a set of debugging problems (easy, medium, hard) is solved, with a focus on understanding error messages, fixing bugs, and writing robust code.

---

## Daily Improvement Chart

| Day   | Easy Problem         | Medium Problem           | Hard Problem(s)                        | Concepts Practiced                | Self-Solved | AI Helped | Notes/Progress                          |
|-------|----------------------|--------------------------|-----------------------------------------|------------------------------------|-------------|-----------|------------------------------------------|
| Day 1 | ✅ Square Function   | ✅ Count Vowels          | ✅ Unique Elements, ✅ Longest Consecutive Subsequence | Functions, Strings, Lists, Sets   | 2/4         | 2/4      | Needed help with hard problems           |
| Day 2 | ✅ HashMap Counter   | ✅ Balanced Parentheses   | ✅ Remove Duplicates (LL)                | Dict, Stack, Linked List           | 2/3         | 1/3      | Needed help with linked list pointers    |
| Day 3 |                      |                          |                                         |                                    |             |           |                                          |
| ...   |                      |                          |                                         |                                    |             |           |                                          |

- ✅ = Solved and understood
- ❌ = Needs review

---

## Problems Solved

### Day 1

#### Easy: Square of a Number
**Problem Statement:**  
Write a function that returns the square of a given number.  
**Bug:** The function was called with a string instead of an integer.  
**Result:** Fixed by self.

#### Medium: Count Vowels in a String
**Problem Statement:**  
Write a function that counts the number of vowels in a string (case-insensitive).  
**Bug:** The function only checked for lowercase vowels, missing uppercase vowels.  
**Result:** Fixed by self.

#### Hard: Unique Elements in a List
**Problem Statement:**  
Write a function that returns a list of unique elements from the input list, preserving the original order (first occurrence only).  
**Bug:** The function incorrectly removed elements that appeared more than once, instead of just skipping duplicates.  
**Result:** Fixed with AI help.

#### Hard: Longest Consecutive Subsequence
**Problem Statement:**  
Write a function that returns the length of the longest subsequence of consecutive integers in an unsorted list. The subsequence does not need to be contiguous in the original list.  
**Bug:** The function did not handle duplicates and empty lists correctly.  
**Result:** Fixed with AI help.

---

### Day 2

#### Easy: HashMap (Dictionary) Value Counter
**Problem Statement:**  
Write a function that counts the frequency of each element in an array and returns a dictionary.  
**Bug:** The function did not count correctly for repeated elements.  
**Result:** Fixed by self.

#### Medium: Stack - Balanced Parentheses
**Problem Statement:**  
Write a function that checks if a string of parentheses is balanced using a stack.  
**Bug:** The function returned True for some unbalanced strings.  
**Result:** Fixed by self.

#### Hard: Linked List - Remove Duplicates (Sorted List)
**Problem Statement:**  
Given the head of a sorted linked list, remove all duplicates such that each element appears only once. Return the head of the updated list.  
**Bug:** The function did not remove all duplicates.  
**Result:** Fixed with AI help.

---

## How to Use

- Review the problems and their statements.
- Check the corresponding solutions and explanations in `day1.py`, `day2.py`, etc.
- Use the test cases to verify your own fixes and understanding.

---

*More problems and solutions will be added daily as the debugging journey continues!*