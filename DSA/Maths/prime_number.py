def isPrime(n):
    # edge case
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# print(isPrime(6))

# Time  = O(n) , O(root(N))
# Space = O(1)

# -----------------------------------

# print all the prime number till N

def allPrimeNumber(n):
    for i in range(2, n+1):
        if isPrime(i):
            print(i)


# print(allPrimeNumber(30))

# Time  = (n * root(n))
# Space = O(1)

# Optimised approach : Sieve of Eratosthenes
# 1. initially assumes every number is prime.
# 2. then eleminates multiple of each prime.
# 3. print the unmarked one

def sieve(n):
    prime = [True] * (n+1)

    for i in range(2, n+1):
        if prime[i]:
            for j in range(i*2, n+1, i):
                prime[j] = False
    
    for i in range(2, n+1):
        if prime[i]:
            print(i, end=" ")

print(sieve(30))

# optimised approach


def countPrimes(self, n: int) -> int:
    prime = [True] * n
    count = 0

    if n <= 2:
        return 0

    prime[0] = prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n, i):
                prime[j] = False

    for i in range(2, n):
        if prime[i]:
            count += 1

    return count

# Time  = O(n * log log n)
# Space = O(1)