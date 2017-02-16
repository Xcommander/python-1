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
    print('------------------------------第一种简单做法----------------------')
    g = (d for d in os.listdir())
    for n in g:
        print(n)
    for i in range(4):
        print(i)







generator()
