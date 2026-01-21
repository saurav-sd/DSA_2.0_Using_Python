def left_rotate(nums):
    first = nums[0]

    for i in range(1, len(nums)):
        nums[i - 1] = nums[i]

    nums[-1] = first
    return nums


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(left_rotate(nums))
