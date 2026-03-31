# task 1

strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]

new_strings = []

for s in strings:

    stripped = s.rstrip("0123456789")
    if s != stripped and not any(e.isdigit() for e in stripped):
        new_strings.append(s)

print(new_strings)


# task 2

numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]

user_num = int(input("enter a number to remove elements that are multiplies of it >>> "))

new_numbers = [e for e in numbers if e % user_num != 0]

print(new_numbers)


# task 3

numbers_1 = [5, 2, 3, 8, 4, 1, 2, 7]
even_numbers = sorted(
    [n for n in numbers_1 if n % 2 == 0],
    reverse=True
)

count = 0

for i in range(len(numbers_1)):
    if numbers_1[i] % 2 == 0:
        numbers_1[i] = even_numbers[count]
        count += 1

print(numbers_1)

# first attempt:
# even_numbers = []
# for i in numbers_1:
#     if i % 2 == 0:
#         even_numbers.append(i)
#
# even_numbers.sort()
# even_numbers.reverse()
