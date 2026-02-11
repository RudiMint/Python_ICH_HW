#  task 1

numbers = [1245.4435, -302.1403, 87459.99, -520.8265, 1450.001]
res = 0
for n in numbers:
    if n > 0:
        res += n

print(f"Сумма положительных чисел: ${res:,.2f}")


# task 2

data_list = [

    "John 23 12345.678",

    "Alice 30 200.50",

    "Bob 35 15000.3",

    "Charlie 40 500.75"
    ]

for s in data_list:
    name, age, balance = s.split()
    print(f"name: {name:<10}| age: {age:^3}| balance: {float(balance):>10.2f}")
