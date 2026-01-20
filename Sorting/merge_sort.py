def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half,right_half)

def merge(left, rigt):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(rigt):
        if left[i] < rigt[j]:
            sorted_arr.append(left[i])
            i+=1
        else:
            sorted_arr.append(rigt[j])
            j+=1
    
    sorted_arr.extend(left[i:])
    sorted_arr.extend(rigt[j:])

    return sorted_arr


arr = [5, 3, 8, 6, 2]
sorted_arr = merge_sort(arr)
print(sorted_arr)