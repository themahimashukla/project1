# class Student:
#
#     def __init__(self):
#         self.student = []
#         self.name = []
#         self.menu()
#
#     def menu(self):
#         user_display = input("""hello here some options are available to choose:
#         1.enter add to add new student detail:
#         2.enter verify to verify if a particular student present or not:
#         3.enter verify all to see student whole info:
#         4.to exit enter E:
#         """)
#         if user_display == "add":
#             self.add()
#         elif user_display == "verify":
#             self.verify()
#         elif user_display == "verify all":
#             self.verify_all()
#         else:
#             print("bye!")
#
#     def add(self):
#         self.student = []
#         self.name = []
#         user_input = int(input("enter the number of students you want to add:"))
#         for i in range(user_input):
#             name = input("enter name:")
#             id = int(input("enter Id in numbers:"))
#             age = int(input("enter age:"))
#             self.name.append(name)
#             self.student.append([name, id, age])
#         print("successfully added")
#         # print(student)
#
#         self.menu()
#
#     def verify(self):
#         user_input = input("enter the student name to verify details:")
#         if user_input in self.name:
#             print("Details found")
#         else:
#             print("Details not found")
#
#         self.menu()
#
#     def verify_all(self):
#         for i in self.student:
#             print("student name,id,age is:", i)
#
#
# s = Student()
#


class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)

    def verify(self, name):
        return self.name == name


students = []

student1 = Student("mahi", 20, "A+")
students.append(student1)

student2 = Student("Alice", 21, "A+")
students.append(student2)

student3 = Student("Harry", 15, "A+")
students.append(student3)


# for student in students:
#     student.display()
#     print()
#
# Name = "Harry"
#
# for student in students:
#     if student.verify(Name):
#         print(f"{Name} is present in the student list")
#         break
# else:
#     print(f"{Name} is not present in the student list")

class Book:

    def __init__(self, title, author, p_year):
        self.Title = title
        self.Author = author
        self.p_year = p_year

    def display(self):
        print("Title:", self.Title)
        print("Author:", self.Author)
        print("Publication year:", self.p_year)

    def search_book(self, title):
        return self.Title == title


books = []

book1 = Book("journey to west", "john", 1980)
books.append(book1)

book2 = Book("yamada 999 level", "luffy", 2000)
books.append(book2)
for book in books:
    book.display()
    # print()
title = "yamada 999 level"


# for book in books:
#     if book.display(title):
#         print(f"{title} is found in the books catalog")
#         break
# else:
#     print(f"this {title} title name book is not found")


class Student:
    students = []

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade", self.grade)

    @classmethod
    def add_student(cls):
        name = input("Enter the name:")
        age = int(input("Enter the age:"))
        grade = input("Enter the grade:")
        stu = cls(name, age, grade)
        cls.students.append(stu)


num_student = int(input("enter the number of students you want to add:"))

for _ in range(num_student):
    Student.add_student()

for student in Student.students:
    student.display()
    print()

# def add_to_cart(self):
    #     count = 0
    #     num = int(input("Enter number of elements to add in cart:"))
    #     for i in range(num):
    #         product = input("Enter the product to add in cart:")
    #         count += self.list.count(product)  # Use count method to count occurrences
    #     print(f"...{count} Iteams found in a cart...")
