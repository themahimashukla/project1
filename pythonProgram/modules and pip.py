#  modules helps to borrow someone's code.....
# pip helps to install the modules......
# import os
print("hello mahima")
# question:multiline
print("""
SONG LYRICS
Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
""")
# question print table
ls = [i for i in range(1, 31) if(i % 3 == 0)]
print(ls)

# --------escape sequence character(\n) for next line-----
print("Hi! My name is Mahima\nHow are u my friend")

# ----------variables and data types-----------
a = 34
print(type(a))
b = True
print(type(b))
a = 32
a1 = 4
print(a+a1)
print(a, a1)
b = "Mahima"
c = complex(8, 2)
print(c)
print(a, b)


# operators( arithmetic )
# print(5+6)
# print(6-4)
# print(4*4)
# print(10/2)
# print(5**3)
# print(5 % 3)
# print(15//6)

# typecasting()
a = "mahima"
b = "shukla"
print(a+b)
print(a, b)
c = "1"
d = "3"
print(c+d)
print(int(c)+int(d))
# EXPLICIT TYPECASTING(done by user acc. to his/her choice)
string = "55"
number = 5
string_number = int(string)
print(string_number+number)

# IMPLICIT TYPECASTING()
c = 1.9
d = 8
print(c+d)

# taking user input()
# a = input("enter your name:")
# print("my name is", a)


# strings in python
name = "mahima"
print(name[0])
print(name[1])
print(name[3])

# looping in string
# n = "apple"
for character in "apple":
    print(character)

# string slicing
# n = "mahima"
# print(len(n))
# print(n[:-3])
nm = "harry"
print(nm[-4:-2])

# string methods
a = "mahima"
print("length is:", len(a))
print(a.upper())
print(a.lower())
b = "!!rachna!!!!!!"
print(b.rstrip("!"))
c = "mahima!! !!m ahima"
# print(c.replace("mahima","rachna"))
print(c.split(" "))
blog_heading = "introduction to string in python"
print(blog_heading.capitalize())
print(a.count("mahima"))
a = "welcome3totheconsole"
print(a.isalnum())
print(a.isalpha())


# f-string in python...
letter = "Hey my name is {} and i am from {}"
country = "India"
name = "Mahima"
print(letter.format(name, country))
print(f"Hey my name is {name} and i am from {country}")

price = 49.0876
txt = "for only {price:.2f}dollars!"
# print(txt.format(price=49.08989))
print(f"for only {price:.2f}dollars!")
print(f"{2 *30}")

#  nested if else conditional
# num = int(input("enter value for num :"))
# if(num<0):
#     print("number is negative")
# elif(num>0):
#     if(num<=10):
#         print("number is present between 1-10")
#     elif(num>=11 and num<=20):
#         print("number lies between 11-20")
#     else:
#         print("number is greater than 20")
# else:
#     print("number is zero")


# match case in python.........
x = int(input("enter number(1-7) to find day:"))
match x:
    case 1:
        print("Today is Monday")
    case 2:
        print("Today is Tuesday")
    case 3:
        print("Today is wednesday")
    case 4:
        print("Today is Thrusday")
    case 5:
        print("Today is Friday")
    case 6:
        print("Today is saturday")
    case _:
        print("Today is Sunday")





#import array
# a = array.array('i',[1,2,3,4,56,7])
# a.insert(3,8)
# print(a)
# print(a[2])
