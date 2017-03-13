class student():
    def __init__(self,name,socre):
        # 注意self是python实例化出来的对象实例，而self.name和self.socre是实例的属性，和传入的name与socre并不相同，一个是属性一个是
        # 传入参数。由此可见python中的属性是可以随意添加的。也就是实例可以随意绑定数据属性。
        self.name=name
        self.socre=socre
    def print_socre(self):
        print('%s,%s'%(self.name,self.socre))

    def get_grade(self):
        if self.socre >=90:
            print('A')
        elif self.socre >=80:
            print('B')
        elif self.socre >=70:
            print('C')
        elif self.socre >60:
            print('D')
        else:
            print('F')
    def __len__(self):
        return 12

class student1():
    def __init__(self,name,socre,age):
        self.__name=name
        self.__socre=socre
        self.__age__=age
    def print_socre(self):
        print('%s,%s'%(self.name,self.socre))
    # 为了能在外部访问，可以设置setsocre(),和getsocre(),方法
    # 注意__xx__是可以从外部访问的,例如__age__就可以访问，简单来说__age__就是特殊变量._xx也是可以访问的，只要不是前面是双下划线就可以
    def setsocre(self,socre):
        self.__socre=socre
    def getsocre(self):
        return self.__socre

    def get_grade(self):
        if self.socre >=90:
            print('A')
        elif self.socre >=80:
            print('B')
        elif self.socre >=70:
            print('C')
        elif self.socre >60:
            print('D')
        else:
            print('F')

class Animal():
    def __init__(self):
        pass
    def run(self):
        print('Animal is running.......')

class Dog(Animal):
    def __init__(self,age):
        self.age=age
    def run(self):
        print('Dog is running......')

class Cat(Animal):
    def run(self):
        print('Cat is running......')

# 多态的意思是表示Animal此时可以传递Animal以及Animal的子类，有很多种类型，只要符合Animal都可以。所以叫多态，多种多样的种类
#
import os
def twice_print(Animal):
    Animal.run()
    Animal.run()

# 动态语言的鸭子类型意思就是，如果一个对象只要走起来像鸭子，看起来也像鸭子，那么这个对象就刻印认为是鸭子，也就是xlc这个对象传入到
# twice_print(Animal)函数中去，虽然传入的是Animal类型，但是我xlc对象也是传入进去的，因为xlc也是有run方法，所以看起来像Animal
# 所以符合鸭子类型
class xlc1():
    name='222'
    def __init__(self,name):
        self.name=name
    def run(self):
        print(os.times())

# 总结来说子类继承了父类的一切，不必要从零开始，子类只需要写自己独有的方法，当然，如果子类觉得父类的方法不合适，就可以重写
# 鸭子类型说明了继承不像静态语言那么必须的


# 继承有个误区，就是如果父类的构造函数中需要传递参数进去，而且这个属性值，在某个方法中被调用，则在子类的构造函数中，那必须显式调用父类的
# 构造函数，否则会有些函数不能使用，继承来的函数



import types
def fn():
    pass



class ysw():
    #__slots__是为了限制外加类的属性，除了元组里面的，所有都不允许
    __slots__=('name','age','city')
    def read(self,age):
        self.city=age


class xlc(ysw):
    #从xlc继承ysw来看，__slots__并没有对xlc实例生效，也就是说父类的__slots__对子类的实例没效果。除非子类也定义__slots__，那么子类的
    # __slots__是子类的__slots__加上父类的__slots__
    # __slots__只是限制实例对象，不能限制类添加属性
    #__slots__ = ('socre','setage')
    pass

def ysw_age(self,age):
    self.age=age

from types import MethodType
if __name__ == '__main__':
    bob=student('bob',79)
    lisa=student1('lisa',99,33)
    bob.socre=99
    lisa.setsocre(77)
    print(bob.socre)
    print(lisa.getsocre())
    print(lisa.__age__)
    # 下面这段代码会报错，是因为lisa中的socre是私有变量，不能在外部被访问。
    # print(bob.socre,lisa.__socre)
    print('----------------------------------------多态与继承-----------------------------')
    A=Animal()
    D=Dog(22)
    C=Cat()
    print('a is Animal ?',isinstance(A,Animal))
    print('a is Animal ?', isinstance(A,Dog))
    print('a is Animal ?', isinstance(A,Cat))
    twice_print(D)
    print('----------------------------鸭子类型测试------------------------------------------')
    x=xlc1(222)
    twice_print(x)
    print('------------------------------ 测试type------------------------------------------')
    if type(123)==type(234)==int:
        print('int')
    if type('222')==type('234')==str:
        print('str')
    if type(2343)!=type('dasd'):
        print('str don\'t equal int')
    if type(fn)==types.FunctionType:
        print('It\'s function')
    # dir()函数遍历一个对象的所有方法和属性
    print('-------------------------------------测试dir------------------------------------')
    print(dir(bob))
    # 在python中，len()方法是返回长度的，其实它是调用一个对象的__len__()方法，所以只执行len（）,必须保证这个对象有__len__()方法，
    # 可见__XX__变量或者方法在python有特殊作用
    print(len(bob))
    # getattr(),setattr(),hasattr,是对对象进行操作，分别表示，获取某个属性，设置某个属性值，是否有某个属性值，确定的是python是允许
    # 从外部设置属性值的
    if hasattr(bob,'socre'):
        print('bob object has socre')
        print(getattr(bob,'socre','No attibute'))
        setattr(bob,'xlc',2)
        print(bob.xlc)
    print(type(fn))
    print(type(setattr))
    # 给一个类增加属性，要加上self，不然会报错。因为在类中，自动会添加self，在外部增加必须要有self
    setattr(student,'test',lambda self, x:x*x)
    # 给一个对象增加属性或者方法，记住方法也属于属性，直接可以用setattr(),不需要传递self。带上self只是为了能用对象本身的数据
    setattr(bob,'print_self',lambda self,x:print(self.name,x*x))
    print(bob.test(4))
    print(bob.print_self(bob,3))
    if callable(fn):
        print('function')
    print(isinstance(fn,types.FunctionType))
    print(getattr(bob,'print_socre'))
    # getattr()方法，如果是属性是常量，则返回常量，如果是函数体，则返回函数体的内存地址
    list1=[f for f in dir(bob) if callable(getattr(bob,f))]
    print(list1)
    print(getattr(bob,'name'))
    print('-----------------------------类属性和实例对象-------------------------------')
    x=xlc1('22')
    print(xlc1.name)
    print('------------------------------实例绑定方法绑定方法----------------------------')
    # 传入函数的时候只传入函数名，不加(),()表示执行过了
    x=ysw()
    # x.setage=MethodType(ysw_age,x)
    # x.setage(2)
    # print(x.age)
    print('------------------------------类绑定方法--------------------------------------')
    # y=ysw()
    # ysw.setage=ysw_age
    # y.setage(22)
    # print(y.age)
    k=xlc()
    k.setage=MethodType(ysw_age,k)
    k.setage(22)
    print(k.age)
    k.socre=3
    k.name='Kven'
    y1=ysw()
    y2=ysw()
    y1.read(12)
    y2.read(34)
    print(y1.city,y2.city)
    ysw.kk=23
    print(y1.kk)
    # 这个就属于绑定了类的属性，使其变成类的属性，而不是实例的属性
    xlc.setage=MethodType(ysw_age,xlc)
    xlc.setage=ysw_age
    x1=xlc()
    x2=xlc()
    #类的属性是共有的，不能随便改类的属性值，因为一旦改动，这个类的属性值就会发生变化，,就会用本次的值，去替换上一次更新的值
    # 可能导致不可预测的结果
    # 给一个类增加适用方法，但是每个实例不受影响，那就使其变成实例的方法，来对实例进行操作，使其不变成类的属性，用xlc.setage=ysw_setage
    # 所以总结，MethodType是用来绑定该object（包括class and 实例）属性，而=是用来绑定实例对象的属性，所以说def xxx(self)这个都是
    # 针对实例的，MethodType是一动则动，=是一动自己动，其他不动
    x1.setage(33)
    x2.setage(44)
    xlc.abc=2
    xlc.abc=3
    print(x1.age,x2.age)
    print(dir(xlc))
    print(xlc.abc)










