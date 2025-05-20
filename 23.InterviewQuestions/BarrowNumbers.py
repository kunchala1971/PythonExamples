# you have two numbers number1 and number2,
# you job is to check the number of borrow operations needed for subtraction of number1 from number2
# if the subtraction is not possible then return the string not possible

def count_borrows(number1, number2):
    if number2 < number1:
        return "not possible"

    num1_str = str(number1)
    num2_str = str(number2)

    max_length = max(len(num1_str), len(num2_str))
    num1_str = num1_str.zfill(max_length)
    num2_str = num2_str.zfill(max_length)

    borrow_count = 0
    borrow = 0

    for i in range(max_length - 1, -1, -1):
        digit1 = int(num1_str[i]) + borrow
        digit2 = int(num2_str[i])

        if digit2 < digit1:
            borrow_count += 1
            borrow = 1
        else:
            borrow = 0

    return borrow_count



number1 = 658
number2 = 754
result = count_borrows(number1, number2)
print(result)
