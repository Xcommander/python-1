class student():
    def __init__(self,name,socre):
        #注意self是python实例化出来的对象实例，而self.name和self.socre是实例的属性，和传入的name与socre并不相同，一个是属性一个是
        #传入参数。由此可见python中的属性是可以随意添加的。也就是实例可以随意绑定数据属性。
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

class student1():
    def __init__(self,name,socre,age):
        self.__name=name
        self.__socre=socre
        self.__age__=age
    def print_socre(self):
        print('%s,%s'%(self.name,self.socre))
    #为了能在外部访问，可以设置setsocre(),和getsocre(),方法
    #注意__xx__是可以从外部访问的,例如__age__就可以访问，简单来说__age__就是特殊变量._xx也是可以访问的，只要不是前面是双下划线就可以
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
class xlc():
    def run(self):
        print(os.times())

#总结来说子类继承了父类的一切，不必要从零开始，子类只需要写自己独有的方法，当然，如果子类觉得父类的方法不合适，就可以重写
#鸭子类型说明了继承不像静态语言那么必须的


#继承有个误区，就是如果父类的构造函数中需要传递参数进去，而且这个属性值，在某个方法中被调用，则在子类的构造函数中，那必须显式调用父类的
#构造函数，否则会有些函数不能使用，继承来的函数


if __name__ == '__main__':
    bob=student('bob',79)
    lisa=student1('lisa',99,33)
    bob.socre=99
    lisa.setsocre(77)
    print(bob.socre)
    print(lisa.getsocre())
    print(lisa.__age__)
    #下面这段代码会报错，是因为lisa中的socre是私有变量，不能在外部被访问。
    #print(bob.socre,lisa.__socre)
    print('----------------------------------------多态与继承-----------------------------')
    A=Animal()
    D=Dog(22)
    C=Cat()
    print('a is Animal ?',isinstance(A,Animal))
    print('a is Animal ?', isinstance(A,Dog))
    print('a is Animal ?', isinstance(A,Cat))
    twice_print(D)
    print('----------------------------鸭子类型测试------------------------------------------')
    x=xlc()
    twice_print(x)



