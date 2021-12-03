# -*- coding:utf-8 -*-
# Author：Wyss
# File:demo9.py
# Date:2021/12/1 18:04

# 面向对象：面向对象编程 Object Oriented Programming  OOP
# 是一种封装代码的写法
# 是面向过程的基础上发展过来的，面向对象比面向过程更加灵活和有扩展性

# 面向过程：按照需求逐步去完实现，然后再把独立功能封装，最后再有顺序的调用
# 面向对象：更大的封装，根据要做的事情，在一个对象中可封装多个方法，针对于复杂的系统


# 面向对象
# 两个核心内容：1、类   2、对象
# 类：具有相同特征或者相同行为的事物的统称   抽象的，类似模板，不能直接使用

# 定义类
# class 类名：
#     属性：
#     方法


# 方法：在类中 self      def open(self)
# 类名：即变量名

# 用类中的方法：实例类.方法名   或者属性名

# self:对象本身
# 类中写注释 “”“ ********* ”“”

# 属性：
# init函数：用来定义一个类具有哪些属性
# 特定：创建对象时，会自动调用
# init方法内部使用：self.属性名=属性初始值
# class Cat:
#     def __init__(self,name):
#         print("这是初始化函数")
#         self.name=name
#     def eat(self):
#         print('%s爱吃鱼'%self.name)
# # 具体对象
# cat1=Cat('Jack')
# cat1.eat()
#
# cat2=Cat('Tom')
# cat2.eat()


# 内置函数：
# _init_   创建对象时，会自动调用
# _del_    对象从内存中销毁之前，会被调用
# _str_    返回对象的描述信息  print函数输出


# class Fruit:
#     def __init__(self,new_name):
#         self.name = new_name
#         print('%s新鲜水果到了'%self.name)
#     def __del__(self):
#         print('%s水果坏了'%self.name)
#     def __str__(self):
#        return '我是水果%s'%self.name
# fruit1=Fruit('苹果')
# print(fruit1.name)
