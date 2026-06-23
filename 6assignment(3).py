def multiply_list(lst):
    result = 1
    for num in lst:
        result = result * num
    return result

numbers = [2, 3, 4]
print(multiply_list(numbers))