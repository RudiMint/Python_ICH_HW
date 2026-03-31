import math


def round_the_math_way():
    num = float(input("give me your digits with '.' >>> "))
    if num > 0:
        print(math.ceil(num))
    else:
        print(math.floor(num))


round_the_math_way()


def count_hypotenuse():
    a = float(input("first side of a triangle >>> "))
    b = float(input("second side of the same triangle >>> "))
    c = math.sqrt(a ** 2 + b ** 2)
    print(f"your hypotenuse is {round(c, 1)}")


count_hypotenuse()