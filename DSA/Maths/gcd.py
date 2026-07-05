# Bruteforce approach

def gcd(a,b):
    ans = 1

    for i in range(1, min(a,b)+1):
        if a % i == 0 and b % i == 0:
            ans = i
    
    return ans

print(gcd(12,18))

# Time = O(min(a,b))
# Space = O(1)

#--------------------------------
# Approach 2 : Eucledial algo

# 1. recurssive
def gcd_e(a,b):
    if b == 0:
        return a
    
    return gcd(b,a%b)

# 2. iterative
def gcd_i(a,b):
    while b != 0:
        a,b = b, a%b
    
    return a

# Time = O(log(min(a,b)))
# Space = O(1)

