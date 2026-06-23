def check_range(num):
    if 10 <= num <= 50:
        return "Number is within the range."
    else:
        return "Number is outside the range."

print(check_range(25))