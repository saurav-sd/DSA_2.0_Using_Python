def LargestSubarrayWithSum0(nums):
    n = len(nums)
    prefix_sum = 0
    max_len = 0
    mp = {}

    for i in range(n):
        prefix_sum += nums[i]

        if prefix_sum == 0:
            max_len += 1

        if prefix_sum in mp:
            max_len = max(max_len, i - mp[prefix_sum])
        else:
            mp[prefix_sum] = i

    return max_len

if "__main__" == __name__:
    nums = [15, -2, 2, -8, 1, 7, 10, 23]
    print("Largest subarray with 0 sum : ", LargestSubarrayWithSum0(nums))