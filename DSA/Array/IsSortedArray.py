
def solve(nums):
    is_sorted = True

    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            is_sorted = False
            break

    return is_sorted

if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    print("Second Largest Element : ", solve(nums))

# Time  = O(N)
# Space = O(1)