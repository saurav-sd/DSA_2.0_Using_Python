class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        negative = x < 0
        x = abs(x)
        while x != 0:
            d = x % 10
            rev = rev * 10 + d
            x = x // 10
        if negative:
            rev = -rev
        # Check for 32-bit signed integer overflow
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
    

n = int(input("Enter a number: "))
solution = Solution()
result = solution.reverse(n)
print(f"The reverse of {n} is: {result}")