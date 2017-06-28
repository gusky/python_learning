#和map()类似，filter()也接收一个函数和一个序列。
#和map()不同的是，filter()把传入的函数 依次 作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，
##需要用list()函数获得所有结果并返回list。    一定注意：：是list() 是小括号() 而不是中括号[] ！！！


##取回数。 回数是指从左向右读和从右向左读都是一样的数

# -*- coding: utf-8 -*-
def is_palindrome(n):
  m=str(n)
  if m==m[::-1]:    #m[::-1]是将字符串反过来，m[::-2]是将字符串反过来隔一个取一个 m[::a]其中a 可以是负数
     return n
output = filter(is_palindrome, range(1, 100000))
print(list(output))
