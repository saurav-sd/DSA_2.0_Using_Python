from collections import Counter

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    
    s1_count = Counter(s1)
    window = Counter()

    for i in range(len(s2)):
        window[s2[i]] += 1

        if i >= len(s1):
            if window[s2[i-len(s1)]] == 1:
                del window[s2[i - len(s1)]]
            else:
                window[s2[i - len(s1)]] -= 1

        if window == s1_count:
            return True
        
    return False


#-------------------
s1 = "abc"
s2 = "eidbaooo"
output = checkInclusion(s1,s2)
print("is permutation : ", output)
