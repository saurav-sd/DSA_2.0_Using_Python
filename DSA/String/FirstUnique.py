#  First Unique Character in a String

from collections import Counter

def firstUnique(s):
    count = Counter(s)

    # for char in s:
    #     count[char] = count.get(char,0) + 1

    # for char in s:
    #     if char in count:
    #         count[char] += 1
    #     else:
    #         count[char] = 1

    for i in range(len(s)):
        if count[s[i]] == 1:
            return i
        
    return -1

# Time = O(N)
# Space = O(N)



s = "leetcode"
print(firstUnique(s))