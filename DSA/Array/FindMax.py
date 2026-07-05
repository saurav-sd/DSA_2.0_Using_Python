def solve(nums):
    max_val = float("-inf")

    for num in nums:
        if num > max_val:
            max_val = num

    return max_val


if __name__ == "__main__":
    nums = [2,40, 23, 18, 15 ]
    print("Max element : ", solve(nums))

# time and space complexity
# Time  = O(n)
# Space = O(1)