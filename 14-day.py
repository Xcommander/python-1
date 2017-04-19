from collections import namedtuple, deque, defaultdict, OrderedDict,Counter


# namedtuple是针对tuple，设定属性；deque是针对list的，属于增强型list;defaultdict是针对dict，增强dict，增加默认值，但是注意，
# 传递参数是，要注意传入的是个返回值的函数
# OderedDict是按照插入顺序来读取列表值

def namedtuple_test():
    cricle = namedtuple("Cricle", ['x', 'y', 'z'])
    p = cricle(2, 3, 6)
    print(p.x, p.y, p.z)
    if isinstance(p, tuple):
        print('It\'s a tuple')


def deque_test():
    q = deque(['a', 'b', 'c'])
    q.append('d')
    q.appendleft('y')
    print(q)


def defaultdict_test():
    d = defaultdict(lambda: 'NA')
    d['xlc'] = "xulinchao"
    print(d['xlc'], d['yansuwan'], sep='    ')


def OderedDict_test():
    d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    for key in d.keys():
        print(key)


class FIFODict(OrderedDict):
    def __init__(self, cap):
        super(FIFODict, self).__init__()
        self._cap = cap

    def __setitem__(self, key, value):
        keylike = 1 if key in self else 0
        if len(self) - keylike >= self._cap:
            last = self.popitem(last=False)
            print("remove item is ", last)
        if keylike:
            del self[key]
        OrderedDict.__setattr__(self, key, value)

def Cunter_test():
    c=Counter()
    xlc="xlcsdasdasda"
    x=xlc
    x=x+'/yansuwan'
    print(x)
    print(x)
    for i in x:
        c[i]=c[i]+1
    for i in c.keys():
        print("%s 出现 %s 次"%(i,c[i]))



if __name__ == '__main__':
    # 返回函数顾名思义，就是函数调用时，返回一个函数。注意返回函数一定要写在调用函数里面。不然就叫做函数调用了。
    # 装饰器原理就是返回函数体内的装饰函数
    defaultdict_test()
    OderedDict_test()
    print()
    Cunter_test()
    '''
    l=list([1,2,3])
    print(l)
    x=namedtuple("xlc",['x','y'])
    x1=x(1,2)
    print(x1.y)
    '''
