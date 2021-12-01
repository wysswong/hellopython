# -*- coding:utf-8 -*-
# Author：Wyss
# File:demo8.py
# Date:2021/11/29 16:11

# 异常和时间模块
# 语法结构：
'''
try:
    运行的代码
except 错误类型:
    出现错误的处理
except Exception as 变量名：
    出现的错误处理
程序中不确定会不会出现问题的代码可以用try
如果出现问题，就执行except里面的代码
捕获的错误会保存在日志中

'''





# 题1：要求用户输入整数
# try:
#     # 用户输入   input
#     num = int(input('请输入数字：'))
#     print(num)
# except:
#     print('请输入正确的数字')

# 题2：针对不同的错误类型进行不同的处理，
# try:
#     # 用户输入一个数字进行2整除
#     num = int(input('请输入数字：'))
#     result = 2/num
#     print(result)
# except ZeroDivisionError:
#     print('不能输入0')
# except ValueError:
#     print('请输入正确的数字')


# 错误类型：
# indexError   下标索引有问题
# keyError     字典里面的键有问题
# TypeError    对象的类型有问题
# IOError      文件打开/关闭 流错误有问题

# 未知的异常也要进行处理   BaseException
# 项目中主要用 Exception
# try:
#     # 用户输入一个数字进行2整除
#     num = int(input('请输入数字：'))
#     result = 2/num
#     print(result)
# except ZeroDivisionError:
#     print('不能输入0')
# except Exception as ee:
#     print('未知错误打印%s'%ee)


# 异常传递
# 函数内不处理异常，调用者处理错误
# def demo1():
#     a = int(input('请输入数字：'))
#     return a
# try:
#     result = demo1()
#     print(result)
# except Exception as bb:
#     print('未知的错误捕获%s'%bb)


# 函数内处理异常
# def demo2():
#     try:
#         a = int(input('请输入数字：'))
#         return a
#     except Exception as cc:
#         print('未知的错误%s'%cc)
# result = demo2()
# print(result)


# 完整语法结构：
import calendar
import datetime

'''
try:
    尝试运行的代码
except 错误类型：
    出现的错误处理
except Exception as 变量名：
    出现的错误处理
else:
    没有异常的代码会执行
finally：
    无论代码有没有问题，都会被执行
'''

# 例：
# try:
#     a = int(input('请输入整数：'))
#     result = 2/a
#     print(result)
# except ZeroDivisionError:
#     print('不能除0')
# except Exception as e:
#     print('未知的错误捕获%s'%e)
# else:
#     print('没有异常的代码会执行')
# finally:
#     print('无论代码有没有问题，都会被执行')


# raise 语法结构    主动抛出异常，用于特定需求
# 定义一个函数，函数提示输入用户密码
# 如果用户输入的密码长度小于八位，抛出异常
# 如果用户输入的密码长度≥八位，返回输入的密码
# def input_pwd():
#     # 用户输入密码
#     pwd = input('请输入密码')
#     if len(pwd) >= 8:
#         return pwd
#     # else:
#     #     print('密码长度不够')
#     exx = Exception('密码长度不够')
#     raise exx
# # u_pwd = input_pwd()
# # print(u_pwd)
# try:
#     u_pwd = input_pwd()
#     print(u_pwd)
# except Exception as e:
#     print('未知的错误捕获%s'%e)



# 时间模块   用于日志，测试报告，订单生产
# 时间：时间戳    从1970年01月01日00时00分00秒开始
# 获取时间戳
# 当前时间戳    time  导包
import time
print('当前时间戳：',time.time())

# 做日期运算
# 时间元祖：用9个数字表示，放在元祖中
# 年，月，日，时，分，秒，一周的第*天(0--6,0是周一)，一年的第*天，夏令时
t = (2021,11,30,16,35,56,1,336,0)
print(t)


# 用代码表示时间元祖 tm_year  tm_mon
print('当前时间元祖：',time.localtime())
print('当前时间元祖：',time.localtime(time.time()))
print('当前时间元祖：',time.localtime(1638261470.2285483))

# 时间元祖转化为时间   time.asctime()
print('以英文的方式转为时间：',time.asctime(time.localtime(time.time())))

# 时间改为系统时间   常用方法
print('当前系统时间：',time.strftime('%Y-%m-%d %H:%M:%S'))

# 时间元祖转化为时间戳   time.mktime()
# 指定时间转为时间戳  2021-11-30
print('指定时间转为时间戳：',time.mktime((2021,11,30,0,0,0,0,0,0)))

# 当前时间转为时间戳
print('当前时间转为时间戳:',time.mktime(time.localtime()))

# 时间戳转为元祖   time.time() 时间戳    time.localtime() 元祖
print('当前时间戳转为元祖:',time.localtime(time.time()))

# 指定日期转为时间格式    1988-10-03 19:32:55
time_str = '1988-10-03 19:32:55'
print(datetime.datetime.strptime(time_str,'%Y-%m-%d %H:%M:%S'))


# 日历  Calendar模块    日历年历月历
# 月历
# mon = calendar.month(2021,11)
# print(mon)

# 年历
# year = calendar.calendar(2022)
# print(year)


# 局部变量、全局变量
# 局部变量：定义在函数内，如果有局部变量，就取局部变量
# 全局变量：定义在函数外，即公共的

num = 20
# 局部变量
def demo1():
    num = 10
    print('在demo函数内部的变量%d'%num)

# 全局变量
# num2 = 20
def demo2():
    print('在demo函数外的变量%d'%num)
demo2()
demo1()