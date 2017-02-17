# 切片，按照索引取值，就是位置索引
from collections import Iterable


def qiepian():
    a = list(range(100))
    print('-------------list切片--------')
    print(a[0:10])
    print(a[-1])
    print(a[-99:-97])
    print(a[:])
    b = tuple(range(100))
    print('--------------tuple切片----------')
    print(b[20:30])
    print(b[-4:-1])
    print('---------------字符串切片---------')
    # 字符串是一种特殊的list
    s = 'yansuwan'
    print(list(s))
    print(tuple(s))
    print(s[0:])
    print(s[:])
    print(s[-(len(s)):-1])


# 字符串是一个特殊的list

# 迭代，如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
def diedai():
    # 字典的迭代
    print('--------------------------dict的迭代--------------')
    d = {'xlc': 1, 'yansuwan': 2}
    for key, value in d.items():
        print(key, value)
    print('--------------------------list的迭代--------------')
    l = list(range(5))
    for i in l:
        print(i)
    print('--------------------------检查是否为迭代器----------')
    l2 = set([2, 2, 3, 5])
    print(isinstance(l2, Iterable))

    print('--------------------------list变成key-value格式------------')
    for key, value in enumerate(l):
        print(key, value)
    print('--------------------------list多维数组---------------------')
    # 打印list多维数组，必须保证循环的变量和列数一致，一维数组是打印不出来的。当然可以用enumerate函数，将位置和list元素作为键值对，
    # 其实就是dict
    l1 = [(1, 2), (4, 5), (7, 8)]
    for x, y in enumerate(l1):
        print(x, y)
        # 任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，
        # 只要符合迭代条件，就可以使用for循环任何可迭代对象都可以作用于for循环，
        # 包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环,当然dict也属于迭代对象


# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
import os


def list_product():
    print('-----------------------------1 range生成-------------------')
    print(list(range(1, 20)))
    print('-----------------------------2 for生成---------------------')
    l = [x * x for x in list(range(10)) if x % 2 == 0]
    print(l)
    print('-----------------------------3 两重循环---------------------')
    s = [m + n for m in 'ABC' for n in 'FGK']
    print(s)
    # 总结，for循环的列表表达式，要写成一个list变量格式，必须写成[变量 for语句]，这个变量表示列表元素.也就是写列表生成器时，
    # 必须在for语句前面添加一个变量,for循环前面的变量可以是单个变量，也可以是一个变量表达式
    print(list([d for d in 'Bcd']))
    print(list('xxxxx'))
    print('--------------------当前目录和文件------------')
    fir = [d for d in os.listdir('./')]
    print(fir)
    print('------------------------------------dict生成-------------')
    d = {'xu': 'linchao', 'yan': 'suwan'}
    l3 = [k + '=' + v for k, v in d.items()]
    print(l3)
    print('----------------------------------------str转换大小写----------')
    l4 = [i.lower() for i in 'XULINchao']
    print(l4)
    # list 增加元素通过append()方法，dict增加元素通过键值对，d['x']='y',删除元素都是pop方法。

    print('-----------------------------------------practice--------------------')
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [sr.lower() for sr in L1 if sr is not None and isinstance(sr, str)]
    print(L2)


# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。不像list一下子全部生成
def generator():
    # 创建一个生成器，第一种方法特别简单，就是将列表生成式中的[]，改成（）
    # 一切迭代器，都可以用for循环打印出来，迭代器意思就是遍历打印，只要是个list tuple dict generator等，只要能遍历，都能for循环
    # 第二种方法是生成器函数，yield L之类的
    print('------------------------------第一种简单做法----------------------')
    g = (d for d in os.listdir())
    for n in g:
        print(n)
    for i in range(4):
        print(i)


'''
我们已经知道，可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：

被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
可迭代对象和迭代器的区别在于，可迭代对象只需要能for循环，而迭代器要能够被next函数调用，并且能不断返回下一个对象
'''
from collections import Iterator


def Iterator1():
    print('--------------------------测试generator-----------------------')
    print(isinstance((x for x in list(range(4))), Iterator))
    print('--------------------------测试list----------------------------')
    print(isinstance([i for i in range(4)], Iterator))
    print('--------------------------测试dict----------------------------')
    print(isinstance({}, Iterator))
    print('--------------------------测试set----------------------------')
    print(isinstance(set([1, 2, 3]), Iterator))
    print('--------------------------测试str----------------------------')
    print(isinstance('addsadsa', Iterator))
    # 虽然dict list tuple set都不是一个iterator，但是可以通过iter函数来转换。
    print('---------------------------iterator转换------------------------')
    print(isinstance(iter({}), Iterator))
    '''
    通过上面分析，list ，tuple，dict,set,str都不是一个Iterator，但是是一个Iterable（因为可以for循环）。之所以不是iterator
    是因为Iterator是一个数据流，可以被next函数不断调用返回下一个数据，直到没有数据时，返回stopIteration。我们可以预测这个数据流是有序
    的，但我们不知道他的长度，因为他是边计算边生成。这点类似于generator，其实感觉generator就是Iterator，只不过定义有点出入。
    所以说Iterator具有惰性。我们没办法知道其长度。所以说Iterator可以表示一个无穷大的数据流，而一个list显然是不能做出的。



    总结：凡是可以作用于for循环的对象都是Iterable对象
         凡是可以作用于next函数的对象都是Iterator对象，因为他们表示惰性计算
         python中的for循环其实就是一个不断next的过程，直至出现stopIterator异常，但是为啥list可以for，因为list等是在for循环内部做成
         Iterator，而不是一开始就是Iterator。一开始的Iterator具有惰性，后面转化的不具有惰性。
         所以说定义一个Iterator或者generator，要如何不断next打印出来，可以通过for循环来实现。
         generator和Iterator函数的调用后，会一直驻扎内存，直至不用被释放。因为它是一个不断被next的过程。


    '''


# Iterator举例
def Iterator_1():
    n = 0
    while n < 100:
        yield n
        n = n + 1


o = Iterator_1()
m = 0
print('-------------------------------第一次打印----------------------')
for i in o:
    print(i)
    m += 1
    if m == 10:
        break

print('-------------------------------第二次打印-----------------------')
m = 0
for n in o:
    print(n)
    m += 1
    if m == 10:
        break

print('-----------------------------第三次打印，重新定义个Iterator对象--------------------------')
m = 0
i = Iterator_1()
for j in i:
    print(j)
    m += 1
    if m == 10:
        break
