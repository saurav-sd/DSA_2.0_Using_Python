class GCD:
    def gcd(self, n1, n2):
        # Approach 1: Using Euclidean algorithm
        while n1 > 0 and n2 > 0:
            if n1 > n2:
                n1 = n1 % n2
            else:
                n2 = n2 % n1
        
        if n1 == 0:
            return n2
        return n1
    
        


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
gcd = GCD()
result = gcd.gcd(n1, n2)
print(f"The GCD of {n1} and {n2} is: {result}")