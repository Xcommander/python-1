# ------------数据类型及变量-----------#
"""
name=input("请输入您的名字：\n")
#print函数中，一个逗号，打印出来就是一个空格
print("hello,"+name)

print("1024*768=",1024*768)
"""


# print('\\\t\\')
# print("i'm lean")
# print(r'\\\\a\\')
# '''...'''表示多行内容
# python属于动态语言，因为它的变量类型是不固定的，可以赋值任意变量类型；而java是静态语言，必须定义类型才能赋值
# 在Python中，通常用全部大写的变量名表示常量,但是这个只是约定俗成的写法而已，重新赋值，仍然可以改变
# 除法/表示精确除法，而//表示取整数部分--地板除，%表示取余
def shuju():
    n = 123
    f = 456.789
    s1 = 'Hello, world'
    s2 = 'Hello, \'Adam\''
    s3 = r'Hello, "Bart"'
    s4 = r'''Hello,
    Lisa!'''
    print(n)
    print(f)
    print(s1)
    print(s2)
    print(s3)
    print(s4)


'''
python支持多种数据类型，在计算机内部，可以把任何数据都看成一个“对象”，而变量就是在程序中用来指向这些数据对象的，对变量赋值就是把数据和变量给关联起来。
注意：Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648-2147483647。
Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。
'''


# --------字符串和编码------#
# 在计算机内存中，字符统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。因为utf-8节约空间；
# 也就是unicode和utf-8可以相互转换，utf-8对于汉字用三个字节，所以中文最好读取用utf-8，然后通过unicode来转换。因为python3字符串是unicode表示的
# 在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
# 编码是指将字符改成bytes给计算机识别，也就是encode，decode解码，就是将bytes，改成str，显示出来
def str():
    print(ord('A'))
    print(chr(97))
    print('闫苏婉'.encode('utf-8'))
    print(b'\xe9\x97\xab\xe8\x8b\x8f\xe5\xa9\x89'.decode('utf-8'))


# ----------list and tuple ---------
# list。list是一种有序的集合，可以随时添加和删除其中的元素。
# list 删除一个元素用的是pop，弹出栈
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。tuple不可变是指指向不变，可能指向的对象改变，
# 导致tuple元素值发生了改变,但是tuple的指向仍然没有发生改变
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
def list_and_tuple():
    print('########################list 相关测试######################')
    classmates = ['Michael', 'Bob', 'Tracy']
    print('-------倒数测试--------')
    print(classmates[-1])
    print('-------可变长度测试-----')
    classmates.append(1)
    print(classmates[0:])
    print('-------替换测试--------')
    classmates[1] = 'xulinchao'
    print(classmates[0:])
    print('------多维数组测试------')
    p = [2, 3, 4]
    classmates[1] = p
    print(classmates[0:])
    print(classmates[1][0:])

    print('########################tuple 相关测试######################')
    classTuple = (1, p, 2)
    print(classTuple)
    p[2] = 5
    print(classTuple[1][2])

    print('--------------综合练习----------------')
    L = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', 'Ruby', 'PHP'],
        ['Adam', 'Bart', 'Lisa']
    ]
    # print apple
    print('Apple is ', L[0][0])
    # print Python
    print('Python is', L[1][1])
    # print Lisa
    # L.pop([1][0])
    L.insert(1, 5)
    print('Lisa is', L)

    print([0][0])


# -------------if and while --------------#
def if_while():
    height = 1.75
    weight = 80.5
    # **表示乘方，pow(x,y)表示x的y次方
    bmi = 80 / pow(1.75, 2)
    print('bmi is %.2f' % bmi)
    if bmi >= 32:
        print('严重肥胖')
    elif bmi >= 28:
        print('肥胖')
    elif bmi >= 25:
        print('过重')
    elif bmi >= 18.5:
        print('正常')
    else:
        print('过轻')

    names = ['Michael', 'Bob', 'Lisa']
    for name in names:
        print(name)

    print('-----------range测试--------')
    # range是一个列出一个范围的值,返回来是一个对象，然后通过list转化成列表
    sum = 0
    for i in list(range(101)):
        sum += i
    print(sum)

    # while使用,+=表示先加后复制。而=+表示先复制，再加
    n = 1
    sum = 0
    while n <= 100:
        sum = sum + n
        n += 1
    else:
        print(sum)

    # break是跳出整个循环，而continue是跳出当前循环
    print('-----------------打印0-100质数之和------------------')
    sum = 0
    for i in list(range(101)):
        if i % 2 == 0:
            continue
        else:
            sum = sum + i

    print(sum)


def dict_set():
    print('-----------------dict 测试-----------------')
    # 字典是靠键-值来查找的，通过key来找到value
    # 所以，dict是用空间来换取时间的一种方法。
    #第一条就是dict的key必须是不可变对象
    #这个通过key计算位置的算法称为哈希算法（Hash）。
    #要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，
    # 因此，可以放心地作为key。而list是可变的，就不能作为key：
    #dict 中的key值是不存在重复一说，当你定义两个相同的key值，而value值不一样，其实就是一个key值，（系统会自动检查有没有重复的，
    #有的话，就会用存在的key ），对应两个不同的value，而key讲究
    #一对一，就会key的指向就会指向最新的value地址。
    #简而言之，重复的key值会用后面的key-value替换前面的key-value,所以说key重复不了
    nameDict={'Michael':96,'Bob':67,'Lisa':88,'Michael':99,(2,2):(2,)}
    #for in得出的是key值，非key-value值
    nameDict.pop('Michael')
    nameDict[4]='x;c'

    for i in nameDict:
        print(nameDict.get(i,-1))

    print(len(nameDict))
    #print('Hi,Michael ',nameDict['Michael'])

    print('----------------------------set 测试------------------------------')
    #set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
    #要创建一个set，需要提供一个list作为输入集合
    s=set([1,2,3])
    s.add(4)
    print(s)
    s.remove(4)
    print(s)
    #set可以看成数学意义上的无序和无重复元素的集合
    #set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，
    # 所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
    #由于tuple是不可变长的，所以tuple是可以作为key,但是这个tuple是不能含有list的，因为有list代表tuple虽然指向不变，但是结果变了
    #所以hash值也就变了，所以说对已dict和set来说，不可变长是不仅指向不变，而且元素内容也不变。对于tuple来说，不可变长是指指向不变，
    #内容变不变无所谓
    #set的输入是一个list，而这个list不能有可变长的存在，这里的list是指一个可迭代的参数，可迭代的参数其实就是list
    s1=set([0,1,2,3])
    s2=set([2,3,4,5])
    print(s1&s2)
    print(s1|s2)
    s3=set([1,2,3,(3,2,3)])
    print(list(s3))
    print(s3)
    s4=(1,2,[2,3])
    s4[2].append(4)
    print(s4)
    s5=set('sdadasd')

    print(s5)


    print('---------------str不可变的讨论------------------')
    a='adb'
    print(a.replace('a',"A"))
    #上面这个结果虽然是Adb，但是adb没有变，只不过a.replace()后，会返回一个字串，也就是系统在内存中创建了Adb这个字串，与adb毫无关系
    #也就是adb的值仍然没做出任何变化，而a指向adb仍然不变，也就是a的值不变
    print(a)








dict_set()
