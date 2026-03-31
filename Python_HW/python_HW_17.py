# task 1

set1 = {1, 2, 3, 4}
set2 = {2, 3}

indicator = True

for i in set2:
    if i not in set1:
        indicator = False
        break

print(indicator)

result1 = set1 & set2

print(result1 == set2)
print(set2 <= set1)
print(set2 < set1)
print(set2.issubset(set1))
print(all(i in set1 for i in set2))
print(set2.difference(set1))


# task 2

set1 = {2, 3, 4, 5, 6}
set2 = {4, 5}

if set1.issubset(set2):
    print(f"Подмножество: {set1 <= set2}\nРазница: {set2 - set1}")
elif set2.issubset(set1):
    print(f"Подмножество: {set2 <= set1}\nРазница: {set1 - set2}")
else:
    print("False")
