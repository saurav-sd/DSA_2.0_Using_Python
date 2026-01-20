nums = [1, 2, 3, 4, 5, 6]

def split_list(lst, k):
    n = len(lst)
    k = k % n  # Handle cases where k is greater than n
    return lst[:k], lst[k:]

res = split_list(nums, 2)
print(res)