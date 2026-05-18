class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        super().introduce()
        print(f"I`m on course {self.course}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        print(f"Hello, I am professor {self.name}\nMy subject is {self.subject}")


people = [
    Student("Dave", 2),
    Student("Clara", 3),
    Teacher("Pat", "English Literature"),
    Teacher("Amanda", "Self Defence")
          ]

for person in people:
    person.introduce()