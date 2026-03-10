def productExceptSelf(nums):
    n = len(nums)

    res = [1]*n

    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n-1,-1,-1):
        res[i] *= suffix
        suffix *= nums[i]

    return res

# Time = O(n)
# Space = O(n)

if __name__ == "__main__":
    nums = [1,2,3,4]
    print("output:", productExceptSelf(nums))