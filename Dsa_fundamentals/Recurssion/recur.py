def sum(num):
    if num == 0:
        return 0
    else:
        return num + sum(num-1)

calculate_sum = sum(5)
print(calculate_sum)

