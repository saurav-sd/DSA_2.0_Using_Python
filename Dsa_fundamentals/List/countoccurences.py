items = ['apple', 'banana', 'apple', 'cherry']

# count = 0
# target = 'banana'
# frequency = {}

# for item in items:
#     if item in frequency:
#         frequency[item] += 1
#     else:
#         frequency[item] = 1

# print(frequency)
# print(frequency[target])

itemsList = ['pen', 'pencil', 'eraser']

target = 'eraser'
found = False

for item in itemsList:
    if item == target:
        found = True
        break

print(found)

print(target in itemsList)
