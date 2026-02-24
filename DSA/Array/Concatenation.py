# Approach 1 
def getConcatenation1(nums):
    return nums + nums


# Approach 2
def getConcatenation2(nums):
    n = len(nums)
    ans = [0] * (2*n)

    for i in range(n):
        ans[i] = nums[i]
        ans[i+n] = nums[i]

    return ans

# Approach 3 
def getConcatenation3(nums):
    res = []
    res.extend(nums)
    res.extend(nums)

    return res

# Time Complexity: $O(n)$ — We visit each element once.
# Space Complexity: $O(n)$ — We create a new array of size $2n$.


if "__main__" == __name__:
    nums = [1,2,3]
    print("Concatenated array : ", getConcatenation3(nums))