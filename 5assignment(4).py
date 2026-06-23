numbers = (12, 45, 7, 89, 23, 56)

total = 0
highest = numbers[0]
lowest = numbers[0]

for num in numbers:
    total += num

    if num > highest:
        highest = num

    if num < lowest:
        lowest = num

print("Tuple:", numbers)
print("Total =", total)
print("Highest =", highest)
print("Lowest =", lowest)
