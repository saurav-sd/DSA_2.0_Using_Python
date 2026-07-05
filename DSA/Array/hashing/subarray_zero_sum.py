# subarray with zero sum with hashing 
# for java hastmap in python what is similar to hashmap in python is dictionary and for set in java is set in python
# what is dict in python is a data structure that stores key-value pairs. It is similar to a hashmap in Java. In this code, we are using a dictionary to keep track of the cumulative sums of the elements in the array. If we encounter a cumulative sum that we have seen before, it means that there is a subarray with a sum of zero.

def zeroSum(arr):
    dict = {}
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum == 0 or sum in dict:
            return True
        dict[sum] = i
    return False

# count the subarrays with zero sum with hashing
def countZeroSum(arr):
    dict = {}
    sum = 0
    count = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum == 0:
            count += 1
        if sum in dict:
            count += dict[sum]
        dict[sum] = dict.get(sum, 0) + 1
    return count