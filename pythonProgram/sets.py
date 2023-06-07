s = {2, 4, 5, 6, 2}
print(type(s))

mahi = set()
print(type(mahi))
info = {"hello", 23, 50.67, "Good"}
for value in info:
    print(value)

# SETS METHOD----(UNION)---
s1 = {2, 4, 5, 6}
s2 = {6, 7, 8}
# print(s1.union(s2))
s1.update(s2)
print(s1)
# ---INTERSECTION---
citty = {"jalandhar", "delhi", "punjab"}
citty2 = {"jalandhar", "ludhiana"}
print(citty.intersection(citty2))
citty.intersection_update(citty2)
print(citty)
# symmetric difference(print not common values/remove intersection )
citty = {"jalandhar", "delhi", "punjab"}
citty2 = {"jalandhar", "ludhiana", "delhi"}
print(citty.symmetric_difference(citty2))
# difference(print only set A which not present in B)
citty = {"jalandhar", "delhi", "punjab"}
citty2 = {"jalandhar", "ludhiana", "delhi"}
print(citty.difference(citty2))

# in-built method of sets( isdisjoint())
citty = {"jalandhar", "delhi", "punjab"}
citty2 = {"jalandhar", "ludhiana", "delhi"}
print(citty.isdisjoint(citty2))
citty = {"seoul"}
citty2 = {"tokyo"}
print(citty.isdisjoint(citty2))
# isuperset()(B set is present in A set)
citty = {'jalandhar', 'mumbai', 'new-zealand'}
citty1 = {"jalandhar", 'mumbai'}
print(citty.issuperset(citty1))
# issubset()
# remove() and discard() are quite same but in case of discard no error are formed even the value is not present in set
citty = {'jalandhar', 'mumbai', 'new-zealand'}
citty.remove("new-zealand")
print(citty)
# pop()(this method help to remove last element from the set which can be random)
citty = {"jalandhar", "delhi", "punjab"}
print(citty.pop())
# del() remove entire set
citty = {'jalandhar', 'mumbai', 'new-zealand'}
citty1 = {"jalandhar", 'mumbai'}
del citty
print(citty1)

info = {"carla", 55}
if "carla" in info:
    print("carla is present ")
else:
    print("carla is absent")

# <<<<<<<Dictionary{}>>>>>>>>
dic = {56: "rachna", 446: "neha", 503: "prince"}
print(dic[446])
info = {'name':'Rachna', 'age': 19, "eligible": True}
print(info)
print(info['name'])
print(info.get('name3'))
# both are the ways to print in dictionary but with .get we will not get any error even the value is not present
print(info.keys())
print(info.values())
for key in info.keys():
    print(f"the value correspnding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"the value correspnding to the key {key} is {value}")

# <<<<----DICTINOARY METHODS--->>>>
ep = {212: 33, 432: 55, 111: 68}
ep2 = {456: 89, 332: 76, 908: 77}
ep.update(ep2)
print(ep)
# ep.clear()
# print(ep,ep2)
ep.pop(212)
print(ep)
D = {'name': "Rachna", 'Age': 19, "studying": "BCA", "Hobby": "Anime" }
print(D["Hobby"])
print(f"This is my dictionary:{D}")

# for loop with else
# for i in range(5):
for i in []:
    print(i)
else:
    print("Sorry no. i")
for i in range(6):
    print(i)
    if(i==4):
        break
else:
    print("sorry no i")
# else part wont execute

# <<----EXCEPTION HANDLING---->>
# a = input("enter number:")
# print(f"Multiplication table of {a} is:")
# try:
#   for i in range(1,11):
#      print(f"{int(a)} x {i}= {int(a)*i}")
# # except Exception as e:
# #     print(e)
# except:
#     print("invalid input!")
# print("some lines of codes start")
# print("code end here")

# try:
#     num = int(input("enter an integer:"))
# except ValueError:
#     print("Number entered is not an integer.")
#
# except IndexError:
#     print("Index Error")

# finally keyword..
# try:
#     l = [1, 4, 5, 6]
#     i = int(input("enter the index:"))
#     print(l[i])
# except:
#     print("some error occurred")
#
# finally:
#     print("always executed")

# def func1():
#     try:
#       l = [1, 4, 5, 6]
#       i = int(input("enter the index:"))
#       print(l[i])
#       return 1
#     except:
#        print("some error occurred")
#        return 0
#     finally:
#        print("always executed")
#
# x = func1()
# print(x)

# <<<-----custom error----->>
# a = input("enter any value between 5 and 9=")
# if(a=='quit'):
#     print("wow")
# elif(int(a)< 5 or int(a) >9):
#     raise ValueError("value should be between 5 and 9 and quit")
# print("hello")

# s = int(input("enter any value between 5 and 9="))
# if(s>5 and s<9):
#     print("right")

# <<<<---------short hand if else----->>>>
a = 330
b = 450
# print("A") if(a>b) else print('=') if(a==b) else print("B")
c = 9 if(a>b) else 0
print(c)

c = int(input("enter your age:"))
print("adult") if(c>18) else print("child")
