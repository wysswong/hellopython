# -*- coding:utf-8 -*-
# Author：Wyss
# File:demo7.py
# Date:2021/11/19 20:23

# 文件处理：打开、读取、写入、关闭  os模块
# 具体应用：txt,csv,xml,excel,yaml

# 1.txt
# 文件读取
# 1.打开文件   open（路径，模式）     with open() as 别名
# 2.读取文件/写入文件   read()  readline()   readlines()
# 3.关闭文件

# # 读取文件
# f = open('123.txt','r',encoding='utf-8')
# # print(f.readlines())
# # f.close()
#
# # 把列表中的数据都读取出来
# for i in f.readlines():
#     # print(i)
#     # print(type(i))
#
#     # 只读取名字    先用分隔，再根据位置取值
#     print(i.split(',')[1])
#
# f.close()

# 用with open() as 实现,此方式可以不用关闭   输出名字和年龄
# with open('123.txt','r',encoding='utf-8') as f:
#     a = f.readlines()
#     print(a)
# for i in a:
#     # print(i)
#     print(i.split(',')[1:3])   #切片方式，左闭右开



# 2.csv
# 读取csv，需要导包   reader()
# f = open('456.csv','r',encoding='utf-8')
# # print(csv.reader(f))
# f2 = csv.reader(f)
# for i in f2:
#     # print(i)
# #     只读取名字
#     print(i[1])    #列表取值


# with open() as方式
# with open('456.csv','r',encoding='utf-8') as f:
#     a = f.readlines()
# for i in a:
#     print(i.split(',')[1])

# csv写入数据
# stu1 = [4,'huyue',29,'class191']
# stu2 = [5,'guqian',29,'class183']
# f33 = open('456.csv','a',newline='')
# insert_data = csv.writer(f33,dialect='excel')
# insert_data.writerow(stu1)
# insert_data.writerow(stu2)


# 3.xml
#读取xml中的数据   需要导包
from xml.dom import minidom
# 1.加载xml文件
dom = minidom.parse('stu.xml')
# 2.文件数据
root = dom.documentElement
# 3.获取父元素/根节点  即Class
print(root.nodeName)
# 获取类型   节点的类型是1
print(root.nodeType)

# # 获取元素标签名 getElementsByTagName
# # 不加s标识获取一个，加s标识获取所有
# age1 = root.getElementsByTagName('age')
# print(age1[0].nodeName)

# # 获取/节点标签值    先获取标签，再获取值
# name1 = root.getElementsByTagName('name')
# print(name1[0].nodeName)
# print(name1[0].firstChild.data)

# # 获取属性值   getAttribute
# # 获取input所有的标签  getElementsByTagName
# input1 = root.getElementsByTagName('input')
# # input[1]，第一个标签属性
# user = input1[1].getAttribute('username')
# print(user)


# 题1：获取所有学生的信息
# 先获取所有学生文件
# All_stu = root.getElementsByTagName('student')
# # print(All_stu)
# # 再获取学生信息里面的name,age,phone
# stu_name = root.getElementsByTagName('name')
# stu_age = root.getElementsByTagName('age')
# stu_phone = root.getElementsByTagName('phone')
# # 再获取所有学生的值，for循环
# for i in range(3):
#     print(stu_name[i].firstChild.data)
#     print(stu_age[i].firstChild.data)
#     print(stu_phone[i].firstChild.data)


# 题2：只获取ID=S002的值


# 4.excel,yaml

