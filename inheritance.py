from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_area(self):
        pass

    def display(self):
        print('hello friend..')


class Rectangle(Shape):
    def __init__(self, len, width, color):
        super().__init__(color)
        self.len = len
        self.width = width

    def get_area(self):
        c = self.len * self.width
        print("Area of Rectangle is:", c, "and color is:", self.color)


class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.pi = 3.14
        self.radius = radius

    def get_area(self):
        c = self.pi * (self.radius * self.radius)
        print("Area of Rectangle is:", c, "and color is:", self.color)


class Triangle(Shape):
    def __init__(self, base, height, color):
        super().__init__(color)
        self.height = height
        self.base = base

    def get_area(self):
        c = self.height * self.base / 2
        print("Area of triangle is:", c, "and color of triangle is:", self.color)


r1 = Rectangle(3, 4, "red")
r1.get_area()
c1 = Circle(3, "blue")
c1.get_area()
# c1.display()
# r1.display()
t1 = Triangle(5, 3, "black")
t1.get_area()
