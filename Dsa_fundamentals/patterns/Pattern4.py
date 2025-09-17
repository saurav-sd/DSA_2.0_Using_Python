class Pattern4:
    def display(self , n):
        for i in range(1,n+1):
            for j in range(0,n-i+1):
                print("* ", end="")
            print()


n = int(input("Enter the number of rows: "))
pattern = Pattern4()
pattern.display(n)