# Bruteforce solution :


def divisors(n):
    if n == 0:
        return

    for i in range(1, n + 1):
        if n % i == 0:
            print(i, " ")


# Time  = O(n)
# Space = O(1)


# optimize solution

def divisors_o(n):
    divisor = []

    if n == 0:
        return

    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisor.append(i)

            # avoid the duplicates when i == n//i
            if i != n//i:
                divisor.append(n//i)
                
    divisor.sort()
    return divisor


print(divisors_o(36))
