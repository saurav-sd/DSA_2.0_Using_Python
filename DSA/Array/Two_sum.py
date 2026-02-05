# nums = [2, 7, 11, 15]

# bruteforce approach using 2 loops 

# def two_sum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1,n):
#             if nums[i] + nums[j] == target:
#                 return [i,j]
#     return [-1,-1]

# Time = O(N)
# Space = O(1)

# Using map 

def two_sum(nums,target):
    mp = {}
    for i,num in enumerate(nums):
        rem = target - num
        if rem in mp:
            return [mp[rem],i]
        mp[num] = i
        


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 2
    print(two_sum(nums, target))

