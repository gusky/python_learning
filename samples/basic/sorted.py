
#Python内置的sorted()函数就可以对list进行排序
#此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
#按绝对值大小排序：
sorted([36, 5, -12, 9, -21], key=abs)

#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。

#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True:     ((( 可以一直加条件，第一个是list！！！)))
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
