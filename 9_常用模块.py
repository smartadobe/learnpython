# import time
# # time.time()返回的是时间戳,可用于时间计算
# timestamp = time.time()
# print(timestamp)
#
# #time.localtime()返回的是结构化时间
# lctime = time.localtime()
# print(lctime)
# print(time.localtime(time.time()))
#
# # time.strftime()返回的是格式化的时间，按住ctrl点击函数名字，可以进模块查看函数
# strftime = time.strftime('%Y-%m-%d',lctime)
# print(strftime)
#
# a = time.strptime('2021-04-23 21:34:30','%Y-%m-%d %H:%M:%S')
# print(a)
# import random
# b  = random.choice([1,2,'aa',3,4,5])
# print(b)
import os

print(os.getcwd())
