def move_zeroes(nums):
    j = 0  # index for non-zero elements

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1

    return nums


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print(move_zeroes(nums))
