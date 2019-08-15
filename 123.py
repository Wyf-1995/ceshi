# coding:utf-8
# a = str(input("请输入:"))
# if a>="A" and a<="Z":
#     print("是字母")
# elif a>="a" and a<="z":
#     print("是字母")
# else:
#     print("不是字母")


# while 1:
#     try:
#         t = int(input("工作时长"))
#         if t>160:
#             sum=160*30+(t-160)*30*1.5
#             print(sum)
#         elif t==160:
#             sum=160*30
#             print(sum)
#         else:
#             print("工作时长这么低，还想要工资，滚")
#     except:
#         print("输入错误")



# sum=0
# for m in range(2,101):
#     for i in range(2,m):
#         if m % i == 0:
#             sum+=m
#             break
# print ('The total is %d' %sum)


year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print ('data error')
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print ('it is the %dth day.' % sum)