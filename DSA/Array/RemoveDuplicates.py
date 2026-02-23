# Remove Duplicates from Sorted Array

# Approach : 2 pointer

def removeDuplicates(nums):
    if not nums:
        return 0
    
    slow = 0
    for fast in range(1,len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]

    return slow+1

if "__main__" == __name__:
    nums = [0,0,1,1,1,2,2,3,3,4]
    print("solution : ", removeDuplicates(nums))