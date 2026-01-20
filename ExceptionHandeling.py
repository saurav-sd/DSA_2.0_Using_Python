# try:
#     num1  = int(input("Enter First number : "))
#     num2 = int(input("Enter secont number : "))
#     res = num1/num2
# except ValueError:
#     print("please enter valid number")
# except ZeroDivisionError:
#     print("divisor shound not be zero")



# try:
#     fileName = input("Enter a file name : ")
#     f = open(fileName, "r")
#     print(f.read())
# except FileNotFoundError:
#     print("file not found")
# finally:
#     print("program ends !")


# class AgeError(Exception):
#     pass

# try:
#     age = int(input("Enter age : "))
#     if age < 18:
#         raise AgeError("Not eligible !")
#     else:
#         print("Eligible")

# except AgeError as e:
#     print(e)

# except ValueError:
#     print("please enter a valid numver")


# def safe_divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "cannot divide"

# print(safe_divide(10,2))
