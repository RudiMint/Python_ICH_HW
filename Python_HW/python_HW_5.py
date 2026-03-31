#Task 1

def sorting_numbers():

    numbers = []

    for i in range(1, 4):
        numbers += [int(input(f"Введите {i}-е число: "))]
    numbers.sort()

    print("Числа в порядке возрастания: ", *numbers, sep=", ")

sorting_numbers()


# Task 2

year = int(input("Введите год: "))

def leap_year(year):
    if year % 400 == 0:
        print("Год является високосным.")
    elif year % 4 == 0 and year % 100 != 0:
        print("Год является високосным.")
    else:
        print("Год не является високосным.")

leap_year(year)
#
# test = [1995, 1996, 1997, 1998, 1999]
#
# for y in test:
#     print(y, leap_year(y))




