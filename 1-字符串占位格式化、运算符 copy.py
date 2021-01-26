#!/usr/bin/env python
#coding:utf-8

'''
Created on 2020-01-25

@author :yanglei
'''

#字符串占位替换
info = "%s"
name = input('name:')
print(info%(name))

#数字占位替换
info = "%d"
age = int(input('age:'))
print(info%(age))
#总结 %s 是万能的，它可以使用任何字符串

#使用 f+{变量名} 的方式进行字符串拼接
name = input()
info = f"name:{name}"
print(info)
'''注意：f + {变量名}的方式只有在python3.6及以上才可以使用'''
print('--------------------字符串-结束-----------------------')



#算数运算符
# + - * /  - 加、减、乘、除
# // - 整除
# ** -求次方
# % - 取余

#赋值运算符
#*= 自乘
#/= 自除
#//= 整除
#**= 幂次方等于
#%= 取余等于

#逻辑运算符
#关于AND的取值
#都为真的时候取And后面的值
#都为假的时候取And前面的值
#一真一假的时候取假的
print(3 and 5 and 9 and 0 and False)
#结果为0
#过程：1：3、5、9为真，0、false为假，一真一假 -->取假的 0、false
#     2:0 、false都为假 -->取前面的值 0

print(9 and False and 1 and 0)
#结果：false
#过程：1： 9 和 false 一真一假 -->取假的：false
#     2：false 和后面的1也是一真一假 -->取假的：false
#     3: false和0都是假的 -->取前面的值 ：false

print(-1 and 9 and 1 and 2 and 6)
#结果：6
#过程：-1、1、2、3都为真 --> 取后面的值：6
'''注意：不是0的都是真的，负数也是真的'''


#关于OR的取值
#与AND相反
#都为真的时候取or前面的值
print(1 or 2)
#都为假的时候取or后面的值
print(0 or False)
#一真一假的时候取真的
print(1 or 0)

#运算符级别
#() > not > and > or 
print(9 and 1 or not False and 8 or 0 and 7 and False)
#过程：
#1：9 and 1 or True and 8 or 0 and 7 and False
#2：1 or True and 8 or 0 and 7 and False
#3：1 or 8 or 0 and 7 and False
#4：1 or 8 or 7 and False
#5：1 or 8 or False
#6: 1 or 8
#7: 1

#And
#都为真的时候取And后面的值
#都为假的时候取And前面的值
#一真一假的时候取假的
#Or
#都为真的时候取or前面的值
#都为假的时候取And后面的值
#一真一假的时候取真的
print('--------------------逻辑运算符-结束-----------------------')