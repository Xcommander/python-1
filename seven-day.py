# __str__
class Student(object):
    def __init__(self, name):
        self.name = name

    # print 一个object，其实就是调用该object __str__方法
    def __str__(self):
        return 'xlc'

    # 当你试图去获取一个不存在的属性的时候，要让它返回一个理想的值的时候，这时候就用到了__getattr__()函数，一切不存在的属性，python
    # 解释器都会试图去从__getattr()中去获取
    def __getattr__(self, item):
        if item == 'socre':
            return 99
        else:
            return 1

    # 直接显示用__repr__
    __repr__ = __str__


class fb(object):
    # __iter__这个方法表示如果一个类想被for循环，那必须有__iter__(),用来返回一个可迭代的object，然后通过不断循环该对象的__next__()
    # 方法直到遇到stopIteration才停止。所以说__iter__()和__next__()是搭配使用的。
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    # 虽然按照__iter__()可以for循环，但是不可以按照list切片来，要达到list切片，需要__getitem__()函数
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 0, 1
            for i in range(item):
                a, b = b, a + b
            return a
        elif isinstance(item, slice):
            start = item.start;
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            l = []
            for i in range(stop):
                if i >= start:
                    l.append(a)
                a, b = b, a + b
            return l


# 通过__getattr__()可以写出一个动态的调用

class Chain(object):
    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, item):
        if item == 'users':
            return lambda x: Chain('%s/%s' % (self.path + '/users', x))
        else:
            return Chain('%s/%s' % (self.path, item))

    def __str__(self):
        return self.path

    __repr__ = __str__


if __name__ == '__main__':
    s = Student('Michael ')
    print(s)
    print('---------------------fb test-----------------------------------------')
    f = fb()
    '''
    for i in f:
        print(f.a)
    print(f[:4])
    print(s.socre)
    '''
    print(Chain().users('michael').repos)
