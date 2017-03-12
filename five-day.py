# 此文讲的是模块概念。
# 每一个包名，必须含有__init__.py，不然不能叫包，对于__init__.py文件来说，它的模块名就是他的包名，对于非init文件，那么就是模块名等于
# 包名加上一个文件名
import sys


def sys_test():
    # argv这个变量使用list存储了命令行的所有参数，比如python3 hello.py xxx，此时参数就是hello，和xxx，因为第一个参数是始终指向的
    # 是该py的文件名，剩下的就是命令行传入的参数。所以说argv至少有一个参数
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello world %s' % args[1])
    else:
        print('too many arguments')


# __name__ == '__main__'的含义是，当我们直接执行这个文件的时候，此时python就会把__name__设置为__main__，此时就会执行，这样方便我们
# 单个模块的调试。当我们从外部导入某块的时候，此时的__name__就是这个文件的名字而不是__main__
# 公开函数或者变量，其前面不加下划线，但是前面加了下划线（后面不加下划线）表示非公开的变量

if __name__ == '__main__':
    sys_test()
