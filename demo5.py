# -*- coding:utf-8 -*-
# Author：Wyss
# File:demo5.py
# Date:2021/7/2 15:25

# 运算符
# 比较运算符：==  !=  > >= < <=   用于if判断
# 算术运算符：+ - * / // %    数字操作
# 赋值运算符：= += -= *=      数字操作
# 逻辑运算符：and or not  两个表达式进行判断   用于if判断
# 成员运算符：in   not in    用于if判断
# 身份运算符：is   not is  对于标识符是不是同一个对象   id()内存地址  用于if判断
# print(1>1)
# print(1+1)
#
# a=3
# b=5
# a+=b
# print(a)

# 1.and 两个表达式都为真的时候，才为TURE，反正则为FALSE
# print(40>60 and 60>40)

# 2.or 两个表达式只要有一个为真，就为TURE
# print(40>60 or 50>30)

# 3.not a表达式 a为真时，输出的是FALSE；
# 全部为假时，则输出为TURE
# print(not 50>20)

# if判断
# num = int(input("请输入Num:"))  #int()将num输入的数据转换成int类型
# print(type(num))
# if num <=18:
#     print("Stop")
# else:
#     print("Continue")

# str123 = "process"
# if 's' in str123:
#     print("exist")
# else:
#     print("not exist")

# # 判断内存地址是否是同一个
# a = "123"
# a = "abc"
# if id(a) is id(a):
#     print("The Same")
# else:
#     print("Different")

# 多重if，多个条件判断


# 循环:让特定的事件重复执行
# while循环：while for

# 格式：
# while 条件：
#     循环的内容
# i = 1
# while i <=5:
#     print("hello python")
#     i += 1

# 计算：0+1+2+……+100
# a = 0    #定义变量起始值
# sum = 0  #求和
# while a <= 100:
#     print(a,sum)
#     sum = sum + a
#     a = a +1

# i = 0
# while i < 10:
#     if i == 3:
#         i = i + 1  #(当上面满足条件，则执行此栏)
#         continue
#     i += 1
#     print(i)


# 模块与函数
# 函数：把具有独立功能的代码块封装成一个小的模块
# 1.封装：
# 2.调用：

# 格式：
"""
def 函数名(参数1,参数2,……):
    封装的代码
    :return
函数名(参数值1,参数值2,……)
"""

# 例：
# def say_hello():
#     print("Hello Joy")
#     print("Hello Reyn")
#     print("Hello Tracy")
# say_hello()

# 只有调用函数的时候，函数才会被执行
# 例：
# def sum():
#     num1 = 10
#     num2 = 20
#     result = num1 + num2
#     print("%d + %d = %d"%(num1,num2,result))
# sum()
# 上面是固定数值，可优化成以下传参形式运行  %d--整数  %f--浮点数
# def sum(num1,num2):
#     result = num1 + num2
#     print(("%d +%f = %f"%(num1,num2,result)))
# sum(12,15.5)
# 参数的作用，针对不同的数值进行相同的逻辑处理
# 函数内的参数叫形参，在方法调用里面叫实参

# 完整的函数，实际上有返回值关键字 return
# 在开发过程中，有时会需要一个函数运行的最终结果，可以通过return返回
# def sum(num1,num2):
#     return num1 + num2
# result = sum(10,11.2)
# print(result)

# 空函数，是一个完整的函数，没有实际意义，预留
# def empty():
#     pass

# 函数的参数：必须参数、关键字参数、默认参数、不定长参数
# 必须参数：必须以正确的顺序传入，调用时，必须和申明的一致

# def cart_detail(good_name,price,quantity,totle_price):
#     return "商品名称: {},单价: {}元,数量: {},总价: {}元".format(good_name,price,quantity,totle_price)
# cart = cart_detail("OPPO手机",2500.88,2,5000)
# print(cart)

# 关键字参数：通过关键字传参，不用按顺序写
# def order_details(good_name,price,quantity,order_price):
#     return "商品名称: {},单价: {}元,数量: {},订单金额: {}元".format(good_name,price,quantity,order_price)
# order = order_details(price=4588.88,quantity=2,good_name="TCL OLED电视机",order_price=8000)
# print(order)

# 默认参数：在定义过程中，设置默认值
def good_detail(good_name="TCL OLED电视机",price=4588.88):
    return "商品名称: {},单价: {}元".format(good_name,price)
good = good_detail()
# good = good_detail(good_name="创维电视机")  #可强制给个值，会覆盖前面定义的默认值
print(good)

# 如果位置参数和关键字参数同时存在，先写位置参数 -- price，再写默认参数
# def good_detail(price,good_name="神舟电脑",activity_price=4500):
#     return "商品名称: {},单价: {}元, 活动价： {}".format(good_name,price,activity_price)
# good = good_detail(price=4888.88,good_name="神舟电脑",activity_price=4500)
# print(good)

# 不定长参数：在定义过程中，不知道有多少个参数，设置成不定长参数
# 不定长参数的两种写法： * args(把数据转化成元祖类型) 、 ** kwargs（把数据转化成字典类型）
# * 可以传多个参数，传过来的参数保存在元祖中
# 在参数前面带一个 *，把参数放在元祖里面
# def user(name,*args):
#     print(name,end='')
#     print(args)  #元祖类型
# user("Tom","Heracles",80,"abc@163.com")

# * 单独出现，调用时，要用关键字调用
# def box(num1,*,num3):
#     return num1 + num3
# print(box(5,num3 = 3))

# def aa(*args):
#     print(args)
# aa(15,'abc',12.2)

# ** 可以传多个参数，但是参数是字典类型，保存在字典中，要以键值对来传参
# def ab(**kwargs):
#     print(kwargs)
# ab(name = "Jason",age = 25,gender = 'male')

# * 和 ** 同时存在
# def sort(*args,**kwargs):
#     print(args)
#     print(kwargs)
# sort(33,"颜艳",6666.68,address = "岳阳",job = "Salaman")

# print()时输入 * 和 **，表示对数据进行解析
# * 解析元祖； ** 解析字典
def user(*args,**kwargs):
    print(args)
    print(kwargs)
info1 = (31,'肖霞',6666.68)  #元祖形式
info2 = {'address':'邵阳','job':'Amazon_Salaer'}  #字典形式
user(info1,info2)  #打印出来一个元祖，元祖里面包含元祖和字典，和一个空字典（因为*args已经能
# 够接收所有的值，所以字典内为空 ）

# 如果要把(31,'肖霞',6666.68) 传给*args  {'address':'邵阳','job':'Amazon_Salaer'}传给**kwargs
# user(31,'肖霞',6666.68,address='邵阳',job='Amazon_Salaer')

# * 和 **解包
user(*info1,**info2)


# 函数嵌套：
def test1():
    print("A" * 50)
    print("test1")

def test2():
    print("B" * 50)
    print("test2")
    test1()
    print("C" * 50)
test2()

# 匿名函数 lambda
# 语法：
# lambda 参数，参数：表达式
# 匿名函数和普通函数的区别
# 普通函数求和：
def sum5(num11,num22):
    return num11 + num22
result = sum5(2,3)
print(result)

# 匿名函数求和：
sum = lambda a,b:a+b
print(sum(5,6))

# 模块  py文件 想要用另一个模块中的方法
# 先拿到模块即模块名，在拿模块里面的方法

# 传一个参数和多个参数的区别
# 加*可以传多个参数，不加*则只能传一个参数
# 加**可以传多个参数，不加**则只能传一个参数

# 传参时，*和**的区别
# *是可以传多个参数，且参数保存在元祖中
# **传参时，需要与关键字对应，参数保存在字典中
def demo(*args):
    print(args)
demo(1,'aa',56.7)

def demo1(**kwargs):
    print(kwargs)
demo1(name = 'Lili',age = '25',gender = 'woman')

def demo2(*args,**kwargs):
    print(args)
    print(kwargs)
a = (1,'abc',9.99)
b = {'name':'Brany','age':26,'gender':'man'}
demo2(a,b)  #会打印出一个元祖和一个空字典，args能接受多个参数

# 有关键字的传给kwargs,注意关键字和值使用=号，且关键字不需要‘’
demo2(1,'abc',9.99,name='Brany',age=26,gender='man')

# *和**解包, *a ——> (1,'abc',9.99)  **b ——> {'name':'Brany','age':26,'gender':'man'}
demo2(*a,**b)