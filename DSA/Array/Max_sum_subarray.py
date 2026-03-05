#Approach 1
def max_subarray(nums):
    curr_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(curr_sum, max_sum)

    return max_sum

# Time  : O(n)
# Space : O(1)

# Approach 2 : Kadane’s Algorithm

# If current sum becomes negative → reset to 0.

def maxSubArray(nums):
    max_sum = float('-inf')
    curr_sum = 0

    for num in nums:
        curr_sum += num
        max_sum = max(max_sum, curr_sum)

        if curr_sum < 0: # it reduces the further sum
            curr_sum = 0

    return max_sum

# Time = O(n)
# Space = O(1)

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(max_subarray(nums))




