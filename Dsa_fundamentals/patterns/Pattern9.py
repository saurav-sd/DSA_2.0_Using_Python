class Pattern9:
    def display(self, n):
        for i in range(n):
            for j in range(i):
                print(f" ", end="")
            for j in range(2*(n-i)-1):
                print(f"*", end="")
            print()

n = int(input("Enter the number of rows: "))
pattern = Pattern9()
pattern.display(n)