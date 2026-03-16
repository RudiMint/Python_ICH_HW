# task 1

data = {"a": 1, "b": 2, "c": 1, "d": 3}
new_data = {}

# for key, value in data.items():
#     if value in new_data.keys():
#         new_data[value].append(key)
#     else:
#         new_data[value] = [key]

for key, value in data.items():
    new_data.setdefault(value, []).append(key)

print(new_data)


# task 2

words = ["anna", "bennet", "john"]

dict_words = {word: {letter: word.count(letter) for letter in word} for word in words}

print(dict_words)


# task 3

students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}

groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]

# result = {g: {} for g in groups}
#
# for key, value in students.items():
#     if value >= 85:
#         result["Отличники"][key] = value
#     elif value >= 70:
#         result["Хорошисты"][key] = value
#     elif value >= 50:
#         result["Троечники"][key] = value
#     else:
#         result["Не сдали"][key] = value

result = {
    "Отличники": {k: v for k, v in students.items() if v >= 85},
    "Хорошисты": {k: v for k, v in students.items() if 70 <= v < 85},
    "Троечники": {k: v for k, v in students.items() if 50 <= v < 70},
    "Не сдали": {k: v for k, v in students.items() if v < 50}
}

print(result)

