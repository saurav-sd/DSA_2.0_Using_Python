def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if(arr[j] < arr[min_index]):
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]


arr = [10,15,9,20,7,6,21,4]
selection_sort(arr)
print(arr)
