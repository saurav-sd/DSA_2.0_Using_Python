# Variable-size Sliding Window

def longest_subarray(nums, k):
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > k:
            current_sum -= nums[left]
            left +=1

        max_length = max(max_length, right - left + 1)
    
    return max_length

if __name__ == "__main__":
    nums = [1,2,1,0,1,1,0]
    k = 4
    print(longest_subarray(nums, k))


# Time  = O(n)
# Space = O(1)