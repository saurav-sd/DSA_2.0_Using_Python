# Length of last word


# Approach 1 : using split
# .split() without arguments splits by any whitespace 
# and removes leading/trailing spaces automatically.

def lengthOfLastWord(s):
    words = s.split()

    if not words:
        return 0

    return len(words[-1])

# Approach 2 : using two pointer

def lengthOfLastWord_2(s):
    length = 0
    r = len(s)-1

    while r >= 0 and s[r] == " ":
        r -= 1

    while r >= 0 and s[r] != " ":
        length += 1
        r -= 1
    
    return length
        

# --------------------------------------------

s = "  Hello World  "
print(lengthOfLastWord_2(s))