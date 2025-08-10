# oop/polymorphism_demo.py

import math


class Shape:
    def area(self):
        """Base method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement area().")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Returns int if both length and width are ints (e.g., 10 * 5 -> 50)
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # π * r^2
        return math.pi * (self.radius ** 2)
