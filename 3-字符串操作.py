
import elasticsearch
#什么是字符串：python中引号引起来的就是字符串
#作用：用于存储数据

#字符串索引
#通过索引可以准确定位到某个元素
name = "meet"
print(name[0])
print(name[1])
print(name[2])
print(name[3])

print(name[len(name)-1])
print(name[len(name)-2])
print(name[len(name)-3])
print(name[len(name)-4])

#字符串截取
content = "我的名字叫小明"
print(content[5:7])
#5起始位置，7终止位置

#特性：顾头不顾尾巴
print(content[5:-1])
#小

#某个位置不指定时，默认取最 或最后
print(content[5:])
#小明
print(content[:])
#我的名字叫小明

#
print(content[-1:-4:-1])
#[起始位置、终止位置、步长]  默认为1
#此处为从右往左进行取值，步长默认为1，1是从左往右走，所以不设置-1的是无法取到数据的。

res = "大黑哥吃大煎饼"
print(res[-3:-7:-1])
print(res[1:5])
