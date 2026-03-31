# Task 1

first_v = bool(input("Enter first value, if there`s none, just skip: "))
second_v = bool(input("Enter second value, if there`s none, just skip: "))
print(
    f"and: {first_v and second_v}\n"
    f"or: {first_v or second_v}\n"
    f"not: {not first_v}\n"
    f"equal: {first_v == second_v}\n"
    f"not equal: {first_v != second_v}"
)


# Task 2

lights_on = bool(input("if lights on: type smth, else: skip >> "))
window_open = bool(input("if window is open: type smth, else: skip >> "))

print(
    f"Свет включён? {lights_on}\n"
    f"Окно открыто? {window_open}\n"
    f"Оба условия выполнены? {lights_on and window_open}\n"
    f"Хотя бы одно условие выполнено? {lights_on or window_open}"
)


# Task 3

def internet_price():
    used_mb = int(input("Введите использованные мегабайты: "))
    payment = 30
    price_per_mb = 0.2
    if used_mb <= 500:
        return payment
    else:
        payment += round((used_mb - 500) * price_per_mb, 1)
        return payment

print(f"Общая стоимость: {internet_price()} €")
