def solve(nums):
    max_val = nums[0]
    count = 0

    for num in nums:
        if num > max_val:
            max_val = num

    for num in nums:
        if max_val == num:
            count += 1

    return count


if __name__ == "__main__":
    nums = [5,5,5]
    print("Number of time Max element present: ", solve(nums))

# time and space complexity
# Time  = O(n)
# Space = O(1)