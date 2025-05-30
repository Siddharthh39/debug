#easy
def square(num):
    return num * num
print(square(int("4"))) # change was to move str to int

# medium 
def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in s:
        if char in vowels: #need to change everything to lower case as the code only check            
            count += 1 # for lower cases so char.lower() 
    return count
    
print(count_vowels("Hello World"))
# no error
# hard
def unique_elements(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] not in result:
            result.append(lst[i])
        else:
            result.remove(lst[i])
    
    return result

print(unique_elements([1, 2, 2, 3, 4, 4, 5]))
## no error

#hard 
def longest_consecutive_subsequence(nums):
    nums.sort()
    max_len = 1
    curr_len = 1
    
    if len(nums) == 0: #fix
        return 0
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]: # fix
            continue

        if nums[i] == nums[i - 1] + 1:
            curr_len += 1
        else:
            curr_len = 1
        max_len = max(max_len, curr_len)
    return max_len

# Test cases
print(longest_consecutive_subsequence([100, 4, 200, 1, 3, 2]))  # Expected: 4
print(longest_consecutive_subsequence([1, 9, 3, 10, 4, 20, 2])) # Expected: 4
print(longest_consecutive_subsequence([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42])) # Expected: 5
print(longest_consecutive_subsequence([1, 2, 2, 3])) # Expected: 3 #wrong
print(longest_consecutive_subsequence([])) # Expected: 0 # wrong