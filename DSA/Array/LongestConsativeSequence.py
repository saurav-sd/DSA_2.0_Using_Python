def longestConsative(nums):
    s = set(nums)
    longest = 0

    for num in s:
        if num-1 not in s:
            curr = num
            length = 1

            while curr+1 in s:
                curr += 1
                length +=1

            longest = max(longest,length)
    return longest

if "__main__" == __name__:
    nums = [100,4,200,1,3,2]
    print("Longest consative sequence : ", longestConsative(nums))

# Time  = O(n) 
# Space = O(n)