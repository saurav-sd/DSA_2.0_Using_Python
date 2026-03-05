# Makority element n/2

# Approach 1 : using hashmap

def majority_element(nums):
    count = {}
    n = len(nums)

    for num in nums:
        count[num] = count.get(num, 0) + 1

        if count[num] > n//2:
            return num

# Time  = O(n)
# Space = O(n)

# Approach 2 : Moore’s Voting Algorithm

def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -=1

    return candidate
        

# Time  = O(n)
# Space = O(1)


if "__main__" == __name__:
    nums = [3,2,3]
    print("Majority element n/2 : ", majorityElement(nums))




