def palindrome_number(num):
    dup = num
    rev = 0

    while num > 0:
        d = num % 10
        rev = rev * 10 + d
        num = num//10

    if rev == dup:
        return True
    else:
        return False
    

num = 121
print(palindrome_number(num))