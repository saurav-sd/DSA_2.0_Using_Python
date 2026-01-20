class Pattern5:
    def display(self , n):
        for i in range(1,n+1):
            for j in range(1,n-i+2):
                print(f"{j} ", end="")
            print()


n = int(input("Enter the number of rows: "))
pattern = Pattern5()
pattern.display(n)