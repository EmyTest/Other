import  random
import  math

# #输入函数
# num =  input("请输入一个三位数: ")
# # print(num)
# if num.isdigit() and 100<=int(num)<=999:
#     # 输入的函数是字符型， 不强制转换会报错
#
#         pass
# else:
#     print("请按规定输入")


'''
输入一个三位数与程序随机数比较大小
如果大于程序随机数，则分别输出这个三位数的个位\十位\百位
如果等于程序随机数，则提示中将，记100分
如果小于程序随机数，则将120个字符输入到文本的文件中（规则是每一条字符串的长度为12，单独占一行，并且前四个是字母，后8个是数字）

'''

# num = input("请输入一个三位数")
# #程序随机数
# random_num = random.randrange(100,1000)
# #检测输入的是否是纯数字
# if num.isdigit() and 100 <= int(num) <= 999:
#     unm=int(num)
#     random_num = int(random_num)
#     #and int(num) > int(random_num):
#     '''求百位数的方法 -- 地板除100或者用数学模块当中的floor（）函数'''
#     if num >random_num:
#         bai = int(num)//100
#         print(bai)
#
#     if num == random_num:
#         print(random_num)
#     if num < random_num:
#         print(random_num)
# else:
#     print("请按规定输入")
