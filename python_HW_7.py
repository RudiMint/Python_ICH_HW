import random


# task 1

def sum_of_numbers():

    num = input("Введите число >>> ")
    index_count = 0
    total_sum = 0

    if num.isdigit():
        while index_count < len(num):
            total_sum += int(num[index_count])
            index_count += 1
        print(f"Сумма цифр: {total_sum}")
    else:
        print("try again. only didgits >>> ")
        sum_of_numbers()

sum_of_numbers()


# task 2

def palindrom():

    num = input("Введите число: ")
    reversed_num = ""
    index_str = len(num) - 1

    if num.isdigit():
        while index_str >= 0:
            reversed_num += num[index_str]
            index_str -= 1
        print(
            f"Число {num} является палиндромом." if num == reversed_num
              else f"Число {num} не является палиндромом."
        )
    else:
        print("try again. only didgits >>> ")
        palindrom()

palindrom()


# task 3

def try_intuition():

    num = random.randint(1, 100)
    num_of_attempts = 10

    while num_of_attempts >= 0:

        if num_of_attempts == 0:
            print(f"you failed. guessed number was {num}")
            break

        user_num = int(input("your guess >>> "))

        if num == user_num:

            if num_of_attempts == 10:
                print(f"Отличная интуиция! Вы угадали {user_num} с первой попытки!")
            else:
                print(f"Поздравляем! Вы угадали число: {user_num} за {10 - num_of_attempts} попыток. "
                      f"Отличный результат!")
            break

        elif num > user_num:
            num_of_attempts -= 1
            print("Загаданное число больше вашего")
        else:
            num_of_attempts -= 1
            print("Загаданное число меньше вашего")


try_intuition()