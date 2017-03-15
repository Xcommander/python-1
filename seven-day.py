# __str__
class Student(object):
    def __init__(self,name):
        self.name=name
    # print 一个object，其实就是调用该object __str__方法
    def __str__(self):
        return 'xlc'
    #直接显示用__repr__
    __repr__=__str__

class fb(object):
    # __iter__这个方法表示如果一个类想被for循环，那必须有__iter__(),用来返回一个可迭代的object，然后通过不断循环该对象的__next__()
    # 方法直到遇到stopIteration才停止。所以说__iter__()和__next__()是搭配使用的。
    def __init__(self):
        self.a,self.b=0,1

    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a >100000:
            raise StopIteration()
        return self.a
    # 虽然按照__iter__()可以for循环，但是不可以按照list切片来，要达到list切片，需要__getitem__()函数
    def __getitem__(self, item):
        if isinstance(item,int):
            for i in  range(item):
                a,b=b,a+b
            return a
        elif isinstance(item,slice):
            start=item.start
            stop=item.stop
            if start is None:
                start=0
            a,b=1,1
            l=[]
            for i in range(stop):
                if i>=start:
                    l.append(a)
                    a,b=b,a+b
            return l







if __name__ == '__main__':
    s=Student('Michael ')
    print(s)
    print('---------------------fb test-----------------------------------------')
    f=fb()
    for i in f:
        print(f.a)
    print(f[:4])
