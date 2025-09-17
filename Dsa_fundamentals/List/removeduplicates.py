nums = [1, 2, 2, 3, 4, 4]

# new_list = []

# for num in nums:
#     if num not in new_list:
#         new_list.append(num)

# print(new_list)

# time complexity: O(n^2)
# space complexity: O(n)

# give me optimized code
new_list = list(set(nums))
print(new_list)

# time complexity: O(n)
# space complexity: O(n)