n1 = int(input("Enter First number : "))
n2 = int(input("Enter second number : "))
operator  = input("Choose operator (+,-,*,/): ")

if operator == "+":
    print(n1+n2)
elif operator == "-":
    print(n1-n2)
elif operator == "/":
    if n2 == 0:
        print("invalid operation")
    else:
        print(n1/n2)
else:
    print("None...")




