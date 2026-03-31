# Task 1


def sum_of_numbers():
    number = input("type 4 digits: ")

    if len(number) == 4 and number.isdigit():
        total = 0
        for i in number:
            total += int(i)
        return total

    else:
        return sum_of_numbers()


result = sum_of_numbers()
print(result)


#Task 2


def multiplier():
    first_number = input("type your first number: ")
    second_number = input("type your second number: ")
    if first_number.isdigit() and second_number.isdigit():
        return f"{int(first_number) * int(second_number)}-{first_number}-{second_number}"
    else:
        return multiplier()

print(multiplier())


#Task 3


def division():
    while True:
        try:
            first_number = int(input("you type ya first number: "))
            second_number = int(input("and di second numba: "))
            if second_number == 0:
                print("you dey misbehave well well, try am again >:C")
                continue
            break
        except ValueError:
            print("Look what you din done did, expected integer. TRY AGAIN> ")

    remainder = first_number
    int_division = 0
    while remainder >= second_number:
        remainder -= second_number
        int_division += 1
    return f"remainder of division: {remainder}\ninteger of division: {int_division}"

print(division())
