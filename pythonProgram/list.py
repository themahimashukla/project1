#  1.list basic
a = ["mahima",10,20.5,"ram"]
print(a)
print(a[2])
print(a[-1])
print(a[-3])
a[1]="shukla"
print(a)
# ---------DONE-------------

#2. list slicing
a = ["ram",20,"mahima",12.5,'hello']
print(a)
print(a[:])
print(a[0:])
print(a[1:3])
print(a[:3])

# -----------DONE----------

#3. updating list in python
a=[10,20.4,'mahima','hello']
print(a)
a[3] ="shukla"
print(a)
a[1]="hello"
print(a)

# deleting list values in python
del a[2]
print(a)
del a[0]
print(a)

# --------DONE----------

# 4.traversal or accessing items in list
a = [10,'ram',20.5,'mahima','hello']
a[3]='shukla'
for i in a:
    print(i)
print(len(a))

# -------------DONE----------------------

# 5. list function in python
# 1.len( ) = length of list........
a = [10,20.3,"mahima",55,"hello"]
b = len(a)
print("Length of the given list:",b)

c =["mahima",10.2,"ten",29,"namaste",44]
print("Length of the given list:",len(c))

# 2.max( )
a = [10,20,30,40,66.70]
b = max(a)
c = len(a)
print("maximum number in list:",b)
print("Length of the given list:",c)

# 3.min( )
a =[20.2,20.1,30,40,50,60,70]
b = min(a)
print("minimum number in then list:",b)

c =[60.1,33,22,44,1,2,3,4,0.1]
print("min in list:",min(c))

# 4.list.append
# a=[]
# for i in range(5):
#     x =int(input("enter number:"))
#     a.append(x)
# print(a)

# 5. count( )
a = ["mahima",10,20,"mahima","prince"]
x = a.count("mahima")
print("Frequency is:",x)

# 6.index()
a = ["ram","mahima","ram","shyam"]
x = a.index("ram")
print("index of ram is:",x)

# 7.insert()
a = [3,"mahima","hi",10]
a.insert(2,"shukla")
print(a)

# 8. remove function()
a =["ram",10,"shyam",10]
a.remove(10)
print(a)

# 9.reverse()
a =[2,"mahima",3,4,"ram"]
a.reverse()
print(a)

# 10.pop()
a =[1,2,3,4,5]
a.pop()
a.pop()
print(a)


# ---------QUESTIONS ON LIST ONLY-------------
#  1.sum of elements of a list
# a = []
# size = int(input("enter size for the list"))
# for i in range(size):
#     x = int(input("enter number:"))
#     a.append(x)
# sum = 0
# for i in range(size):
#     sum = sum+a[i]
# print("total sum of given list are:",sum)

# 2. count total number of odd and even numbers in a list.....
# a =[]
# size = int(input("enter no.for the size of your list:"))
# for i in range(size):
#     x = int(input("enter numbers :"))
#     a.append(x)
# even = 0
# odd = 0
# for i in range(size):
#     if(a[i]%2==0):
#         even = even+1
#     else:
#         odd = odd+1
# print("Total number of even=", even)
# print("Total number of odd=", odd)

# 3.program to search a number in a list..........
# a = []
# size = int(input("enter the size of the list:"))
# for i in range(size):
#     val =int(input("enter values:"))
#     a.append(val)
# key = int(input("enter the value you want to search in the list:"))
# flag =0
# for i in range(size):
#     if(a[i]==key):
#         flag = 1
#         pos = i+1
#         break
# if(flag==1):
#     print("element found at:",pos,"position")
# else:
#     print("element not found")

# 4.program to count the frequency of a number.....
# a=[]
# size = int(input("enter the size of the list:"))
# for i in range(size):
#     s =int(input("enter the values:"))
#     a.append(s)
# z = int(input("enter the element whose frequency u want to find:"))
# for i in range(size):
#     b=a.count(z)
# print("Frequency of the given number is:",b)

# ----------------------OR---------------------------
# a =[]
# size =int(input("enter size of list:"))
# for i in range(size):
#     val = int(input("enter the elements:"))
#     a.append(val)
# key =int(input("enter number to find frequency:"))
# count =0
# for i in range(size):
#     if(a[i]==key):
#         count=count+1
# print("frequency=",count)

#5. program to find max and min in the list.........
# a =[]
# size = int(input("enter the size of the list:"))
# for i in range(size):
#     val = int(input("enter the elements:"))
#     a.append(val)
# # for i in range(size):
# print("maximum value in the list are:",max(a))
# print("minimum value in the list are:",min(a))

# ----------------------------------OR-------------------------
# maximum'
# a = []
# size = int(input("enter the size of the list:"))
# for i in range(size):
#     v = int(input("enter the elements:"))
#     a.append(v)
# max=a[0]
# for i in range(size):
#     if(a[i]>max):
#         max=a[i]
# print("maximum value in the list are:",max)

# minimum'
# a=[]
# size = int(input("enter the size of the list:"))
# for i in range(size):
#     v = int(input("enter the elements:"))
#     a.append(v)
# min=a[0]
# for i in range(size):
#     if(a[i]<min):
#         min = a[i]
# print("minimum value in the list are:",min)

# 6.program to reverse the list............
# a=[]
# size = int(input("enter the size of the list:"))
# for i in range(size):
#     x= int(input("enter the elements:"))
#     a.append(x)
# i = 0
# j=size-1
# while(i<j):
#     t=a[i]
#     a[i]=a[j]
#     a[j]=t
#     i=i+1
#     j=j-1
# print("list after reverse=")
# for i in range(size):
#     print(a[i])


# program to find second minimum number.........
# a =[]
# size = int(input("enter the number of elements you want in a list:"))
# for i in range(size):
#     x = int(input("enter the elements:"))
#     a.append(x)
# firstmin = min(a)
# print("lowest minimum number are:",firstmin)
# a.remove(firstmin)
# sec_min = min(a)
# print("second minimum number are: ",sec_min)

# -----------------------------------OR-------------------
# a =[]
# size=int(input("enter number for the size of list="))
# for i in range(size):
#     x = int(input("enter the elements in a list="))
#     a.append(x)
# a.sort()
# print("lowest minimum number=",a[0])
# print("second minimum number=",a[1])

# # program to insert a number at given index in an list........
# a =[]
# size = int(input("Enter the number for the size in a list:"))
# for i in range(size):
#     x =int(input("enter the elements:"))
#     a.append(x)
# print("The original list are=",a)
# val = int(input("enter the number to insert="))
# ind = int(input("enter the number for index in the list:"))
# # for i in range(size):
# a.insert(ind,val)
# print("after inserting the number on the given index:",a)

# .............list comprehension.......
# square =[]
# for i in range(1,101):
#     square.append(i**2)
# print(square)

# -------or--------------------
# squares =[i**2 for i in range(1,101)]
# print(squares)

# s =[]
# for i in range(1,11):
#     s.append(i*i)
# print(s)

# ----------------------OR-------------------------
# s = [i*i for i in range(1,11)]
# print(s)

# ls =[]
# for i in range(100):
#     if(i%3==0):
#         ls.append(i)
# print(ls)

# ls =[i for i in range(1,101) if(i%3==0)]
# print(ls)

# ----Nested Lists in python----------


# print("""hi !
# how are you my friend""")
# print("hi!my name is'mahima'")


# -------------2D LIST--------------
# drink = ['coffee','mango shake','tea']
# dinner = ['pizza','burger','pasta']
# dessert = ['ice cream','cake']
# food = [drink,dinner,dessert]
# print(food)
# print(food[0][2])
#
# li=[10,40,30,[56,34,22]]
# print(li[2])


# a =[10,20,30,[40,50]]
# print(a[2])
# print(a[3][1])
# a[3][0]=77
# a[1]=82
# a.sort()
# print(a)

# n =int(input())
# ls =[]
# for i in range(n):
#     ls1=input()
#     ls2=input()
#     ls.append([ls1,ls2])
# print(ls)
# for i in ls:
#      i.sort()
# print(ls)
# # sorted(ls)
# print(max(ls))
# print(max(ls[1]))


# ----------------------program for nested list maximum number--------------

# n = int(input("number:"))
# ls =[]
# res =[]
# ress=[]
# for i in range(n):
    # ls1 = int(input())
    # ls2 = int(input())
    # ls.append([ls1,ls2])
    # res.append(ls1)
#     ress.append(ls2)
# a = max(res)
# b = max(ress)
# print(ls)
# print(a)
# print(b)
# if(a>b):
#     print("maximum number:",a)
# else:
#     print("maximum number:",b)

# ls = []
# size = int(input("enter size for list :"))
# for i in range(size):
#     val = int(input("enter value:"))
#     ls.append(val)
# # max =ls[0]
# # for i in range(size):
# #     if(ls[i] > max):
# #         max = ls[i]
# first_maximum = max(ls)
# ls.sort()
# ls.remove(first_maximum)
# print("second minimum:",ls[1])
# print("second maximum",max(ls))
# # print("maximum value:",max)
# # print("minimum value",min(ls))

# ls = []
# size = int(input("enter number:"))
# for i in range(size):
#     val = int(input("enter numbers:"))
#     ls.append(val)
# max = 0
# for i in range(size):
#     if(ls[i]>max):
#         max = ls[i]
# print("maximum number :",max)
# l = [2,3,4,5,6,9]
# print(l)
# m = l.copy()
# m = l
# m[0] = 4
#
# print(l)
# ls = ["Who is bts?","how many members are their in bts?","Name the most popular one?"]
for i in ['Red','yellow']:
    for j in ['Apple']:
        for k in['pink']:
            print(i,'=',j,'and',k)
