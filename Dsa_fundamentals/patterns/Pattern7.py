class Pattern7:
    def display(self, n):
        for i in range(n, 0, -1):
            for j in range(1, i + 1):
                print(f"{j} ", end="")
            print()

n = int(input("Enter the number of rows: "))
pattern = Pattern7()
pattern.display(n)