def jump(nums):
    max_reach = 0

    for i in range(len(nums)):
        # If our current position is beyond our max reach, we are stuck
        if i > max_reach:
            return False
        
        max_reach = max(max_reach, i+nums[i])

        # If we can already reach the end, stop early
        if max_reach >= len(nums):
            return True

    return True

# Time = O(n)
# Space = O(1)

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print("output : ", jump(nums))