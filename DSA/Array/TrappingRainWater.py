# Trapping Rain Water

# Approach 1:  Bruteforce 
def trap(height):
    n = len(height)
    water = 0

    for i in range(n):
        left_max = max(height[:i+1])
        right_max = max(height[i:])

        water += min(left_max, right_max) - height[i]

    return water

# Time = O(n^2)
# Space = O(1)

# ---------------------------------------------

# Approach 2 : Prefix array

def prefix_array(height):
    n = len(height)

    left = [0]*n
    right = [0]*n

    left[0] = height[0]
    for i in range(1,n):
        left[i] = max(left[i-1], height[i])

    right[n-1] = height[n-1]
    for i in range(n-2,-1,-1):
        right[i] = max(right[i+1], height[i])
    
    water = 0
    for i in range(n):
        water += min(left[i], right[i]) - height[i]

    return water

# Time = O(n)
# Space = O(2n)

# -----------------------------------

# Approach 3 : two pointer

def two_pointers(height):
    n = len(height)
    left = 0
    right = n-1

    left_max = 0
    right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]

            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]

            right -=1

    return water

# Time = O(n)
# Space = O(1)


# ==========================================================

if __name__ == "__main__":
    height = [4,2,0,3,2,5]
    print("output:", two_pointers(height))