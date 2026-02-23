# Container With Most Water

# Formula : Area = min(height[i], height[j]) * (j-i)

# Approach 1 : Brute Force
def maxArea1(height):
    n = len(height)
    max_area = 0

    for i in range(n):
        for j in range(i+1, n):
            area = min(height[i], height[j]) * (j-i)
            max_area = max(area, max_area)

    return max_area

# Time Complexity : O(n^2)
# Space Complexity : O(1)

# Approach 2 : Two Pointer
def maxArea2(height):
    n = len(height)
    l,r = 0,n-1
    max_area = 0

    while l < r:
        area = min(height[l], height[r]) * (r-l)
        max_area = max(area, max_area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area


if "__main__" == __name__:
    height = [1,8,6,2,5,4,8,3,7]
    print("Max area : ", maxArea2(height))

# Time complaxity : O(n)
# Space complaxity : O(1)


