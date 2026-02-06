# task 1

list_of_coins = [50, 10, 5, 2, 1]

cost = int(input("enter the cost of the goods >>> "))

for c in list_of_coins:
    count = cost // c
    if count > 0:
        print(f"insert coins of the following denominations {c}: {count}")
        cost %= c


# task 2

numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
print(f"initial list: {numbers}")
numbers = [n ** 2 if n % 2 != 0 else n for n in numbers]
print(numbers)