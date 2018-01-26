# This Python file uses the following encoding: utf-8
# 数学工具
import math
print(math.pi)
print(math.sqrt(2))
# 随机数
import random
print(random.random() * 10)
print(random.choice([1,2,3,4,5,6,7,8,9,0]));
# 序列(字符串)
str2 = 'Spam'
print(str2 + str2[0] * 2)
print(len(str2))
print('s1 = ' + str2[3] + ',s2 = ' + str2[-1])
# 分片(截取字符串)
print(str2[1:2])

str1 = 'Test'
flag = str1.find('es')
print(flag)
flag = str1.replace('t','zer')
print(flag)
print(str1)
