# Bruteforce approach to print all subarrays of an array

# def solve(nums):
#     n = len(nums)

#     for i in range(n):
#         for j in range(i+1, n+1):
#             print(nums[i:j], end=" ")
#     print()
    

# if __name__ == "__main__":
#     nums = [10, 5, 20, 8]
#     print("All subarray : ", solve(nums))


# Time complaxity : O(n^2)
# Space complaxity : O(1)

# Using sliding window we can optimize space complaxity to O(k) where k is size of subarray

def solve(nums,k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == "__main__":
    nums = [2,1,5,1,3,2]
    k = 3
    print("Max sum of an subarray of size k : ", solve(nums, k))

# Time complaxity : O(n)
# Space complaxity : O(1)