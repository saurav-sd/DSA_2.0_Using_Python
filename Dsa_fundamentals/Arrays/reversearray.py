arr = [1,2,3,4,5,6]

for i in range(len(arr)//2):
    arr[i], arr[len(arr)-1] = arr[len(arr)-1],arr[i]

print(arr)