nums = [1, 2, 3, 4]

def rotate_list(lst, k):
    n = len(lst)
    k = k % n  # Handle cases where k is greater than n
    return lst[-k:] + lst[:-k]

res = rotate_list(nums, 2)
print(res)

# time complexity: O(n) 
# space complexity: O(n) for the new list created by slicing
# Note: The space complexity is O(n) because a new list is created.

# in place rotation
def reverse(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

def rotate_list_in_place(lst, k):
    n = len(lst)
    k = k % n  # Handle cases where k is greater than n
    reverse(lst, 0, n - 1)
    reverse(lst, 0, k - 1)
    reverse(lst, k, n - 1)

rotate_list_in_place(nums, 2)
print(nums)
