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


# r1 = Rectangle(3, 4, "red")
# r1.get_area()
# c1 = Circle(3, "blue")
# c1.get_area()
# # c1.display()
# # r1.display()
# t1 = Triangle(5, 3, "black")
# t1.get_area()

class Online_shopping_cart:

    def __init__(self):
        self.list = ["T-shirt", "shirt", "heels", "heels", "chocolate", "lip balms"]
        # self.value = ["200",  "150", "560", "320", "150"]


class Product(Online_shopping_cart):
    def b_product(self):
        product = input("Enter the product name to browse:")
        for i in self.list:
            if i == product:
                print(f"Product {product} has been found")
                break
        else:
            print("oops! not found")


class Cart(Online_shopping_cart):
    def __init__(self):
        super().__init__()
        self.fin = []

    def add_to_cart(self):
        # self.fin = []
        count = 0
        num = int(input("Enter number of elements to add in cart:"))
        for i in range(num):
            product = input("Enter the product to add in cart:")
            for j in self.list:
                if j == product:
                    self.fin.append(j)
                    count = count + 1

        print(f"...{count} Items found in a cart...")

    def display_cart(self):
        print("list of items present in a cart is :", self.fin)

    def remove_from_cart(self):
        user_input = input("Enter the element you want to remove:")
        self.fin.remove(user_input)
        self.display_cart()


class Order(Cart):

    def shipping(self):
        name = input(" Recipient.Name:")
        address = input("Recipient.Address:")
        city = input("City:")
        contact = input("contact.info:")

    def payment_details(self):
        user_input = input(""" Select the mode for payment
        Enter 1. to pay with credit card
        Enter 2. to pay with debit card
        Enter 3. for cash on delivery option
        """)

        if user_input == "1":
            print("order will be placed using credit card")
        elif user_input == "2":
            print("order will be placed using debit card")
        elif user_input == "3":
            print("order will be placed using cash on delivery")

    def review(self, cart_instance):
        cart_instance.display_cart()
        user_input = input(""" After review the Cart once:
        Enter 1. to complete order
        Enter 2. to cancel the order
        """)

        if user_input == "1":
            print("Order completed successfully...")
        elif user_input == "2":
            print("order has been cancelled")
        else:
            print("...some Error...")


c1 = Cart()
c1.add_to_cart()
c1.display_cart()
o1 = Order()
o1.review(c1)
o1.shipping()
o1.payment_details()
c1.remove_from_cart()
p1 = Product()
p1.b_product()
