# Approach 1: Using slicing
def palindrome(s):
    return s == s[::-1]

# Time Complexity: O(n) where n is the length of the string.
# Space Complexity: O(n) since we are creating a new string to hold the reversed version

# Approach 2 : Using Two Pointer

def palindrome_twoPointer(s):
    l , r = 0, len(s)-1

    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

    return True 

# Time  = O(N)
# Space = O(1)

# ==================================

# Example usage:
input_string = "A man a plan a canal Panama"
# Remove spaces and convert to lowercase for accurate palindrome checking
input_string = input_string.replace(" ", "").lower()
is_palindrome = palindrome(input_string)
print(is_palindrome)  # Output: True