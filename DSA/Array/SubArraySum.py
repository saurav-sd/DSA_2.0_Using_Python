# Count number of subarrays whose sum equals k.

def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0
    mp = {0:1}

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in mp:
            count += mp[prefix_sum - k]

        mp[prefix_sum] = mp.get(prefix_sum,0)+1

    return count

if __name__ == "__main__":
    nums = [1,2,3]
    k = 3
    print(subarray_sum(nums,k))