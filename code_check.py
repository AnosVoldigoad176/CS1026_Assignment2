def basic_code(num):

    # Calculate sum of digit of the number for B.C algo
    sum_digit = 0
    num_temp = str(num)[:-1]    # Delete last digit and use new number as num_temp
    for digit in num_temp:      # For loop to calculate sum of num_temp
        sum_digit = sum_digit + int(digit)
    # print(sum_digit)

    # Check last digit
    if sum_digit % 10 != num % 10:
        return False
    elif sum_digit % 10 == num % 10:
        return True
    else:
        print("Something went wrong.")
# End basic_code()


def positional_code(num):

    # Calculate sum of digit of the number with P.C algorithm
    sum_digit = 0
    index = 0
    num_temp = str(num)[:-1]
    len_nt = len(num_temp)

    for digit in num_temp:                              # For loop to go through all the number in num_temp
        if num_temp[index] == str(digit):               # If num_temp at the index position = digit
            sum_digit += int(digit) * (index + 1)       # Then calculate sum
            if index < len_nt:                          # If index is smaller than length of num_temp
                index += 1                              # Increase index by 1
    # print(sum_digit)

    # P.C check
    if sum_digit % 10 != num % 10:
        return False
    elif sum_digit % 10 == num % 10:
        return True
    else:
        print("Something went wrong.")
# End positional_code()


def UPC_code(num):
    sum_digit = 0
    index = 0
    num_temp = str(num)[:-1]

    for digit in num_temp:
        if int(digit) % 2 == 0:
            sum_digit += int(digit) * 1
        elif int(digit) % 2 != 0:
            sum_digit += int(digit) * 3
    print(sum_digit)

    res_digit = sum_digit % 10
    if 1 <= res_digit <= 9:
        res_digit = 10 - res_digit

    if res_digit == num % 10:
        return True
    elif res_digit != num % 10:
        return False
    else:
        print("Something went wrong")

# End UPC_code()


print(basic_code(24528348))
print(positional_code(434191))
print(UPC_code(24528344))
