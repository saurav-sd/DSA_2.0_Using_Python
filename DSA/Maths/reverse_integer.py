def reverseInteger(n):
    sign = -1 if x < 0 else 1
    x = abs(x)

    res = 0

    while n > 0:
        d = n%10
        res = res * 10 + d
        n = n//10
    
    return sign * res

print("reverse integer : ", reverseInteger(123))