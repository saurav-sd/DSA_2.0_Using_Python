def countDigit(n):
    count = 0

    while n > 0:
        count += 1
        n = n//10

    return count

res = countDigit(10000)

print("res : ", res)

# Time complaxity = O(log(n))
# Space complaxity = O(1)