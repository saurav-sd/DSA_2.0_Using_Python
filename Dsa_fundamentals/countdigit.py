import math

class CountDigit:
    def count_digit(self, n):
        #Approach 1
        # if n == 0:
        #     return 1
        # count = 0
        # while n != 0:
        #     n //= 10
        #     count += 1

        #Approach 2
        if n == 0:
            return 1
        count = int(math.log10(n) + 1) 
        return count
    

n = int(input("Enter a number: "))
count_digit = CountDigit()
result = count_digit.count_digit(n)
print(f"The number of digits in {n} is: {result}")