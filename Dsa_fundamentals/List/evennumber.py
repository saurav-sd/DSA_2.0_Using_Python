nums = [1, 2, 3, 4, 5, 6]

even_numbers = []
for num in nums:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"Even numbers in the list: {even_numbers}")

# time complexity: O(n)
# space complexity: O(n) for the even_numbers list

