def solve(nums):
    max_val = nums[0]

    for num in nums:
        if num > max_val:
            max_val = num

    return max_val


if __name__ == "__main__":
    nums = [1,3,2,46,4,]
    print("Max element : ", solve(nums))

# time and space complexity
# Time  = O(n)
# Space = O(1)