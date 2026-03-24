# Reverse Words

# Approach 1 : using split

def reverseWords(s):
    words = s.split()
    reverse = words[::-1]

    return " ".join(reverse)

# -------------------------------------------

def reverseWords_1(s):
    words = []
    word = ""

    for char in s:
        if char != " ":
            word += char
        else:
            if word:
                words.append(word)
                word = ""

    if word:
        words.append(word)

    return " ".join(words[::-1]) # reverses the order of words in a list and combines them back into a single string, separated by a space.

# Time = O(N)
# Space = O(N)

# -----------------------------------------------

s = "the sky is blue "
print(reverseWords_1(s))