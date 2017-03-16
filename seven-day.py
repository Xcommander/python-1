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


# 要使一个对象本身就可以被调用，就像一个函数一样，xx()这种类型写法，那么则需要__call__函数
# 比如上面Chain().xlc('xlc').yaw.zc.此时xlc返回的就是一个Chain对象,就变成了Chain.Chain('xlc').ysw.zc，Chain('xlc')就是
# 直接调用实例本身，所以要写__call__()
class NewChain(object):
    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, item):
        return NewChain('%s/%s' % (self.path, item))

    def __call__(self, item):
        return NewChain('%s/%s' % (self.path, item))

    def __str__(self):
        return self.path

    __repr__ = __str__


# 当使用Enum枚举定义的时候，会自动给实例赋值，从默认从1开始，像fiveline为class，然后Gold等是类的实例，然后编译器会自动给他们赋值
from enum import Enum,unique

FiveLine = Enum('FiveLine', ('GOld', 'Wood', 'Water', 'fire', 'Eatrh'))

class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6

# 用type查看一个类型或者变量的类型，class的定义时运行时动态创建的，而创建class的方法就是使用tyoe()函数
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如我们可以通过type()函数创建出hello类，而无需
# 通过class Hello(object)的定义
class Hello(object):
    def hello(self,name='hello'):
        print('Hello, %s'%name)

def fn(self,name='Hello'):
    print('Hello,%s'%name)





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
    print(callable(NewChain()))
    print(NewChain().uesrs('michael').repos)
    for name, member in FiveLine.__members__.items():
        print(name, '>=', member, ',', member.value)

    for day,value in Weekday.__members__.items():
        print('it\'s %s and %s '%(day,value.value))
    # items是实例名加上实例对象组成的dict，而value是实例的属性
    for k in Weekday.__members__.items():
        print(k )
    # callable 判断的是一个内存地址，也就是判断的是一个函数名而非一个函数执行，不要xx（）,只要xx
    print(callable(Chain.__call__))
    print('------------------------------------test type--------------------------')
    h=Hello()
    print(type(Hello))
    print(type((h)))
    # type()创建类
    #要创建一个class对象，type()函数依次传入3个参数：

    # class的名称；
    # 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    # class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
    #通过type()函数创建的类和直接写class是完全一样的，
    # 因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
    my=type('Hello',(object,),dict(Hello=fn))
    m=my()
    print(type(m))
    print(type(m.Hello))

