# class Employee_database:
#
#     employee = []
#
#     def __init__(self, name, ID, department):
#         self.name = name
#         self.id = ID
#         self.department = department
#
#     def display(self):
#         print("Name:", self.name)
#         print("Employee ID:", self.id)
#         print("Employee_Department:", self.department)
#
#     @classmethod
#     def add_employee(cls):
#         name = input("Enter the employee name:")
#         ID = int(input("Enter the employee id:"))
#         department = input("Enter the employee department:")
#         database = cls(name, ID, department)
#         cls.employee.append(database)
#
#     def search(self, user_input):
#         if self.department == user_input:
#             self.display()
#             print()
#             return 1
#         else:
#             print()
#             return 0
#
#     def remove_employee(self, user_input2):
#         if self.name != user_input2:
#             print(f"after deleting {user_input2} Employee details")
#             self.display()
#
#             return 1
#         else:
#             print()
#             return 0
#
# num_employee = int(input("Enter the number of employee you want to add:"))
# for _ in range(num_employee):
#     Employee_database.add_employee()
#
# for e in Employee_database.employee:
#     e.display()
#     print()
#
# found = 0
# user_input = input("Enter employee department:")
#
# for emp in Employee_database.employee:
#     found += emp.search(user_input)
#
# print("Number of employees found in the given department:", found)
# user_input2 = input("Enter the employee name you want to delete from Employee_database:")
# for name in Employee_database.employee:
#     name.remove_employee(user_input2)


class Book:
    books = []
    person = []
    available = "Yes"

    def __init__(self, name, title):
        self.Title = title
        self.Author = name

    def display(self):
        print("Author:", self.Author)
        print("Title:", self.Title)

    @classmethod
    def add_book(cls):
        name = input("Enter the author name :")
        title = input("Enter the title:")
        bye = cls(name, title)
        cls.books.append(bye)

    def search_book(self, user_input):
        if self.Title == user_input:
            self.display()
            print("Available_status:", Book.available)
            return 1
        else:

            return 0

    @classmethod
    def check_out(cls):
        user_input2 = input("Enter the book you want to borrow:")
        name = input("Enter your name:")
        date = int(input("Enter the date:"))
        per = cls(name, date)
        cls.person.append(per)
        book.display()
        available = "check_out"
        print("Available_status:", available)
        print("Please! return this book after 7 days")


num = int(input("Enter the number of books you want to add:"))
for _ in range(num):
    Book.add_book()

for book in Book.books:
    book.display()
    print()
found = 0
user_input = input("Enter the Book Title to search:")
for book in Book.books:
    found += book.search_book(user_input)

print(f"number of books with {user_input} Title found is:", found)
print(f"{user_input} book is not available to check out.....")
if found == 1:
    Book.check_out()
