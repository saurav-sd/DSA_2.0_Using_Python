# How to make arrays in python ?
# array is not a builtin datatype in python.

from array import *

arr = array('i', [10,20,30])

# print(arr)

# for i in arr:
#     print(i)

# for i in range(3):
#     print(arr[i])

# i = 0
# while(i < len(arr)):
#     print(arr[i])
#     i+=1

# methods for array

arr.append(40)

print(arr)

# drawbacks of array
# allow only limited data types.
# 