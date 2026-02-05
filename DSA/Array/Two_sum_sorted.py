def two_sum_sorted(nums, target):
    left = 0
    right = len(nums)-1

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left,right]
        elif sum < target:
            left += 1
        else:
            right -= 1


if __name__ == "__main__":
    nums = [-1,0]
    target = -1
    print(two_sum_sorted(nums, target))