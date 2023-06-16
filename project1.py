class Student:

    def __init__(self):
        self.student_name = []
        self.student_grade = []

        self.student_class()
    def student_class(self):
        c = input("""Hello! here we can perform:
        1.Enter N to add student_name
        2.Enter add to add student_grade
        3.Enter avg to calculate_average
        4.Enter info to display student info
        """)
        if c == "N":
            self.s_name()
        elif c == "add":
            self.s_grade()
        elif c == "avg":
            self.calculate_avg()
        elif c == "info":
            self.display_info()
        else:
            print("Exist")

    def s_name(self):
        self.student_name = []
        s = int(input("enter number of new student you want to add:"))
        for i in range(s):
            name = input("enter the student name:")
            ID = int(input("enter the student ID:"))
            self.student_name.append([name, ID])
        print(self.student_name)

    def s_grade(self):
        self.student_grade = []
        n = int(input("enter the no. of students whose  grades you want to store:"))
        for i in range(n):
            s = input("enter name with grade and press space in between:")
            self.student_grade.append(s)

        print(self.student_grade)

    def calculate_avg(self):
        if len(self.student_grade) == 0:
            print("no grades available")
            return

        total_grade = 0
        for grade in self.student_grade:
            _, grade_value = grade.split()
            total_grade += int(grade_value)
        average = total_grade/len(self.student_grade)
        print("Average garde:", average)

    def display_info(self):
        if len(self.student_name) == 0:
            print("NO data available...firstly add students data")
        print("please add data related to id number and name")
        self.s_name()

        for name, ID in self.student_name:
            print("Name:", name)
            print("ID:", ID)





about = Student()
# about.s_name()
# about.s_grade()
# about.calculate_avg()
# about.display_info()