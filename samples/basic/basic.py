print('hello,python')


name=input('Please input your name:')
print("hello,",name)


a='ABC'
b=a
a='XYZ'
print(b)  #get 'ABC'


list(range(5)) #得到结果为：[0, 1, 2, 3, 4]
#               #注意此时list后面要用小括号()

L=list(range(0,100)) #注意list后面加小括号（）而不是中括号[]
print(L)
L[:10:2] #前10个数，每两个取一个
L[::5]   #所有数，每5个取一个
L[]:     #原样复制
  
(0, 1, 2, 3, 4, 5)[:3] #取tuple的前三个元素，结果仍是tuple

#字符串'xxx'也可以看成是一种list，每个元素就是一个字符
'ABCDEFG'[::2] #结果仍是字符串

#list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
  print(key)  #dict无序，默认迭代key
#果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。

from collections import Iterable  #通过collections模块的Iterable类型判断是否能否迭代
isinstance('abc', Iterable) # str是否可迭代  True
isinstance([1,2,3], Iterable) # list是否可迭代  True
isinstance(123, Iterable) # 整数是否可迭代  False
#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
   print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]: #同时引用两个变量
     print(x, y)
