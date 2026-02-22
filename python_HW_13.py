# task 1

numbers = (3, 7, 2, 8, 5, 10, 1)

new_numbers = tuple()

for i in numbers:
    if not new_numbers:
        new_numbers += (i,)
    if i > new_numbers[-1]:
        new_numbers += (i,)

print(f"increasing tuple: {new_numbers}")


# task 2

numbers_1 = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)

for num in set(numbers_1):
    index_list = []

    if numbers_1.count(num) > 1:
        for index, value in enumerate(numbers_1):
            if value == num:
                index_list.append(index)

        print(f"{num} found by indexes:", *index_list)

