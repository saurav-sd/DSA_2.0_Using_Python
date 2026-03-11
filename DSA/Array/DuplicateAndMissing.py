# Find Missing And Repeating numbers from Array

# Approach 1 : Hashmap

def findErrorNumbers(nums):
    n = len(nums)
    counts = {}
    
    # Fill the frequency map
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        
    repeating = -1
    missing = -1
    
    # Check every number from 1 to n
    for i in range(1, n + 1):
        if i not in counts:
            missing = i
        elif counts[i] == 2:
            repeating = i
            
        # Optimization: break early if both are found
        if repeating != -1 and missing != -1:
            break
            
    return {"repeating": repeating, "missing": missing}

# Time = O(n)
# Space = O(n)

# Approach 2 : Using Hashset

def find_missing_and_repeating(nums):
    n = len(nums)
    seen = set()
    repeating = -1
    missing = -1
    
    # 1. Identify the repeating number
    for num in nums:
        if num in seen:
            repeating = num
        else:
            seen.add(num)
            
    # 2. Identify the missing number by checking the range 1 to n
    for i in range(1, n + 1):
        if i not in seen:
            missing = i
            break
            
    return {"repeating": repeating, "missing": missing}


# Approach 3 : Cyclic Sort Pattern

# nums[i] should be at nums[nums[i]-1]

def findErrorNums(nums):

    i = 0
    n = len(nums)

    while i < n:
        correct = nums[i] - 1

        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return [nums[i], i+1]

if __name__ == "__main__":
    nums = [3,1,3]
    print("Repearing and Missing : ", findErrorNumbers(nums))


