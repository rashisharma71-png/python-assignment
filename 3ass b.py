num = int(input("Enter a number between 2 and 50: "))

if num < 2 or num > 50:
    print("Please enter a number between 2 and 50.")
else:
    print("\nTable of", num)

    for i in range(1, 11):
        print(num, "x", i, "=", num * i)