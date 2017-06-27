print('hello,python')


name=input('Please input your name:')
print("hello,",name)


a='ABC'
b=a
a='XYZ'
print(b)  #get 'ABC'


list(range(5)) #得到结果为：[0, 1, 2, 3, 4]
#               #注意此时list后面要用小括号()

a=list(range(0,100)) #注意list后面加小括号（）而不是中括号[]
print(a)
