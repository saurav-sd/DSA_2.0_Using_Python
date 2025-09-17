class Pattern10:
    def display(self, n):
        for i in range(0,n):
            for j in range(i):
                print(f" ", end="")
            for j in range(2*(n-i)-1):
                print(f"*", end="")
            for j in range(i):
                print(f" ", end="")
            print()

n = int(input("Enter the number of rows: "))
pattern = Pattern10()
pattern.display(n)