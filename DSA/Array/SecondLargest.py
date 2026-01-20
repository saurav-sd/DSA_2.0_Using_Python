# nums = [10, 5, 20, 8]

def solve(nums):
    largest = second_largest = float('-inf')

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest

if __name__ == "__main__":
    nums = [10, 5, 20, 8]
    print("Second Largest Element : ", solve(nums))


# Time complaxity : O(n)
# Space complaxity : O(1)