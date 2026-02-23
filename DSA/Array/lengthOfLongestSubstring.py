def lengthOfLongestSubstring(str):
    char_set = set()
    left = 0
    max_len = 0

    for i in range(len(str)):
        while str[i] in char_set:
            char_set.remove(str[left])
            left += 1

        char_set.add(str[i])
        max_len = max(max_len, i-left+1)
    
    return max_len


if __name__ == "__main__":
    str = "abcabcbb"
    print("max lnght substring : ", lengthOfLongestSubstring(str))
