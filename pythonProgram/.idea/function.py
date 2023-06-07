# no argument no return....
# def oddeve(n):
#     if n % 2 == 0 :
#         print("given number is even")
#     else:
#         print("given number is odd")
# n = int(input("enter number:"))
# oddeve(n)

# QUESTON 2:
# def reverse(i):
#     rev = 0
#     while i > 0:
#         rev = (rev*10)+ i%10
#         i = i//10
#         print("reverse is:",rev)
# i = int(input("enter number:"))
# reverse(i)
#
# def isgreater(a,b):
#     if(a>b):
#         print("A is greater than B..")
#     else:
#         print("B is greater than A...")
# x = int(input("enter number:"))
# y = int(input("enter number"))
# isgreater(x,y)
#
# a =[10,20,30,[40,50]]
# print(a[2])
# # print(a[3][1])
# # a[3][0]=77
# # a[1]=82
# # a.sort()
# # print(a)
# c =2
# d =7
# isgreater(c,d)

# <<<<<<<<<<DEFAULT ARGUMENT>>>>
def average(a,b):
    print("average is:",(a+b)/2)
average(4,2)
# in case of default argument only value pass on calling is consider...

# <<<<<<<<<keywords arguments>>>>>>>>>
# does not bothered by order of value passed in an argument...
# def average(a,b):
#     print("average is:",(a+b)/2)
# average(b=4,a=2)

# <<<<<variable - lenght argument>>>>.
def average(*numbers):
    sum =0
    for i in numbers:
        sum = sum+i
    print("Average is :",sum/len(numbers))
average(2,4,6,8)
# with this argument i can calculate or find average of many numbers at once...

#  <----RECURSION----->
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# n = int(input("enter one number:"))
# print(factorial(n))

#FIBONACCI SSEQUENCE
a = int(input("enter number:"))
def fibonacci(n):
    if(n==1 or n==0):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(a):
    print(fibonacci(i))



