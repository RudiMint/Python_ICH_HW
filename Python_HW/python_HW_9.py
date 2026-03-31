# task 1

def multiplication_table():
    num = int(input("enter a number >>> "))
    width = len(str(num * num + 1))
    for i in range(1, num + 1):
        for w in range(1, num + 1):
            print(f"{i * w:>{width}}", end=" ")
        print()


# task 2

def staicase_of_numbers():
    num = int(input("give me your number >>> "))
    for i in range(1, num + 1):
        for n in range(1, i + 1):
            print(n, end=" ")
        print()


# task 3

def unique_symbols():
    text = input("type smth >>> ")
    new_text = ""
    for i in text:
        if i in new_text:
            continue
        new_text += i
    print(new_text)


unique_symbols()
multiplication_table()
staicase_of_numbers()