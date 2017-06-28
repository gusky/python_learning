#在Python中，迭代是通过for ... in来完成的

[x*x for k in range(1,11) if x%2==0] 

[m+n for m in 'ABC' for n in 'XYZ'] #双重循环

#在Python中，这种一边循环一边计算的机制，称为生成器：generator。

#要创建一个generator，有很多种方法。
#第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L=[x*x for x in range(10)]
g=(x*x for x in range(10))
#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
#这就是定义generator的另一种方法。  如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

#generator和函数的执行流程不一样:
#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。


#杨辉三角
# -*- coding: utf-8 -*-
def triangles():
L=[1]
while True:
    yield L
    L = [1] + [ L[x-1] + L[x] for x in range(1,len(L)) ] + [1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
