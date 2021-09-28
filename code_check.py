def basic_code(num):

    # Calculate sum of digit of the number with B.C algorithm
    sum_digit = 0
    for x in str(num):
        sum_digit = sum_digit + int(x)

    # B.C check
    last_num = num % 10
    if (sum_digit - last_num) % 10 != last_num:
        return False
    elif (sum_digit - last_num) % 10 == last_num:
        return True
    else:
        print("Something went wrong.")

# End basic_code function


def positional_code(num):

    # Calculate sum of digit of the number with P.C algorithm
    sum_digit = 0
    for x in str(num):
        for y in range(len(str(num)) - 1):
            sum_digit = sum_digit + int(int(x) * (y + 1))

    print(sum_digit)

    # P.C check
    last_num = num % 10
    if (sum_digit - last_num) % 10 != last_num:
        return False
    elif (sum_digit - last_num) % 10 == last_num:
        return True
    else:
        print("Something went wrong.")

# End positional_code function


print(basic_code(24528349))
print(positional_code(24528349))
