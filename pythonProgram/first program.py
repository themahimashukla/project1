# python code for "Hello world"
# nothing else to type......see how simple is the syntax.

# print("hello world" , "my name is mahima")
# print(40<20)

# Python program to declare variables
# myNumber = 3
# print(myNumber)

# myNumber2 = 4.5
# print(myNumber2)

# myNumber3 ="Hello world"
# print(myNumber3)

# python program to illustrate a list

# creates empty list
# nums = []
# course = []
# appending data in list
# nums.append(199)
# nums.append(66.8)
# nums.append("Mahima shukla")
# course.append("my first program in python")
# course.append("2 month")
#
# print(nums)
# print(course)
# b="hello mahima"
# print(b,type(b))
#
# s='''
# hello everyone!
# my name is mahima
# '''
# print(s)
#
# l=[19,66,"mahi"]
# l[2]="mahima"
# print(l,type(l))
#
# t=(7,9,78)
# print(t,type(t))
#
# d={
#     "name":"mahima",
#     "height":"4.9",
# "age":"19"
# }
# print(d)
#
#
# s={10,50,10,80}
# print(s)
#
# import keyword
# print("the list of keywords are:")
# print(keyword.kwlist)
#
#
#
# first_name ="mahima"
# last_name ="shukla"
# full_name = first_name+' '+last_name
# print("hello "+full_name)

age = 19
age += 1
print(age)
print("my age is:"+str(age))

# Boolen
# human = True
# print("Are u a human :",str(human))

# multiple-assigments
name,age,height = "mahima",20,4.9
print(name)
print(age)
print(height)

# important string
# name = "mahima"
# print(len(name))
# print(name.capitalize())
# print(name.find("a"))
# print(name.upper())
# print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("a"))
print(name.replace("a","o"))
print(name*2)

y = 4.7
y = str(y)
print(y*5)

# tyle casting
# name = input("what is your name:")
# print("Hello!"+name)
# age = int(input("how old are you:"))
# age = age+1
# print("you are :"+str(age)+"years old")
# # print("you are :"+int(age)+"years old")
# height = 4.9
# print("my height is :"+str(height))


# math function
# import math
# pi = 3.14
# print(pow(pi,2))
# print(abs(pi))
# print(math.ceil(pi))
# print(round(pi))
# print(math.floor(pi))
# print(math.sqrt(420))
# x=5
# y=8
# z=80
# print(max(x,y,z))
# print(min(x,y,z))

# string-Silicing
# w = http:\\google.com
# print()

# number = int(input("enter any number:"))
# if 2 <= number <= 5:
#     print("weird number")
# elif number%2 == 0:
#     print("not weird")
# else:
#     print("weird number")

# logical operator
# age = int(input("what is your age! :"))
# if age >= 13 and age <= 18:
#     print("you are a teenager")
#     print("not allowed to drive")
# # elif age >= 19 or age <= 25:
# #     print("you are an adult")
# #     print("you can drive")
# elif not(age >= 19 or age <= 25):
#     print("you are a adult")

# n = int(input("enter number:"))
# for i in range(0,n):
#     print( pow(i,2))
# n = int(input("enter number:"))
# i=1
# while(i<=n):
#     print(i)
#     i=i+1

# function
# def_message:print("hello python")
# def_message()

# def add():
#     a = int(input("enter number:"))
# b = int(input("enter 2nd number"))
# c = a+b
# print(c)
# add()

# def is_leap(year):
#  year = int(input("enter a year:"))
#  if (year%400 == 0) or (year % 4 == 0 and year %100 !=0):
#       print(True)
#  else:
#       print(False)
# is_leap("year")
# is_leap("year")
# is_leap('year')


# year = int(input("enter year:"))
# def is_leap(year):
#     # year = int(input("enter year:"))
#     if (year%400==0) or (year%4==0 and year%100 !=0):
#         print(True)
#     else:
#         print(False)
#         # year = int(input("enter year:"))
#         is_leap(year)

# def namaste(name):
#
#     print("hello "+name)
#     print("namaste")
# namaste("mahima")
# # namaste()
# # namaste()

#   no argument no return
# def add():
#     a = int(input("enter first number:"))
#     b = int(input("enter second number"))
#     c = a+b
#     print(c)
# add()
# print("program complete successfully")

# with argument no return
#  
#     c= a+b
#     print("addition",c)
# x = int(input("enter no:"))
# y = int(input("enter no:"))
# add(x,y)

# def is_leap(year):
#     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         print(True)
#     else:
#          print(False)
# year = int(input("enter year:"))
# is_leap(year)

# name = input("enter your name:")
# print("hello",name)


# a = str(input("enter your name:"))
# print(a)
# b = int(input("enter your age:"))
# # print(b)
# if(b>18):
#     print("name",a,"is eligible to vote")
# else:
#     print("name",b,"is not eligible to vote")

# print("enter your name")
# name = input()
# print("enter your age")
# age = int(input())
# if(age>18):
#     print("can vote")
# else:
#     print("cannot vote")


# <<<< --------------docstrings--------->>>
# def func():
#     """
#     this function prints greeting
#     """
# print("hi")
# func()
# print(func.__doc__)

# def add():
#     """
#     this function used to add values
#     """
# print(4+2)
# print(add.__doc__)



#simple-calculator

# print("enter two number:")
# a =int(input())
# b = int(input())
# opr =input("enter operator(+,-,/,*):")
# if(opr=='+'):
#     print(a,opr,b,'=',a+b)
# elif(opr=='-'):
#     print(a,opr,b,'=',a-b)
# elif(opr=='*'):
#     print(a,opr,b,'=',a*b)
# elif(opr=='/'):
#     print(a,opr,b,'=',a/b)
# else:
#     print("NOT A VALID OPERATOR.........")


# <<<<<<TUPLE>>>>>>
tup = (3, 4, 5, "mahima", 22, 12)
print(type(tup),tup)
print(tup[0])
print(tup[3])
if "mahi" in tup:
    print("yes Name Mahi is present....")
tup2 = tup[1:4]
print(tup2)

# <<<<<<<METHODS OF TUPLE>>>>>>>>
# hacker rank question(....Finding the percentage using dict....)
n = int(input("enter the number of students:"))
dic = {}
for i in range(n):
    name = input("enter name:")
    m = []
    print("enter three values as marks")
    for j in range(3):
        marks = int(input())
        m.append(marks)
    dic.update({name: m})
print(dic)
specific_name = input("enter the name whose marks average you want to find:")
for i in range(len(specific_name)):
    s = sum(m)/len(m)
rn = round(s*100.00)/100.00
print(rn)




