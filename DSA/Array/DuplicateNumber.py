# Find the Duplicate Number

# Approach 1 : Bruteforce

def findDuplicate1(nums):
    n = len(nums)

    for i in range(n):
        for j in range(i+1,n):
            if nums[i] == nums[j]:
                return nums[i]
            
# Time = O(n^2)
# Space = O(1)

# Approach 2 : Hashset

def findDuplicate2(nums):
    seen = set() # extra space

    for num in nums:
        if num in seen:
            return num
        seen.add(num)

# Time = O(N)
# Space = O(N)

# Approach 3: Sorting

def findDuplicate3(nums):
    nums.sort()

    for i in range(len(nums)):
        if nums[i] == nums[i+1]:
            return nums[i]

# Time = O(n log n)
# Space = O(1)
        
# Approach 4 : Floyd’s Cycle Detection (Optimal)

def findDuplicate4(nums):
    slow = nums[0]
    fast = nums[0]

    #dectect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
        

if __name__ == "__main__":
    nums = [0,1,0,4,2]
    print("Output : ", findDuplicate3(nums))

