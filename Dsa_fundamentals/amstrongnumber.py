class AmstrongNumber:
    def isAmstrong(self , num):
        k = len(num)
        sum = 0
        for i in num:
            sum += int(i) ** k

        print(f"Sum of digits raised to the power {k} is: {sum}")
        
        if sum == int(num):
             print(f"{num} is an Amstrong number")
        else:
            print(f"{num} is not an Amstrong number")
    

num = int(input("Enter a number: "))
amstrong = AmstrongNumber()
result = amstrong.isAmstrong(str(num))
