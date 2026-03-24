# Longest Common Prefix

def longestCommonPrefix(strs):
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    
    for i in range(len(strs[0])):
        for s in strs:
            if i >= len(s) or s[i] != strs[0][i]:
                return strs[0][:i]

    return strs[0] 


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))

# Time = O(n^2)
# Space = O(1)