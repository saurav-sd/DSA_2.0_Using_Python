# Reverse a string 


# Approach 1: Using slicing 
# it is not the in place reversal but it is the most efficient way to reverse a string in Python.

def reverse_string(s):
    """
    Reverses the input string.

    Args:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    return s[::-1]

# Time Complexity: O(n) where n is the length of the string.
# Space Complexity: O(n) since we are creating a new string to hold the reversed version

# Approach 2: Using two pointers
# This approach is more efficient in terms of space complexity as it reverses the string in place

def reverse_string_in_place(s):
    """
    Reverses the input string in place.

    Args:
        s (str): The string to be reversed.
    Returns:
        str: The reversed string.
    """
    # Convert the string to a list since strings are immutable in Python
    char_array = list(s)
    left, right = 0, len(char_array) - 1

    while left < right:
        # Swap the characters at left and right pointers
        char_array[left], char_array[right] = char_array[right], char_array[left]
        left += 1
        right -= 1

    # Convert the list back to a string
    return ''.join(char_array)

# Time Complexity: O(n) where n is the length of the string.
# Space Complexity: O(1) for the in-place approach (ignoring the space used for the input string).

# Example usage:
input_string = "Hello, World!"  
reversed_string = reverse_string(input_string)
print(reversed_string)  # Output: !dlroW ,olleH