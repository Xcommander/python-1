'''
函数名其实就是指向函数的变量！
因为一个变量可以传入到一个函数中，综合上述，一个函数可以作为参数传入到另外一个函数中。
这种一个函数可以接受另外一个函数作为参数，这种函数叫做高阶函数。
'''

def test(a,b,c):
    print('--------------------------------------高阶函数------------------------------------')
    return c(a)+c(b)



def f(s):
    a={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return a[s]

def r(s,z):
    return 10*s+z

from functools import reduce


def map_reduce():
    print('--------------------------------------------map/reduce test------------------------')
    #map(r,x),map函数接受两个参数，第一个是函数体，第二个是一个参数列表，也就是这个列表会一个个传入到函数体内，在再返回，被map做成
    #一个iterator，如何将一个iterator转换成list，通过list()，即可转换。其实map省去了循环的步骤。
    #reduce(r,x)也是接受两个参数，但是不同的是r是函数体，也要接受两个参数，对于reduce的第二个参数，是一个列表，reduce的功能把上次函数
    #r返回的结果和列表的下一个做累积运算。
    print(reduce(r,list(map(f,'2356'))))


def m1(s):
    if s is not  None:
        a=s.lower()
        return a.replace(a[0],a[0].upper(),1)
def map_practice():
    print(list(map(m1,['adam', 'LISA', 'barT'])))

def r1(s,l):
    return s*l

def reduce_practice():
    print('3*5*7*9=',reduce(r1,[3, 5, 7, 9]),sep='')
#map和reduce都是高阶函数，都是接受函数和列表，只不过map负责根据列表来循环函数体生成generator，而reduce是根据列表来累积函数体


def m2(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,}[s]

def r2(s,y):
    return s*10+y


def map_reduce_practice(xlc):
    l=list(xlc.split('.'))
    #print(reduce(r2,list(m2,list(l[0]))))
    print(reduce(r2,list(map(m2,l[0])))+reduce(r2,list(map(m2,l[1])))/pow(10,len(l[1])))




#对于函数名相同的函数或者变量来说，先以最新的为主，当最新的被del掉，才会以内置的为主。
if __name__ == '__main__':
    map_reduce_practice("233.334444")