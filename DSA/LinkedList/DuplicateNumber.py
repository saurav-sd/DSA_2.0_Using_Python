# Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

# Approach 1 : Bruteforce using 2 loops , time = O(n^2) and space = O(1)
# Approach 2 : by sorting the array, but it will modify the original array, Time = O(nlogn) , space = O(1)
# Approach 3 : using hashset , Time = O(n), Space = O(n)

# Approach 4 : Using linkedlist , Floyd’s Cycle Detection
"""
nums = [1,3,4,2,2]

Treat array like this:
index → value
0 → 1
1 → 3
2 → 4
3 → 2
4 → 2

0 → 1 → 3 → 2 → 4 → 2 → 4 → 2 ...
"""

def duplicateNumber(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


nums = [3, 1, 3, 4, 2]
print(duplicateNumber(nums))
