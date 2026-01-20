numbers = [1, 2, 3, 4]

reversed_numbers = numbers[::-1]
# print(reversed_numbers)  # Output: [4, 3, 2, 1]

# how this works:
# The slice notation [::-1] creates a new list that is a reversed version of the original list. 

# The first colon (:) indicates that we want to include all elements, and the -1 indicates that we want to step backwards through the list.
# This is a concise and efficient way to reverse a list in Python.
# It creates a new list that contains the elements of the original list in reverse order.
# Note that this does not modify the original list; it creates a new reversed list.

# If you want to reverse the list in place, you can use the reverse() method:
# numbers.reverse()
# print(numbers)  # Output: [4, 3, 2, 1]

# The reverse() method modifies the original list in place, reversing its elements without creating a new list.
# This is useful when you want to reverse a list without needing to create a new one.

# give me a code to reverse a list without using in built functions or methods


# solution1 
# def reverse_list(arr):
#     i = 0
#     j = len(arr) - 1
#     while i < j:
#         temp = arr[i]
#         arr[i] = arr[j]
#         arr[j] = temp
#         i += 1
#         j -= 1
#     return arr

# rev = reverse_list(numbers)
# print(rev)

# solution2

# def reverse_list(list):
#     rev_list = []
#     for i in range(len(list)-1, -1, -1):
#         rev_list.append(list[i])
        
#     return rev_list

# rev = reverse_list(numbers)
# print(rev)  # Output: [4, 3, 2, 1]

#solution3
def reverse_list(list):
    n = len(list)

    for i in range(n // 2):
        list[i], list[n-i-1] = list[n-i-1],list[i]

    return list

rev_list = reverse_list(numbers)

print(rev_list)

