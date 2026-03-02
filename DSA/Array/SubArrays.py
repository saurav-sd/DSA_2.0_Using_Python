# Bruteforce approach to print all subarrays of an array

def solve(nums):
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n+1):
            print(nums[i:j], end=" ")
    print()
    

if __name__ == "__main__":
    nums = [10, 5, 20, 8]
    print("All subarray : ", solve(nums))


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

#=============================================#

#  Subarray Sum Equals K

# Approach 1 : Brute force

def subarraySumK(nums, k):
    n = len(nums)
    sub_sum = 0
    count = 0

    for i in range(n):
        for j in range(i+1, n+1):
            sub_sum = sum(nums[i:j])
            if sub_sum == k:
                count += 1

    return count

# Time  = O(n^2)
# Space = O(1)

# Approach 2 : Optimal: Prefix Sum + HashMap

# current_sum - k = some previous prefix sum

def subarraySum(nums, k):
    prefix_sum = 0
    count = 0
    mp = {0:1}

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in mp:
            count += mp[prefix_sum - k]

        mp[prefix_sum] = mp.get(prefix_sum,0) + 1

    return count


if  "__main__" == __name__:
    nums = [1,2,3]
    k = 3
    print("Sum of an subarray equals to k : ", subarraySumK(nums, k))


# Using xor 

def subarrayXor(nums, k):
    prefix_sum = 0
    count = 0
    mp = {0:1}

    for num in nums:
        prefix_sum ^= num

        if prefix_sum ^ k in mp:
            count += mp[prefix_sum^k]

        mp[prefix_sum] = mp.get(prefix_sum,0)+1

    return count

if  "__main__" == __name__:
    nums = [4, 2, 2, 6, 4]
    k = 6
    print("Sum of an subarray equals to k with xor: ", subarrayXor(nums, k))