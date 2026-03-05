def leaders(nums):
    max_right = float('-inf')
    res = []

    for i in range(len(nums)-1,-1,-1):
        if nums[i] > max_right:
            res.append(nums[i])
            max_right = nums[i]
    return res[::-1]

if __name__ == "__main__":
    nums = [16,17,4,3,5,2]
    print("Leader : ", leaders(nums))
