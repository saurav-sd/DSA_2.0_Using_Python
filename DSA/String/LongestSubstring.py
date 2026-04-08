# Longest Substring Without Repeating Characters
# Pattern : variable sliding window

def longestSubstring(s):
    left = 0
    max_len = 0
    char_set = set()
    start_idx = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])

        # Only update if we found a strictly LONGER substring
        if (right - left + 1) > max_len:
            max_len = right - left + 1
            start_idx = left  # Capture the current left pointer

        # Use slicing to get the actual substring from the original string
        actual_substring = s[start_idx : start_idx + max_len]

    return {"longest_substring" : actual_substring, "length" : max_len}

s = "abcabcbb"
lengthOfLongestSubstring = longestSubstring(s)
print("output : ", lengthOfLongestSubstring)

# Time complaxity = O(n)


