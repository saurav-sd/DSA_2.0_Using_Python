# list = [1, 10, 121, 5 , 14, 100, 200, 3, 8, 99]

# largest = list[0]

# for num in list:
#     if num > largest:
#         largest = num

# print(largest)

nums = [10, 20, 40, 30]

# approach 1
second_largest = sorted(nums)[-2]
print(second_largest)

# approach 2
largest = nums[0]
second_largest = float('-inf')

for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest:
        second_largest = num

print(second_largest)

# time complexity: O(n log n) for sorting, O(n) for the second approach
# space complexity: O(n) for the sorted approach, O(1) for the second approach
