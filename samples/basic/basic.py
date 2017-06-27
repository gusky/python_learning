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
