# task 1

def code_check():

    sym = input("enter your symbol >> ")
    
    if len(sym) != 1:
        code_check()
    else:
        print(f"Код Unicode: {ord(sym)}\n"
              f"ASCII символ: {ord(sym) <= 127}")


code_check()


# task 2

def play_with_str():

    text = input("type your text >>> ")
    index_1 = int(input("your first index >>> "))
    index_2 = int(input("your wished length >>> "))
    res = text[index_1 - 1::]

    if len(res) == index_2:
        print(f"your result: '{res}'")
    elif len(res) > index_2:
        print(f"your result: '{res[:-(len(res) - index_2)]}'")
    else:
        print(f"your result: '{res + "_" * (index_2 - len(res))}'")


play_with_str()


# task 3

def count_symbol():

    text = input("Введите строку: ")
    sym = input("Введите символ: ")
    count = 0

    for i in text:
        if i == sym:
            count += 1

    print(f"Символ {sym} встречается {count} раз(а).")


count_symbol()


# task 4

def play_with_text():

    text = input("Введите строку: ")
    new_text = ""

    for i in text:
        if not i.isdigit():
            new_text += i

    print(f"Результат: {new_text[::-1]}")


play_with_text()
