def solve(nums):
    min_val = nums[0]

    for num in nums:
        if num < min_val:
            min_val = num

    return min_val


if __name__ == "__main__":
    nums = [1,3,2,46,4,]
    print("Min element : ", solve(nums))

# time and space complexity
# Time  = O(n)
# Space = O(1)