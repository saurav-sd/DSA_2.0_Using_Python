def jump(nums):
    jump = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums)-1):
        farthest = max(farthest, i+nums[i])

        if i == current_end:
            jump += 1
            current_end = farthest

    return jump

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print("output : ", jump(nums))
