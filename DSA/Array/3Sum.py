# 3 sum 

# Approach 1 : Brute force - 3 loops

def threeSum1(nums):
    n  = len(nums)
    res = set()

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i]+nums[j]+nums[k] == 0:
                    res.add(tuple(sorted([nums[i],nums[j],nums[k]])))

    return res

# Time complaxity : O(n^3)
# Space complaxity : O(n)

# Approach 2 : Hashing (Better)

def threeSum2(nums):
    n = len(nums)
    res = set()

    for i in range(n):
        seen = set()
        for j in range(i+1,n):
            target = -(nums[i]+nums[j])
            if target in seen:
                res.add(tuple(sorted([nums[i], nums[j], target])))
            seen.add(nums[j])

    return list(res)

# Time complaxity : O(n^2)
# Space complaxity : O(n)

# Approach 3 : Optimal (Sort + Two Pointers)

def threeSum3(nums):
    nums.sort()
    res = []

    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue

        l, r = i+1, len(nums)-1

        while l < r:
            s = nums[i] + nums[l] + nums[r]

            if s == 0:
                res.append([nums[i],nums[l],nums[r]])
                l+=1
                r-=1

                while l<r and nums[l]==nums[l-1]:
                    l+=1
                while l<r and nums[r]==nums[r+1]:
                    r-=1

            elif s < 0:
                l+=1
            else:
                r-=1

    return res

# Time complaxity  = O(n^2)
# Space complaxity = O(1)

if "__main__" == __name__:
    nums = [-1,0,1,2,-1,-4]
    print("3 sum array : ", threeSum3(nums))
