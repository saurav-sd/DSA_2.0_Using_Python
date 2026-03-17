# First Missing Positive


def firstMissingPositive1(nums):
    nums.sort()

    for i in range(len(nums)-1):
        if nums[i] <= 0:
            continue
        if nums[i] != nums[i+1]-1:
            return nums[i]+1
        
    return len(nums)

# Time  = O(nlogn)
# Space = O(1)

# Approach 2 : using Hashset

def firstMissingPositive2(nums):
    nums_set = set(nums)

    target = 1

    while target in nums_set:
        target += 1

    return target



if __name__ == "__main__":
    nums = [3,4,-1,1]
    print("Output : ", firstMissingPositive2(nums))