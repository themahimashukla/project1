# import as self
# class Atm:
#     def __init__(self):
#         self.pin = ""
#         self.balance = 0
#         self.menu()
#
#     def menu(self):
#         user_input = input("""
#         hello! how would you like to proceed?
#         1.enter 1 to create pin
#         2. enter 2 to deposit
#         3. enter 3 to withdraw
#         4.enter 4 to check the balance
#         5.enter 5 to exit
#         """)
#         if user_input == "1":
#             self.create_pin()
#         elif user_input == "2":
#             self.deposit()
#         elif user_input == "3":
#             self.withdrawn()
#         elif user_input == "4":
#             self.check_balance()
#         else:
#             print("bye")
#
#     def create_pin(self):
#         self.pin = input("enter your pin:")
#         print("pin set successfully")
#
#     def deposit(self):
#         value = input("enter the pin:")
#         if value == self.pin:
#             amount = int(input("enter the amount you want to deposit:"))
#             self.balance = self.balance + amount
#             print("Deposit successfully")
#         else:
#             print("invalid pin")
#
#     def withdrawn(self):
#         value = input("enter the pin:")
#         if value == self.pin:
#             amount = int(input("enter the amount you want to withdrawn:"))
#             if amount < self.balance:
#                 self.balance = self.balance-amount
#                 print("operation successful: balance after withdrawn is ", self.balance)
#             else:
#                 print("invalid balance")
#         else:
#             print("invalid pin")
#
#     def check_balance(self):
#         value = input("enter the pin:")
#         if value == self.pin:
#             print("check balance:", self.balance)
#         else:
#             print("invalid pin")


# sbi = Atm()
# hdfc = Atm()
# hdfc.deposit()
# sbi.deposit()
# sbi.withdrawn()
# sbi.check_balance()
# class mai object hi self hota hai
# ekk method apna hi clas  s ka dusara method ko access nhi kar sakta hai
# self is the current object


# # program to show magic  method (__str__)

class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.deno = d

    def __str__(self):
        return "{}/{}".format(self.num, self.deno)

    def __add__(self, other):
        temp_num = self.num * other.deno + other.num * self.deno
        temp_deno = self.deno * other.deno
        gcd_val = self.gcd(temp_num, temp_deno)
        simplified_num = temp_num // gcd_val
        simplified_deno = temp_deno // gcd_val
        return Fraction(simplified_num, simplified_deno)

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    def __sub__(self, other):
        temp_num = self.num * other.deno - other.num * self.deno
        temp_deno = self.deno * other.deno
        return "{}/{}".format(temp_num, temp_deno)

    def __mul__(self, other):
        temp_num = self.num*other.num
        temp_deno = self.deno*other.deno
        return "{}/{}".format(temp_num, temp_deno)

    def __truediv__(self, other):
        temp_num = self.num * other.deno
        temp_deno = self.deno * other.num
        return "{}/{}".format(temp_num, temp_deno)


x = Fraction(2, 8)
y = Fraction(2, 8)
print(x)  # Output: 2/8
print(y)  # Output: 2/8
print(x + y)  # Output: 1/2
print(x-y)
print(x*y)
print(x/y)


# l = [1, 2, x]
# print(l)
# print(type(l))




