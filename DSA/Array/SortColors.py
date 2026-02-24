def sortColors(nums):
    n = len(nums)
    low,mid,high = 0,0,n-1

    while mid <= high:
        if nums[mid] == 0:
            nums[low],nums[mid] = nums[mid],nums[low]
            low +=1
            mid +=1

        elif nums[mid] == 1:
            mid +=1
        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high -=1

    return nums

if "__main__" == __name__:
    nums = [2,0,2,1,1,0]
    print("Sorted Color : ", sortColors(nums))

# Time  = O(n)
# Space  = O(1)