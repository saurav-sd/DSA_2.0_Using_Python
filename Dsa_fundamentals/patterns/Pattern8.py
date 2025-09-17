class Pattern8:
    def display(self, n):
        for i in range(0,int(n/2)+1):
            for j in range(0, int(n/2)-i):
                print(f" ", end="")
            for j in range(0, i*2 + 1):
                print(f"*", end="")
            print()

n = int(input("Enter the number of rows: "))
pattern = Pattern8()
pattern.display(n)