# def greeting():
#     name = input("name yourself: ")
#     age = input("now age: ")
#     color = input("and your favourite colour: ")
#     return f"Меня зовут {name}, мне {age} лет, и мой любимый цвет — {color}."
#
# print(greeting())

# string = 'Она сказала: "Привет!"'
# print(f"{string}\n" * 3)
#
# print("\tУчеба\n\tУборка\n\tСпорт")
#
# Введите расстояние (в км): 150
# Введите среднюю скорость (в км/ч): 50
# Время в пути: 3.0 часов

# def mathematika():
#     distance = input("how far you`re willing to go? > ")
#     speed = input("how fast? ")
#     trip_time = round(int(distance) / int(speed), 1)
#     total_minutes = trip_time * 60
#     hours = total_minutes // 60
#     minutes = total_minutes % 60
#     print(f"Время в пути: {trip_time} часов")
#     print(f"Время в пути: {int(hours)} часа и {int(minutes)} минут")
#
# mathematika()
#
# Напишите программу, которая принимает от пользователя количество дней до события и выводит, сколько это
# недель и дней.
# Пример вывода:
# Введите количество дней до события: 45
# До события осталось: 6 недель и 3 дня.
#
# days_before_event = int(input("Введите количество дней до события: "))
# weeks = days_before_event // 7
# days = days_before_event - weeks * 7
# print(f"До события осталось: {int(weeks)} недель и {int(days)} дня")


# Напишите программу, которая принимает расстояние в километрах, расход бензина на 100 км и цену за литр
# бензина. Программа должна рассчитать стоимость бензина для поездки.
# Пример вывода:
# Введите расстояние (в км): 300
# Введите расход бензина на 100 км: 8
# Введите цену за литр бензина: 60
# Стоимость бензина для поездки: 1440.0

# def fuel_costs():
#
#     distance = int(input("Введите расстояние (в км): "))
#     fuel_consumption = int(input("Введите расход бензина на 100 км: "))
#     money_per_liter = int(input("Введите цену за литр бензина: "))
#     total_money = (distance / 100) * fuel_consumption * money_per_liter
#     print(f"Стоимость бензина для поездки: {round(total_money, 1)}")
#
# fuel_costs()
#
# Напишите программу, которая запрашивает у пользователя количество задач и среднее время выполнения
# одной задачи (в минутах). Программа должна вывести общее время выполнения всех задач в формате часов и
# минут.
# Пример вывода:
# Введите количество задач: 5
# Введите среднее время выполнения одной задачи (мин): 40
# Общее время: 3 часа и 20 минут

tasks = int(input("Введите количество задач: "))
average_time = int(input("Введите среднее время выполнения одной задачи (мин): "))
total_min = tasks * average_time
hours = total_min // 60
minutes = total_min % 60
print(f"Общее время: {int(hours)} часа и {int(minutes)} минут")
