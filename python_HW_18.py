# task 1

numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]

new_numbers = sorted(list({i for i in numbers if numbers.count(i) > 1}), reverse=True)
print(new_numbers)


# task 2

dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}

indicator1 = True

for key, value in dict1.items():
    if key not in dict2 or dict2[key] != value:
        indicator1 = False
        break

# indicator2 = all(dict2.get(k) == v for k, v in dict1.items())
#
# print(f"first dictionary is in second >>> {indicator2}")

print(f"first dictionary is in second >>> {indicator1}")

