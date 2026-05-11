# task 1

class Rectangle:
    """
    A class representing a rectangle.
    Attributes:
        width (int | float): The width of the rectangle.
        height (int | float): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle object.
        Args:
            width (int | float): The width of the rectangle.
            height (int | float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def get_area(self):
        """
        Calculate and return the area of the rectangle.
        Returns:
            int | float: The area of the rectangle.
        """
        return self.height * self.width


rectangle = Rectangle(9, 3)

print(f"area: {rectangle.get_area()}")

rectangle.width = 6
rectangle.height = 4

print(f"new area: {rectangle.get_area()}")


# task 2

class Counter:
    """
    A simple counter class.
    Attributes:
        value (int): Stores the current counter value.
    """
    def __init__(self):
        """
        Initialize the counter with a starting value of 0.
        """
        self.value = 0

    def increasement(self):
        """
        Increase the counter value by 1.
        Returns:
            int: The updated counter value.
        """
        self.value += 1
        print(f"value increased. current value: {self.value}")
        return self.value

    def decreasement(self):
        """
        Decrease the counter value by 1.
        Returns:
            int: The updated counter value.
        """
        self.value -= 1
        print(f"value decreased. current value: {self.value}")
        return self.value

    def get_value(self):
        """
        Display and return the current counter value.
        Returns:
            int: The current counter value.
        """
        print(f"current value: {self.value}")
        return self.value


counter = Counter()

counter.get_value()
counter.increasement()
counter.increasement()
counter.decreasement()

