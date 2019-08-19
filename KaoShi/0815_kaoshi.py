#  coding:utf-8

# sum = 0
# for i in range(2,101):
#     flag = True
#     for j in range(2,i):
#         if i % j == 0:
#             flag = False
#             break
#     if flag:
#         sum += i
# print(sum)



# year = int(input('year:\n'))
# month = int(input('month:\n'))
# day = int(input('day:\n'))
#
# months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# if 0 < month <= 12:
#     sum = months[month - 1]
# else:
#     print ('data error')
# sum += day
# leap = 0
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     leap = 1
# if (leap == 1) and (month > 2):
#     sum += 1
# print ('it is the %dth day.' % sum)


# fz = 2
# fm = 1
# sum_1 = 0
# for i in range(20):
#     sum_1 += fz / fm
#     t = fz
#     fz = fz + fm
#     fm = t
# print(sum_1)

