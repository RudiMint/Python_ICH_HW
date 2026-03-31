from collections import Counter, defaultdict

# task 1

text_1 = "Programming is fun!"

# def letter_counter(text):
#     dicts = {k: text.count(k) for k in text if k.isalpha()}
#     return dicts

def letter_counter(text):
    return Counter(c for c in text if c.isalpha())

print(letter_counter(text_1))


# task 2

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

# students_group = {}
#
# for clss, name in students:
#     students_group.setdefault(clss, []).append(name)

students_group = defaultdict(list)

for clss, name in students:
    students_group[clss].append(name)

print(students_group)

