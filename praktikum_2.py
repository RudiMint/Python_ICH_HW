# Task 1

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
#
# if a < b < c:
#     print("Числа упорядочены по возрастанию.")
# else:
#     print("Числа ne упорядочены по возрастанию.")

# task 2

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
#
# match a, b:
#     case _ if a > b:
#         print(f"Большее число: {a}")
#     case _ if b > a:
#         print(f"Большее число: {b}")
#     case _ :
#         print("Числа равны")

# task 3

# num = int(input("Введите число: "))
# print("Четное" if num % 2 == 0 else "Нечетное")

# task 4

# age = int(input("Введите возраст: "))
#
# match age:
#     case _ if age < 12:
#         print("ребенок")
#     case _ if 12 <= age < 18:
#         print("подросток")
#     case _ if 18 <= age < 60:
#         print("взрослый")
#     case _ :
#         print("пожилой")

# task 5

# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью сторону: "))
#
# if a < b + c and b < a + c and c < a + b:
#     print("Такой треугольник может существовать.")
# else:
#     print("Такой треугольник ne может существовать.")

# task 6

# text = input("type etwas: ")
# if text:
#     print("molodets")
# else:
#     print("Строка пуста.")

# task 7

# 2 | 1
# 3 | 4

# x = int(input("Введите координату x: "))
# y = int(input("Введите координату y: "))
#
# if x > 0 and y > 0:
#     print("Точка находится в первом квадранте.")
# elif x < 0 and y > 0:
#     print("Точка находится во втором квадранте.")
# elif x < 0 and y < 0:
#     print("Точка находится в третьем квадранте.")
# elif x > 0 and y < 0:
#     print("Точка находится в четвертом квадранте.")
# elif x == 0 and y == 0:
#     print("Точка находится в начале координат.")
# elif x == 0:
#     print("Точка находится на оси Y.")
# elif y == 0:
#     print("Точка находится на оси X.")

# task 8

# hours = int(input("Введите часы: "))
# minutes = int(input("Введите минуты: "))
#
# if hours <= 24 and minutes <= 60:
#     print("корректное время")
# else:
#     print("Некорректное время")

# task 9

# a = int(input("enter digit: "))
# b = int(input("enter digit: "))
# c = int(input("enter digit: "))
#
# if a == 0 or b == 0 or c == 0:
#     print("Произведение равно нулю.")
# else:
#     negatives = 0
#     if a < 0:
#         negatives += 1
#     if b < 0:
#         negatives += 1
#     if c < 0:
#         negatives += 1
#
#     if negatives % 2 == 0:
#         print("Произведение положительное.")
#     else:
#         print("Произведение отрицательное.")


# task 10

income = float(input("Введите доход: "))
tax = 0.0

if income <= 10000:
    tax = income * 0.05
elif income <= 50000:
    tax = income * 0.10
else:
    tax = income * 0.20

net_income = income - tax

print(f"Налог: {tax}\nИтоговая сумма после уплаты налога: {net_income}")