# Algorithm
# Steps
# Traverse from right → find first decreasing index i
# Find element just greater than nums[i]
# Swap them
# Reverse right portion

def nextPermutation(nums):
    i = len(nums)-2 # first decresing index

    while i>=0 and nums[i]>=nums[i+1]:
        i -=1
    
    if i>=0:
        j = len(nums)-1
        while nums[j]<=nums[i]:
            j -=1
        nums[i],nums[j] = nums[j],nums[i]

    nums[i+1:] = reversed(nums[i+1:])

    return nums

    

if "__main__" == __name__:
    nums = [1,3,2]
    print("Next permutation : ", nextPermutation(nums))

# Time  = O(n)
# Space = O(1)