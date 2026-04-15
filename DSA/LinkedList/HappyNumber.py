# Approach 1 : using hastset

# helper function : calculates the sum of the square of the digits.
def get_next(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total

def isHappy(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False
        
        seen.add(n)
        n = get_next(n)

    return True


# Approach 2 : using fast and slow pointer.
def isHappy_2(n):
    slow = n
    fast = get_next(n)

    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

    return fast == 1

n = 19
print(isHappy_2(n))