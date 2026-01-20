def reverse(nums):
    i = 0
    j = len(nums)-1
    while i<j:
        nums[i], nums[j] = nums[j],nums[i] 
        i+=1
        j-=1
    return nums

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    print("rversed array: ", reverse(nums))
