def longestSubarray(arr, k):  
        prefix_sum = 0
        max_len = 0
        mp = {}
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            if prefix_sum == k:
                max_len = i+1
                
            if prefix_sum - k in mp:
                max_len = max(max_len,i-mp[prefix_sum-k])
                
            if prefix_sum not in mp:
                mp[prefix_sum] = i
                
        return max_len

if __name__ == "__main__":
    nums = [10, 5, 2, 7, 1, -10]
    k = 15
    print("Longest subarray with sum k : ", longestSubarray(nums, k))