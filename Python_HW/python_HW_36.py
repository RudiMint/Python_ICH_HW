class Person:
    """
    Base class representing a generic person.
    """
    def __init__(self, name):
        self.name = name

    def introduce(self):
        """
        Return a basic introduction message.
        """
        return f"Hello, my name is {self.name}"
class Student(Person):
    """
    Represents a student.
    """
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        """
        Return the student's introduction.
        """
        base_intro = super().introduce()
        return f"{base_intro}\nI'm on course {self.course}"

class Teacher(Person):
    """
    Represents a teacher.
    """
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        """
        Return the teacher's introduction.
        """
        return (
            f"Hello, I am Professor {self.name}\n"
            f"My subject is {self.subject}"
        )


people = [
    Student("Dave", 2),
    Student("Clara", 3),
    Teacher("Pat", "English Literature"),
    Teacher("Amanda", "Self Defence")
          ]

for person in people:
    print(person.introduce())