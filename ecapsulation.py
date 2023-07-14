class Point:

    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return "<{},{}>".format(self.x_cod, self.y_cod)

    def euclidean_distance(self, other):
        return ((self.x_cod - other.x_cod) ** 2 + (self.y_cod - other.y_cod) ** 2) ** 0.5

    def distance_from_oigrin(self):
        return self.euclidean_distance(Point(0, 0))


class Line:

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return "{}x + {}y +{} = 0".format(self.A, self.B, self.C)


# p1 = Point(0, 0)
# p2 = Point(10, 10)
# print(p1)
# print(p2)
# print(p1.euclidean_distance(p2))
# print(p1.distance_from_oigrin())
# l1 = Line(1,2,3)
# print(l1)

class Product:

    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def set_quantity(self, new_quantity):
        self.__quantity = new_quantity

    def display(self):
        print(f"Total price of {self.__name} is:", self.calculate_total_value())

    def calculate_total_value(self):
        c = self.__quantity * self.__price
        gst = c * 18 / 100
        return c + gst


# obj_1 = Product("T-shirt", 250, 2)
# obj_2 = Product("Shirt", 100, 2)
# obj_1.display()
# obj_2.display()
# obj_1.set_quantity(10)
# obj_1.display()
# obj_1.calculate_total_value()

class Email:

    def __init__(self):
        self.sender = ""
        self.recipient = ""
        self.__subject = ""
        self.__body = ""

    def display(self):
        self.sender = input("From:")
        self.recipient = input("To:")
        self.__subject = input("Subject:")
        self.__body = input("Main boby:")
        print("Email is send successfully....")

mail_1 = Email()
mail_2 = Email()
mail_1.display()
mail_2.display()
print(mail_1.sender)

