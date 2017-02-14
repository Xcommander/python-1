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
    print()
