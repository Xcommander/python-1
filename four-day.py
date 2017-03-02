'''
函数名其实就是指向函数的变量！
因为一个变量可以传入到一个函数中，综合上述，一个函数可以作为参数传入到另外一个函数中。
这种一个函数可以接受另外一个函数作为参数，这种函数叫做高阶函数。
'''


def test(a, b, c):
    print('--------------------------------------高阶函数------------------------------------')
    return c(a) + c(b)


def f(s):
    a = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return a[s]


def r(s, z):
    return 10 * s + z


from functools import reduce


def map_reduce():
    print('--------------------------------------------map/reduce test------------------------')
    # map(r,x),map函数接受两个参数，第一个是函数体，第二个是一个参数列表，也就是这个列表会一个个传入到函数体内，在再返回，被map做成
    # 一个iterator，如何将一个iterator转换成list，通过list()，即可转换。其实map省去了循环的步骤。
    # reduce(r,x)也是接受两个参数，但是不同的是r是函数体，也要接受两个参数，对于reduce的第二个参数，是一个列表，reduce的功能把上次函数
    # r返回的结果和列表的下一个做累积运算。
    print(reduce(r, list(map(f, '2356'))))


def m1(s):
    if s is not None:
        return s[0].upper() + s[1:].lower()


def map_practice():
    print(list(map(m1, ['adam', 'LISA', 'barT'])))


def r1(s, l):
    return s * l


def reduce_practice():
    print('3*5*7*9=', reduce(r1, [3, 5, 7, 9]), sep='')


# map和reduce都是高阶函数，都是接受函数和列表，只不过map负责根据列表来循环函数体生成generator，而reduce是根据列表来累积函数体


def m2(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, }[s]


def r2(s, y):
    return s * 10 + y


def map_reduce_practice(xlc):
    print('------------------------------------map and reduce practice---------------------------------')
    l = list(xlc.split('.'))
    # print(reduce(r2,list(m2,list(l[0]))))
    print(reduce(r2, map(m2, l[0])) + reduce(r2, map(m2, l[1])) / pow(10, len(l[1])))


def f1(s):
    return s % 2 == 1


def f2(s):
    if s is not ' ':
        return True


# d定义一个以3开始的奇数的generator
def j_generator():
    n = 1
    while True:
        n += 2
        yield n


def f_ex(n):
    return lambda x: x % n > 0


def g_generator():
    yield 2
    it = j_generator()
    while True:
        n = next(it)
        yield n
        it = filter(f_ex(n), it)


# 艾氏筛法的含义就是把奇数进行筛选，每一个序列的第一个肯定是素数，再用这个素继续筛选第二个，以此类推，每次第一个就是素数。
def f_od():
    print('---------------------------------------------filter 素数--------------------------------------')
    for n in g_generator():
        if n < 1000:
            print(n, sep=',')
        else:
            break


def filter_test():
    print('---------------------------------------------filter test-------------------------------------')
    # map 和filter 的区别在于，map是把list每次的function的结果收集起来变成一个iterator，而filter是list根据function返回的结果
    # 来决定list的这个值是否保留或者丢弃。
    print('---------------------------------------------filter 质数--------------------------------------')
    print(list(filter(f1, list(range(10)))))
    print('----------------------------------------------filter delete empty-----------------------------')
    print(list(filter(f2, "xxx sssss")))


def is_palindrome(n):
    m = str(n)
    flag = True
    if len(m) >= 1:
        for i in range(len(m) // 2):
            if m[i] == m[-i - 1]:
                pass
            else:
                flag = False
    return flag


# 这里有个技巧那就是str[::-1]就是把一个list颠倒过来。
def is_palindrome1(m):
    return m == int(str(m)[::-1])


# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序,
# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


# 从这几个方面来看，sorted的key值，其实就是建立key-value的规则。比如说按照名字排序，其实就是把元组的第一个拿出来，建立key-value
# 然后根据sorted根据key来排序。根据分数来排序，其实就是把元组的第二个拿出来，建立key-value。以此类推。
def sorted_practice():
    print('--------------------------------------sorted practice-------------------------')
    print('---------------------------------------按名字排序------------------------------')
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L2 = sorted(L, key=by_name)
    print(L2)
    print('---------------------------------------按成绩排名-------------------------------')
    L3 = sorted(L, key=by_score, reverse=True)
    print(L3)


def filter_practice():
    print('---------------------------------回数test-------------------------------')
    print(list(filter(is_palindrome, range(1, 1000))))
    print(list(filter(is_palindrome1, range(1, 1000))))

    # 返回函数，高阶函数不仅可以接受一个函数，还可以把一个函数返回，这个函数就叫做返回函数。
    # 返回函数是在一个函数的内部定义的，并且被返回.这种相关参数和变量都被保存在返回函数中，
    # 这种结构体被叫做“闭包”
    # 闭包问题：
    # 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
    # 返回的函数并没有立刻执行，而是直到调用了f()才执行,fn表示函数名，而fn()表示函数调用。
    # 所以总结返回函数：1.一个函数可以返回一个计算结果，也可以返回一个函数。 2.返回一个函数时，要牢记该函数并没有被执行，只有调用时才会被执行
    # 返回函数中不要引用任何有变化的变量。
    #这里更加理解下返回函数，如果你定义的返回函数有参数（参数和变量不一样），则你在执行函数体时一定要传入参数
    #如果你定义的返回函数没有参数，则调用的时候，不需要传递参数。至于返回函数变量的值，如果是参数，则用参数，没有，则用这个函数体的


def lasy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax + i
        return ax

    return sum


def count():
    fs = []
    for i in range(1, 4):
        def fn():
            return i * i

        fs.append(fn)
    return fs


def lasy_test():
    print('------------------------------------返回函数-----------------')
    f1 = lasy_sum(1, 2, 3, 4)
    f2 = lasy_sum(2, 3, 4, 5)
    print(f1())
    print(f2())
    print('-----------------------------------返回函数测试2-----------------')
    f3, f4, f5 = count()
    print(f3())
    print(f4())
    print()


# 对于函数名相同的函数或者变量来说，先以最新的为主，当最新的被del掉，才会以内置的为主。
if __name__ == '__main__':
    # s=input("请输入一个字符串")
    # print(reduce(lambda x,y:10*x+y,map(int,s.replace('.','')))/pow(10,len(s)-s.find('.')-1 if s.find('.')+1 else 0))
    map_reduce_practice("2223.555")
    filter_test()
    f_od()
    filter_practice()
    sorted_practice()
    lasy_test()
