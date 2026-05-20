import math
from abc import ABC, abstractmethod


class InvalidSizeError(Exception):
    """Exception raised when a shape is initialized with invalid (non-positive) dimensions."""
    pass


class Shape(ABC):
    """
    Abstract base class for geometric shapes.

    All subclasses must implement the `area()` method.

    Methods:
        area(): Abstract method that returns the area of the shape.
    """

    @abstractmethod
    def area(self):
        """Returns the area of the figure"""
        pass


class Circle(Shape):
    """
    Represents a circle shape.

    Attributes:
        radius (float): Radius of the circle.

    Methods:
        area(): Computes and returns the area of the circle.
    """
    def __init__(self, radius):
        self.__validate_size(radius)
        self.radius = radius

    @staticmethod
    def __validate_size(radius):
        """Validate that radius is greater than zero."""
        if radius <= 0:
            raise InvalidSizeError("Radius must be > 0")

    def area(self):
        """
        Compute the area of the circle.

        Returns:
            float: Area of the circle using πr².
        """
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    """
    Represents a rectangle shape.

    Attributes:
        height (float): Height of the rectangle.
        width (float): Width of the rectangle.

    Methods:
        area(): Computes and returns the area of the rectangle.
    """
    def __init__(self, height, width):
        self.__validate_size(height, width)
        self.height = height
        self.width = width

    @staticmethod
    def __validate_size(height, width):
        """Validate that height and width are greater than zero."""
        if height <= 0 or width <= 0:
            raise InvalidSizeError("Both Height and Width must be > 0")

    def area(self):
        """
        Compute the area of the rectangle.

        Returns:
            float: Area of the rectangle using height × width.
        """
        return self.height * self.width


shapes = [Circle(60), Rectangle(9, 5)]

for shape in shapes:

    print(f"Area: {shape.area():.2f}")


