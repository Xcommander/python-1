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
#也就是unicode和utf-8可以相互转换，utf-8对于汉字用三个字节，所以中文最好读取用utf-8，然后通过unicode来转换。因为python3字符串是unicode表示的
#在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
#编码是指将字符改成bytes给计算机识别，也就是encode，decode解码，就是将bytes，改成str，显示出来
def str():
    print(ord('A'))
    print(chr(97))
    print('闫苏婉'.encode('utf-8'))
    print(b'\xe9\x97\xab\xe8\x8b\x8f\xe5\xa9\x89'.decode('utf-8'))


str()
