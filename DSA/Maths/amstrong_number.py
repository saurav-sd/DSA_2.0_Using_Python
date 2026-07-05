"""
Amstrong number : Sum of each digit raised to the power of the number of digits equals the original number.

for eg: 153

Digits = 3
1³ + 5³ + 3³
= 1 + 125 + 27
= 153

"""

def countDigit(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count


def isAmstrongNumber(n):

    on = n
    nd = countDigit(n)

    sum = 0
    while n > 0:
        d = n % 10
        sum = sum + d**nd
        n = n // 10
    
    return sum == on

print("check amstrong number : ", isAmstrongNumber(1534))

# Time = O(log n)
# Space = O(1)

