# -*- coding:utf-8 -*-
# Author：Wyss
# File:demo6.py
# Date:2021/8/3 20:11

# 文件处理和OS模块
# 文件的作用：储存数据，便于后续从文件中读取
# 文件处理操作：
# 1.打开   open(文件路径，访问模式)
# 主模式： r---只读    w---只写   a---只写
# r+:在r的基础上增加了可写的功能
# w+：在w的基础上增加了可读的功能
# a+：在a的基础上增加了可读的功能
# rb、wb:用于二进制文件

# 2.写入 & 读取
# 3.关闭   会占用服务器资源，所以操作完成后需要关闭

# open --- 创建一个文件，并写入内容，结束后关闭文件
# f = open('test.txt','w')
# f.write("""
# 123木头人，
# 没有心的木头人，
# 心不动则不痛
# """)
# f.close()

# r --- 读取文件
# f = open('test.txt','r')
# print(f.read())
# f.close()

# r --- 读取的文件不存在时，会报错
# f = open('aaa.txt','r')
# f.read()
# f.close()

# w --- 只写
# 如果文件不存在，会新建一个文件
# 如果文件已存在，新增的内容会覆盖原内容

# f = open('test11.txt','w')
# f.write("tom & jerry")
# f.close()

# a --- 只写
# 如果文件不存在，则会新建一个文件
# 如果文件存在，则会在原内容后面，追加新增的内容

# f = open('test22.txt','a')
# f.write("abc123")
# f.close()

# r+ --- 在r的基础上增加了可写的功能,写的内容会覆盖原内容
# f = open('test22.txt','r+')
# # 获取指针位置   tell
# print(f.tell())
# f.write('xxx')
# # print(f.read())
# f.close()

# w+ --- 在w的基础上增加了可读的功能,文件不存在时，会新建文件
# 写的内容会覆盖原内容，写完后，指针在末尾，需要读取数据时可以用 seek 偏移量
# seek(偏移量,指针位置) 0：从头开始读取   1：从当前位置开始读取   2：从末尾开始读取
# f = open('test22.txt','w+')
# # f.write('kcoi')
# # print(f.tell())
# f.seek(2,0)
# f.close()

# a+ --- 在a的基础上增加了可读的功能,文件不存在时，会新建文件
# 写入的内容会追加在原内容后面
# 读取内容时可以用seek
# f = open('test22.txt','a+')
# f.write('lovemore')
# print(f.tell())
# f.close()

# 文件路径：
# 1.当前目录下的文件   ./文件名
# f = open('./test.txt','r')

# 2.访问跨目录文件   ../文件目录/文件名
# f = open('../Demo/test666.txt')
# print(f.read())
# f.close()

# 3.同级目录下的文件   ./文件目录/文件名


# 读取文件   read()  readline()  readlins()
# 换行也算一个字符
# read(字符数)
# f = open('test.txt','r')
# print(f.read(3))
# f.close()
#
# # readline()   只读取一行
# f = open('test.txt','r')
# print(f.readline())
# f.close()

# readlines()  读取文件内所有内容，显示为一个列表，且换行处会用 \n 显示，文件内容每行的显示格式为 ‘***\n’,
# f = open('test.txt','r')
# print(f.readlines())
# # 读取指定行
# print(f.readlines()[2])
# f.close()

# 一般readlines() 会搭配 for循环使用
# f = open('test.txt','r')
# for i in f.readlines():
#     print(i)
# f.close()


# with ... open() as 可以不用关闭文件
# """
# with open (路径,模式) as 别名：
#     文件操作
# """

# with open('test.txt', 'r') as file:
#     print(file.read())

# os模块：处理文件或文件目录
# 1.直接导入
import os
# 路径转义：用r 或者 \\
file1 = r'D:\PycharmProjects\Demo_L\aass'
# 创建一个文件目录
# os.mkdir(file1)

# 删除文件
# os.rmdir(file1)

# 删除非空文件  shutil
# import shutil
# shutil.rmtree(file1)

# 文件重命名  rename(r'文件的绝对路径',r'文件的绝对路径+新名字')
# os.rename(r'D:\PycharmProjects\Demo_L\aass',r'D:\PycharmProjects\Demo_L\newfile')

# 获取当前文件目录  os.getcwd()
# print(os.getcwd())

# 获取当前文件路径  os.path.join()
path1 = os.getcwd()
print(path1)

# 拼接文件路径
demo6 = 'demo6.py'
print(os.path.join(path1,demo6))

# 获取文件权限  os.access(path,mode)
# F_OK (是否存在)
# R_OK (可读)
# W_OK (可写)
# X_OK (可执行)

# 判断 test.txt 是否存在
file2 = r'D:\PycharmProjects\Demo_L\test.txt'
print(os.access(file2,os.F_OK))
# 是否可读
print(os.access(file2,os.R_OK))
# 是否可写
print(os.access(file2,os.W_OK))
# 是否可执行
print(os.access(file2,os.X_OK))

# 设置文件权限  os.chmod
