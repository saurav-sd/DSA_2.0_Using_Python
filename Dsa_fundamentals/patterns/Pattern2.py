class Pattern2:
    def pattern(self, n):
        for i in range(0,n):
            for j in range(0,i+1):
                print("* ", end="")
            print()

n = int(input("Enter the number of rows: "))
pattern = Pattern2()
pattern.pattern(n)