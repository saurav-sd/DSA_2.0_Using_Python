def checkPalindrome(n):
    if n < 0:
        return False
    
    orig_no = n
    rev = 0
    while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n = n // 10
    
    return orig_no == rev


print("Check Palindrome : ", checkPalindrome(-121))

# Time = O(log n)
# Space = O(1)