from __future__ import print_function
# for i in range(1,5):
#     for j in range(1,6):
#         if i==1 or i==4 or j==1 or j==5:
#             print('*',end =" ")
#         else:
#             print(' ',end=" ")
#     print()
#
# for i in range(1,6):
#     for j in range(1,7-i):
#         if i==1 or i==5 or j==1 or j==7-i-1:
#             print('*',end =" ")
#         else:
#             print(' ',end=" ")
#     print()
# for i in range(5):
#     for j in range(0,5-i):
#         print(end="*")
#     #控制列，第一行一列，第二行两列
#     for k in range(6-i,6):
#         print('o',end=" ")
#     print()
# print("-"*20)
#
#
# for i in range(5):
#     # for k in range():
#     for j in range(0,5-i):
#         print(end=" ")
#     for k in range(5-i,6):
#         if i==0 or k==5-i or i==4 or k==5:
#             print('*',end =" ")
#         else:
#             print(' ',end=" ")
#     print()
#
# print('^'*20)
# for i in range(5):
#     print(i)
#
#
#
# #字母D
# for m in range(4):
#     for n in range(3):
#         if n==0:
#             print('*',end=" ")
#         elif m==0 or m==3:
#             if n==2:
#                 break
#             else:
#                 print('$'," ")
#         elif n==2:
#             if m==0 or m==3:
#                 break
#             else:
#                 print('@',end=" ")
#         else:
#             print(' ',end=" ")
#     print()


# #字母p
# for m in range(1,7):
#     for n in range(1,4):
#         if n==1:
#             print('*',end=" ")
#         elif m==1 or m==4:
#             if n>2:
#                 break
#             else:
#                 print('#',end=" ")
#         elif n>2:
#             if m==2 or m==3:
#                 print('&',end=" ")
#         else:
#             print(' ',end=" ")
#     print(" ")

# R
# for m in range(5):
#     for n in range(4):
#         if n==0:
#             print('*',end=" ")
#         elif m==0 or m==3:
#             if n==2:
#                 break
#             else:
#                 print('#',end=" ")
#         elif n==2:
#             if m==0 or m==3:

#                 break
#             else:
#                 print('@',end=" ")
#         else:
#             print('-',end=" ")
#
#     print(" ")

#######################################################################################
#类似栈先进后出的关系
# #要有递推关系 要有临界值
# def digui(num):
#     print('$'+str(num))
#     if num >0:
#         #调用本身的函数
#         digui(num-1)
#     else:
#         print('='*20)
#     print(num)
# digui(1)


#LEGB
# tt = "1"
# def test1():
#     tt ="2"
#     print("test1 函数的局部变量tt{}".format(id(tt)))
#
#     def test2():
#         global tt
#         tt = "3"
#         print("全局变量tt{}".format(id(tt)))
#     test2()
#     print(tt)
#
# print('$'+tt)
# test1()
# print('*'+tt)
# print("全局变量tt{}".format(id(tt)))

#
#
# import os
# path = r'd:\listdir'
# for filename in os.listdir(path):
#     #目录的路径和文件名拼接起来，得到了文件的绝路路径
#     print(os.path.join(path,filename))
# import os
# def getdirpath(dirpath):
#     total = 0
#     allname = os.listdir(dirpath)
#     for name in allname:
#         fullpath = os.path.join(dirpath,name)
#         if os.path.isfile(fullpath):
#             total += os.path.getsize(fullpath)
#         elif os.path.isdir(fullpath):
#             total += getdirpath(fullpath)
#     return total
# size = getdirpath('F:\__MACOSX')
# print(size)




###数据类型的内置函数
####number 数值型 （int float  bool   complex     string 字符型       tuple 元组        list 列表         dictionary 字典   set集合

# #####字符串的简单操作
# str1='lo'
# str2='ve'
# print(str1+str2)
# print('lo'+'ve')
#
# print('#'*10)
#
# s='ilove python'
# print(s[-1])

#切片 包含开始不包含结尾
# print(s[1:5])

#help(str)
#capitalize() 首字母大写 返回字符串
# s = 'i like python'
# print(s.capitalize())

#title()将每个单词首字母大写
s = 'l love python'
print(s.title())

#upper()将所有字母变为大写


#lower（）所有字母小写
#swapcase（） 大小写互换
s = 'l l LLL'
print(s.swapcase())
#len()计算字符串长度，不属于字符串的内建函数
##find（） 查找指定字符串，找不到返回 -1,找到返回索引值
# ##index（）查找指定字符串，找不到报错
# s='asdfgkilkmb'
# s1=s.find('a')
# s2=s.index('0')
# print(s1)
# print(s2)

##count 计算字符串出现的次数
# s='sdffvbgmmm'
# print(s.count('m'))

#startswith() 检测是否有有制定的字母开头，返回布尔值
#endswith（） 检测是否以制定的字母结束
s='I an a baby '
print(s.startswith('I'))
print(s.endswith(' '))




