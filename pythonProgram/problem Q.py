# number = int(input("enter any number:"))
# if 2 <= number <= 5:
#     print("weird number")
# elif number%2 == 0:
#     print("not weird")
# else:
#     print("weird number")





    # def is_leap(year):
    #     leap = True
    #
    #     # Write your logic here
    #     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    #         return leap
    #     else:
    #         return False
    #
    #
    # year = int(input())
    # print(is_leap(year))

# program to implement count()method......
# a = []
# for i in range(5):
#     x = input("Enter the number:")
#     a.append(x)
# x = input("enter the number to find Frequency of element:")
# b=a.count(x)
# print("Frequency of ", x ,"is=",b)
#
# # program to implement index() method....
# a = []
# for i in range(5):
#     x = input("enter the elements you want to add in a list:")
#     a.append(x)
# x = input("enter element to find the index:")
# b = a.index(x)
# print("index of the given element",x,"is=",b)
#
# # program to implement insert()method
# a =[]
# for i in range(3):
#     x = input("enter the Element:")
#     a.append(x)
# print("original list is:",a)
# index =int(input("enter index where you want to insert:"))
# value = input("enter value to insert:")
# a.insert(index,value)
# print("List after insertion:",a)
#
# # program to implement reverse()method
# a =[]
# for i in range(4):
#     x = input("enter elements to reverse:")
#     a.append(x)
# print("original list is:",a)
# a.reverse()
# print("After reversing the list:",a)





 # # program to use all function of list...
# a =[]
# x = int(input("enter the max size for the list:"))
# for i in range(x):
#     val = input("enter elements according to your choice:")
#     a.append(val)
# print("The original list are:",a)
# print("length of the given list:",len(a))
# print("maximum element in a list:",max(a))
# print("minimum element in a lst:",min(a))
# b=a
# print("contant of list b is:",b)
# print("contant of list a is:",a)
# z = input("enter the value to find frequency:")
# x = a.count(z)
# print("frequency of element is:",x)
# c = input("enter element to find index:")
# b = a.index(c)
# print("index of given element is:",b)
# val = input("enter value to insert :")
# ind = int(input("enter index where you want to insert:"))
# a.insert(ind,val)
# print("after inserting the given value in the list:",a)
# val = input("enter value to remove from the list:")
# a.remove(val)
# print(a)
# print("original list is:",a)
# a.reverse()
# print("list after reverse:",a)
# a.sort()
# print("list after sorting is:",a)
# print("last element popped:",a.pop())



#----LIST COMPREHENSION-----

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     a =[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k!=n)]
#     print(a)

#     ---------------------without list comprehension-------

# x = int(input())
# y =int(input())
# z = int(input())
# n = int(input())
# ls =[]
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if(i+j+k!=n):
#                 ls.append([i,j,k])
# print(ls)

#         -----------------nested list-----------------
# n = int(input())
# res = []
# grade = []
# for i in range(n):
#     name=input()
#     marks=float(input())
#     res.append([name,marks])
#     grade.append(marks)
# print(res)
# print(grade)
# grade = sorted(set(grade))
# m = grade[1]
# print(m)
# name =[]
# for val in res:
#     if(m==val[1]):
#         name.append(val[0])
# print(name)
# name.sort()
# for nm in name:
#     print(nm)
# -------------------maximum value in nested list--------------------
# list2 =[]
# def get_max(list1):
#     for i in list1:
#         if type(i)==list:
#             get_max(i)
#         else:
#             list2.append(i)
#     return max(list2)
#
#
# list1 = [7,9,[12,5,[30,15],17,2],7]
# print(get_max(list1))
# n = int(input("enter total  number of students for dictionary length: "))
# dic = {}
# for i in range(n):
#     name = input("enter the name of student:")
prime_number = int(input("enter the number to check whether it's a prime number or not: "))
for i in range(2,prime_number):
    if prime_number % i== 0 :
        print("not a prime number")
        break
else:
    print(f" {prime_number} is a prime number")
# for i in range(1,10+1):
#     print(i)









