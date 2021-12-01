# -*- coding:utf-8 -*-
# Author：Wyss
# File:demo4.py
# Date:2021/5/21 16:20

# Python程序三大结构：顺序结构、选择结构、循环结构

# =====>>> 条件判断：
# ----语法：
# if语句
# if 判断条件（表达式）：
#     代码块

# if else语句
# ----语法：
# if 判断条件（表达式）：
#     代码块
# else：

# if elif else语句
# ————语法：
# if 判断条件（表达式）：
#     代码块
# elif 判断条件（表达式）：
#       代码块
# else：


# chengji = int(input("请输入成绩："))
# if chengji >= 80:
#     print("优秀")
# elif chengji >= 60:
#     print("良好")
# elif chengji >= 50:
#     print("一般")
# else:
#     print("差")

# elif 相当于 else if ,可以有多个

# if的嵌套
# if 判断条件（表达式）：
#     if 判断条件（表达式）：
#         代码块
#     elif 判断条件（表达式）：
#           代码块
#     else:
# elif 判断条件（表达式）：
#     代码块
# else:

"""
chengji2 = int(input("请输入成绩："))
if chengji2 >= 60:
    print("及格")
    if chengji2 >= 90:
        print("优秀")
    elif chengji2 >= 80:
        print("良好")
    else:
        print("一般")
else:
    print("不及格")
"""

# =====>>> 循环语句：while   for
# while循环:
# for循环
# do while： Python没有这个语法

# while 条件表达式（循环变量的判断）：
#     代码块（循环体）

# 条件为真时，执行循环体
# 条件为假，跳出循环

# 实例：
# n = 10
# while n > 0:
#     n = n-1
#     print(n)
# else:
#     print("end")

# 实例：实现1+2+3+4+……+100
# i= 0
# sum = 0
# while i <= 100:
#     sum = sum + i
#     i= i + 1
#     print(i,sum)
# else:
#     print(sum)

# while循环可以与else语句同时使用
# i= 0
# sum = 0
# while i <= 10:
#     sum = sum + i
#     i= i + 1
#     print(i,sum)
# else:
#     print(sum)

# 遍历整个字符串,并连接在一起end=
# str1 = "http://www.baidu.com/"
# j = 0
# while j <len(str1):
#     print(str1[j],end="")
#     j = j + 1


# =====>>> for循环
# 用来遍历字符串、列表、元祖、字典、集合等序列类型，可以逐个获取序列中的各个元素
# 语法：
# for 迭代变量 in 序列：
#     代码块
# 实例：
# list1 = ["aaa","bbb","eee",23]
# for x in  list1:
#     print(x)
#
# str2 = "http://www.baidu.com"
# for a in str2:
#     print(a,end="-")
# else:
#     print("不存在")

# 实例：计算1+2+3+……10的值
# range(x)函数，提供了一个整数序列，从0开始到小于x的值
# sum = 0
# for y in range(11):
#     sum = sum + y
# print(sum)


# while循环、for循环的使用
# 遍历某个序列时，用for
# 其他则用while
# 一般能用for循环时，一定能用while循环，反过来则不一定
# 当知道循环次数时，用for，不知道循环次数时，用while

# =====>>> 循环嵌套
# k = 0
# while k <10:
#     for l in range(10):
#         print("k=",k,"l=",l)
#     k = k + 1

# 实例：打印出如下图案（共5行）
# *
# **
# ***
# ****
# *****

# 第一种方法：
# for w in range(1,6):        # 五行
#     for e in range(0,w):    # 定义行数，在每一行输出
#         print("*",end="")   # 输出每一行的*，不换行
#     print()                 # 打印空行

# 第二种方法：
# row = 1
# while row < 5:
#     col = 1
#     while col < row:
#         print("*",end="")
#         col += 1
#     print("*")
#     row += 1


# =====>>> break、coutinue、pass的区别
# break:跳出整个循环
# continue：跳出本次循环
# pass：空语句，占位语句,可为后续完善功能预留

# 当i 为 h 时，停止循环，但继续执行后面的代码：
# str11 = "nihaoshijie"
# for i in str11:
#     if i == "h":
#         continue
#     print(i,end="")

# i = 0
# while i < 10:
#     if i == 3:
#         i = i + 1  #(当上面满足条件，则执行此栏)
#         continue
#     i += 1
#     print(i)

# 当 i 为 h时，退出循环，停止运行：
# str12 = "nihaoshijie"
# for i in str12:
#     if i == "h":
#         break
#     print(i,end="")
#
# # 打印所有字符
# str13 = "nihaoshijie"
# for i in str13:
#     if i == "h":
#         pass
#     print(i,end="")


# for循环
# 集合：元祖、列表、字典
"""
格式：
for 变量名 in 集合：
    循环体
"""

# range(开始值，结束值) 左闭右开
# for i in range(5):
#     print("hello")

# while循环，不知道循环次数
# for循环，知道循环次数，集合