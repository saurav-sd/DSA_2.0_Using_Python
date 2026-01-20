# for loop
# for i in range(0, 5,3):
#     print(i)


# while loop
# n = 1
# while n < 10:
#     print(n)
#     n = n+1

arr = [10, 20, 30, 40]

# By index
# for i in range(len(arr)):
#     print(i, arr[i])

# by element
# for val in arr:
#     print(val)

# nested loop
arr = [1,2,3]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        print(arr[i], arr[j])