def maxSumSubarray(nums, k):
    window_sum = 0
    max_sum = float('-inf')
    left = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        if right - left + 1 == k:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[left]
            left += 1

    return max_sum

if "__name__" == "__main__":
    nums = [1,2,3,4,5,6]
    print("Max sum : ", maxSumSubarray(nums))