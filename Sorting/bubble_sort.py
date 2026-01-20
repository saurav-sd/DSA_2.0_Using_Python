# Bubble sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]

# Modified Bubble Sort
def modified_bubble_sort(arr):
    swapped = False
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break


arr = [64, 25, 12, 22, 11]
# bubble_sort(arr)
modified_bubble_sort(arr)
print("Sorted array:", arr)

