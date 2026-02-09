import re


# task 1

text_1 = "My number is 123-456-789"
res = ""

for i in text_1:
    if i.isdigit():
        res += "*"
    else:
        res += i

print(f"string: {text_1}\nresult: {res}")

# task 2

text = "Programming in python"

for sym in text.lower():
    count = 0
    for e in text.lower():
        if sym == e:
            count += 1
    print(f"Символ '{sym}' встречается {count} раз(а)")


# task 3

text_3 = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."

def multiply_by_10(match):
    return str(float(match.group()) * 10)

result_3 = re.sub(r'\b\d+(\.\d+)?\b', multiply_by_10, text_3)

print(result_3)
