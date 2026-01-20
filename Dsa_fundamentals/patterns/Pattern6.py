class Pattern6:
    def pattern(self, n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(f"{i} ", end="")
            print()

n = int(input("Enter the number of rows: "))
pattern = Pattern6()
pattern.pattern(n)