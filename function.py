# def sum_of_numbers(a,b):
#     return a + b

# res1 = sum_of_numbers(10,20)
# print(res1)


# def check_age(age):
#     if age >= 18:
#         print("Adult")
#     else:
#         print("Minor")

# res2 = check_age(20)

max = 0
def highest_number(a,b,c):
    if a > b:
        max = a
    elif b > a:
        max = b
    elif c > max:
        max = c
    else:
        max = c
    return max

res3 = highest_number(10,20,30)
print(res3)

