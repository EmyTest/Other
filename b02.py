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
# s = 'l love python'
# print(s.title())
#
# #upper()将所有字母变为大写
#
#
# #lower（）所有字母小写
# #swapcase（） 大小写互换
# s = 'l l LLL'
# print(s.swapcase())
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
# #endswith（） 检测是否以制定的字母结束
# s='I an a baby '
# print(s.startswith('I'))
# print(s.endswith(' '))

#isspace 检测字符串是否是空字符串
# s='    '
# s1=' i am   '
# print(s.isspace())
# print(s1.isspace())

# isalum() 检测字符串是否有字母加数字组成 返回布尔值
# ##如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
# s = 'mmmmqqq2  3333 rrr'
# s1 = 'skkkkk'
# print(s.isalnum())
# print(s1.isalnum())


'''
isdigit()
True: Unicode数字，byte数字（单字节），全角数字（双字节）
False: 汉字数字，罗马数字,小数
Error: 无 

isdecimal() 
True: Unicode数字，全角数字（双字节） 
False: 罗马数字，汉字数字,小数
Error: byte数字（单字节） 
isnumeric() 
True: Unicode数字，全角数字（双字节），罗马数字，汉字数字 
False: 小数 
Error: byte数字（单字节）
'''

# s = '123.0'

#split()用指定的字符切割字符串，返回由字符串组成的列表
# s = '日照香炉生紫烟#疑是银河落九天#飞流直下三千尺'
# list1 = s.split('#')
# print(list1)

# #splitlines() 以换行切割字符串
# s='''日照香炉\n生紫烟\n疑是银河\n落九天\n飞流直下\n三千尺'''
# print ( s.splitlines())

#join() 将列表按照指定字符串连接 返回的是字符串
# list1 = ['日照香炉生紫烟','疑是银河落九天','飞流直下三千尺']
# s= '*'.join(list1)
# print(s)
#
# ##ljust() 指定字符串长度，内容靠左，不足的地方用指定字符填充
# s='abc'
# print(len(s))
# print(s.ljust(5,'$'))


#strip() 去掉左右两边指定的字符，默认是去掉空格
#lstrip（）去掉左侧指定的字符，默认是去掉空格
#rstrip（）去掉右侧指定的字符，默认是去掉空格
# s = '     zxcv     '
# print('---'+s.strip()+'---')
# print('---'+s.lstrip()+'---')
#
# print('---'+s.rstrip()+'---')

#zfill() 指定字符串长度 内容靠右 不足的位置用0填充
# s='abc'
# print(s.zfill(6))


#maketrans()生产用于字符串替换的映射表
# #tarnslate()进行字符串替换
# s='我今天吃了米饭'
# table = s.maketrans('吃了米饭','喝了牛奶')
# print(table)
# print(s.translate(table))



#append 向列表末尾添加新元素   返回none

# list1=[1,2,3,4,5]
# list1.append(5)
# print(list1)


# #copy()
# list1=[1,2,3,4,5]
# list2=list1.copy()
# print(list2)


#count（）计算某个元素在列表中出现的次数
# list1=[1,1,2,5,1,3]
# print(list1.count(1))


#extend()将一个列表继承另一个列表
# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]
# list3=list1.extend(list2)
# print(list1)
# print(list2)
# print(list3)


#index() 获取值在列表中的索引
# list1 = [1,2,3,4,5]
# print(list1.index(3))


#insert() 在指定位置前插入元素   2个参数
# list1 = [1,2,3,4,5]
# list1.insert(2,8)
# print(list1)



#pop() 根据索引移除列表内一个元素，不给索引默认移除最后一个
# list1=[1,2,3,4,5]
# list1.pop(1)
# print(list1)
#pop() 根据字典中指定的元素 返回键所对应的值
# dict1={'a':1,'b':2,'c':3}
# print(dict1.pop('b'))
# print(dict1.pop('d',4))



# a={'a','b','g',5}
# a.pop()
# print(a)

#popitem()移除字典的键值对 返回移除的键和值
# dict1={'d':4,'a':1,'b':2,'c':3}
# print(dict1.popitem())


#remove() 移除列表指定的值
# list1=['a','b','c','d']
# list1.remove('b')
# print(list1)

#reverse() 列表反转
# list1 = [1,2,3,4]
# print(list1.reverse())
#
# list1=[1,2,3,4]
# list2=list(reversed(list1))
# print(list2)



# a=[1,2,3,4,5,6,7,8,9]
# b=list(reversed(a))
# print (b)



#sort() 排序 默认从小到大
# list1=[5,2,4,6,1,9


#clear() 清除整个字典 返回none
# dict1={'a':1,'b':2,'c':3}
# dict1.clear()
# print(dict1)


#fromkeys() 按照指定的序列为键创建字典，值都一样的
# list1 = ['a','b','c']
# dict1={}.fromkeys(list1)
# dict2={}.fromkeys(list1,3)
# print(dict1,dict2)
# print(dict2)


#get 根据键获取指定的值 找不到的键 如果设默认值则返回默认值  没有设默认值 返回none
# dict1={'a':1,'b':2,'c':3}
# print(dict1.get('b'))
# print(dict1.get('d'))
# print(dict1.get('d',4))


#items（）将字典变成类似于元组的形式方便遍历
# dict1={'a':1,'b':2,'c':3}
# for k ,v in dict1.items():
#     print(k,v)
# print(dict1.items())

#keys() 遍历字典中的键
#values（）遍历字典中的值

#setdefault() 在字典里添加一个元素
# dict1={'d':4,'a':1,'b':2,'c':3}
# print(dict1.setdefault('e',5))
# print(dict1)

#update() 修改字典中的值
# dict1={'d':4,'a':1,'b':2,'c':3}
# dict1.update({'a':4,'c':9,'f':1})
# print(dict1)

# #集合
# a=set()
#
# list1=[1,2,3,4]
# a=set(list1)
# print(a)


#add()向集合添加元素
# set={3,4,5,6,7}
# set.add(0)
# print(set)


#clear() 清空集合
#copy()复制集合

#remove()删除集合中的某个值，如果这个值不在集合中，会报错
# a={'a','c','f','r'}
# a.remove('a')
# a.remove(5)
# print(a)

#discard() 删除集合中的某个值，如果这个值不在集合中，什么也不做
# a={'a','c','f','r'}
# a.discard(4)
# print(a)


#difference() 差集
#difference_update() 区别：第一个返回新的集合，第二个把原来的集合覆盖

set1={1,2,3,4,7}
set2={2,4,8,111,24}
# set3=set1.difference(set2)
set4=set2.difference_update(set1)
# print(set3)
print(set4)








