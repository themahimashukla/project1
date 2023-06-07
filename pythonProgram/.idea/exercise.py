# 1. program to make simple calculator using variable and operator...
# a = int(input("enter first value:"))
# b = int(input("enter second value:"))
# print("addition:",a+b)
# print("substraction:",a-b)
# print("multiplication:",a*b)
# print("division:",a/b)
# print("exponent:",a//b)

# 2.program to print greetings(good morning/good night etc) using time module..
# import datetime
# x = datetime.datetime.now()
# print(x)
# helps to print current date and time
# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)

# 3.
# import time
# str = input("enter your name:")
# timestamp = time.strftime('%H:%M:%S')
# hours = int(time.strftime('%H'))
# minutes = int(time.strftime('%M'))
# sec = int(time.strftime('%S'))
# print("current time:",timestamp)
# if(6==hours or hours<=11 and minutes<=59 and sec<=59):
#     print("Good Morning",str.capitalize())
# elif(12==hours or hours<=16 and minutes<=59 and sec<=59):
#     print("Good Afternoon",str.capitalize())
# elif(17==hours or hours<=21 and minutes<=59 and sec<=59):
#     print("Good Evening",str.capitalize())
# else:
#     print("Good Night",str.capitalize())

# 4. program to play KBC in python..
# ls = ["Who is bts?","how many members are their in bts?","Name the most popular one?"]
# print(ls[1])
# ans1 = input("enter answer:")
# score = 0
# if(ans1=="7"):
#     score = score+10
#     print("right answer '10 points are added'")
# else:
#    print("wrong answer..")
# print(ls[0])
# ans2 = input("enter sec answer:")
# if(ans2=="boy band"):
#     score = score+10
#     print("right answer '10 points are added'")
# else:
#     print("wrong answer..")
# print(ls[2])
# ans3 = input("enter final answer:")
# if(ans3=="kim taehyung"):
#     score = score+10
#     print("Right answer'10 points are added'")
# else:
#     print("wrong answer..")
# print("GrandTotal=",score)

# ---------------------------------OR------------------
# question = [["which language was used to create facebook?","python", "French", "javascript", "php", "None",4],"\n"
#             ["which language was used to create facebook?","python", "French", "javascript", "php", "None",4] ,"\n"
# ["which language was used to create facebook?","python", "French", "javascript", "php", "None",4], '\n'
# ["which language was used to create facebook?","python", "French", "javascript", "php", "None",4]
# ]
# levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
# i = 0
# print(levels[i])
# i = 0
# for i in range(0,len(questions)):
#     question = question[i]


# question = [["which language was used to create facebook?", 'python', 'javascript','php', 'none', 2]
#              ["what is the capital of india?","mumbai","delhi","noida","punjab",1]]
            # ["womens day is celebrated on which month?",'may','march','june','april',1],"\n"
            # ["what is the national bird of india?","peacock",'hen','ostrich','woodpeaker',0],'\n'
            # ["what is the national animal of india ?",'tiger','lion','cheetah','monitorlizard',0],'\n'
            # ["how many states are there in india?",'23','45','22','28',3],'\n'
            # ['who is bts?','boy band','girl band','behind the scene','none',0],'\n'
            # ["which language was used to create facebook?", 'python', 'javascript','php', 'none', 2],
            # ]
# levels = [1000,2000,4000,5000,10000,50000,100000,3200000]
# for i in range(len(levels)):
#     print(i)

