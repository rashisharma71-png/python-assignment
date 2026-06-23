numbers = (5, 10, 15, 20, 25)

element = int(input("Enter a number to search: "))

if element in numbers:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")
