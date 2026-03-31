# task 1

text_1 = "My number is 123-456-789"

res_1 = text_1

for d in "0123456789":
    res_1 = res_1.replace(d, "*")

print(f"string: {text_1}\nresult: {res_1}")


res_1_1 = text_1.translate(str.maketrans("0123456789", "*" * 10))

print(f"string: {text_1}\nresult: {res_1_1}")


# task 2

text = "Programming in python"

for sym in text.lower():
    print(f"Символ '{sym}' встречается {text.count(sym)} раз(а)")


# task 3

text_3 = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."

list_of_words = text_3.split(" ")

for e in range(len(list_of_words)):
    element = list_of_words[e]
    if element[0].isdigit():
        list_of_words[e] = str(float(element) * 10)

print(" ".join(list_of_words))
