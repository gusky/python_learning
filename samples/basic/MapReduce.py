#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数  依次  作用到序列的每个元素，并把结果作为新的Iterator返回
#map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算


##将字符串小数转换成浮点数
# -*- coding: utf-8 -*-
from functools import reduce
def str2float(s):
    n=s.index('.')   #找到小数点的位置
    r=list(map(f1,s))
    return reduce(f2,r[:n])+reduce(f2,r[n+1:])/10**len(r[n+1:])   #除以10的r[n+1：]长度次方
def f1(L):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':12}[L]
def f2(x,y):
    return 10*x+y
print('str2float(\'123.456\') =', str2float('123.456'))
print('str2float(\'123.456\') =', str2float('123453.456'))
