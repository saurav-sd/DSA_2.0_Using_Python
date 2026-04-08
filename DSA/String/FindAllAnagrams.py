# Find all anagrams in a string

from collections import Counter

def findAmagrams(s, p):
    res = []
    p_count = Counter(p)
    window = Counter()

    for i in range(len(s)):
        window[s[i]] += 1

        if i >= len(p):
            if window[s[i - len(p)]] == 1:
                del window[s[i - len(p)]]
            else:
                window[s[i - len(p)]] -= 1
        
        if window == p_count:
            res.append(i - len(p) + 1)

    return res

s = "cbaebabacd"
p = "abc"

print("Anagrams in the string : ", findAmagrams(s,p))