# all about input function.......
# without int()
# this program use integer values as string only..and not perf
# a = input("Enter first number:")
# b = input("Enter second number:")
# c = a+b
# print("Addition",c)

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     arr.sort()
#     print(arr[(arr.index(max(arr))) - 1])

# <<<<<<<<<<<<<<<looping in python>>>>>>
# for i in range(100):
#     print("i love myself")
colors = ['red', 'green', 'blue', 'voilet']
for color in colors:
    print(color)
    for i in color:
        print(i)
# n = int(input('enter the number whose table u want to find='))
# for i in range(1,11):
#     print(n, '*', i, '=', i*n)

# <<<<<<<<<<<<<<<<while loop>>>>>>>>>>>>
# i = 0
# while(i<=3):
#     print(i)
#     i=i+1
# count = 5
# while(count>0):
#     print(count)
#     count = count-1
# else:
#    print("i am inside else")

# break and continue statement
for i in range(1,11):
    if (i == 11):
        break
    print("5 x",i,'=',5*i)



