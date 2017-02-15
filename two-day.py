#-----------------函数调用-----------------
#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
#函数可以同时返回多个值，但其实就是一个tuple。
import math
def fuction_d():
    a=abs
    print(a(-100))
    print('-------------hex()测试-----------------')
    n=125
    n2=12
    print(hex(n),hex(n2),sep='\n')



def quadratic(a,b,c):
    x1=(-b+math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
    x2=(-b-math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
    if x1 and x2 is not None:
        pass
    else:
        print('error')
    return x1,x2


def add_end(L=[]):
    L.append("END")
    return L

def add_end_s(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L


#这里连续调用两次，产生的结果却不一样。因为python在运行时，已经确认好默认参数了，因为L是变量指向的始终是[]列表的地址，当第一次调用时[]列表
#的内容发生了改变，但是L的指向没变，所以第二次调用时，仍然采用的是默认参数L，而L此时指向的列表此时发生了改变，所以两次结果不一样。
#所以说默认参数必须指向不变对象
def calc(numbers):
    #像这种写法，基本确定为传递的参数是一个list or tuple
    sum =0
    for n in numbers:
        sum +=n

    return sum
#print(calc([23,3,4,5]))
def calc_c(*numblers):
    #像第二种做法基本上是通用做法，只需要加上*number即可，输入的参数不需要是一个list or tuple
    sum =0
    for n in numblers:
        sum +=n
    return sum

def person(name,age,**kk):
    #**表示关键字参数，通过key-value来表示，所以说**表示字典，而*表示list or tuple。注意所有参数传递，都是一个copy，并不会影响后面的值
    #a关键字参数必须传递的是一个键值对，也就是说，你传递单个关键字，要写号key=value这样传递。也就是关键字函数调用时，要么传递一个字典，要么
    #指定好键值对。而关键字函数定义时，对于分为：可变长关键参数函数，不可定长关键参数函数。可变长参数是**,不可定长需要加一个*，后面跟着
    #参数名
    print('name is '+name,'age is '+age,'other is ',kk)

    for i in kk:
        print(kk.get(i))

def person_B(age,name,*,city,job):
    print(age,name,city,job)

#这个是递归
def fact(n):
    if n==1 :
        return 1
    return n*fact(n-1)

print(fact(5))


print('------------尾递归测试------------')
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式.一旦有表达式，就变成调用了。形如递归，stack来管理
def fact_1(n):
    return fact_iter(n,1)

def fact_iter(m,product):
    if m==1:
        return product
    return fact_iter(m-1,m*product)
print(fact_1(5))
""""
son={'city':'beijing','home':'anhui'}
son['111']=222
person_B('yansuwan','2',city='22',job='44')
"""

