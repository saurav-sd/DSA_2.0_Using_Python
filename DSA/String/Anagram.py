# Approach 1 : using Hashmap

from collections import Counter

# Counter : Counter is a specialized dictionary for frequencies

def isAnagram(str1, str2):
    if len(str1) !=  len(str2):
        return False
    
    return Counter(str1) == Counter(str2)

# -------------------------------------------------------

def isAnagram(str1, str2):
    if len(str1) !=  len(str2):
        return False
    
    count = [0]*26
    
    for i in range(len(str1)):
        count[ord(str1(i)) - ord('a')] += 1
        count[ord(str2(i)) - ord('a')] -= 1

    for val in count:
        if val != 0:
            return False
    return True



# =========================================================

str1 = "anagram", str2 = "nagaram"
print(isAnagram(str1, str2))
