'''
这是I/0测试章节
'''


# 在python，文件或者字串读到内存中，最终都是unicode编码，在内存中。要显示什么，如何显示，就是将unicode流进行对应格式的编码，如
# str.encode('utf-8'),就是将unicode编码成utf-8来显示。然后读到内存中，就是要转化成unicode,用decode（xx），意思就是将编码xx，转化
# 成unicode
def openfile():
    try:
        f = open('C:/Users/xulinchao/PycharmProjects/liaoxuefeng/xlc.txt', 'r', encoding='utf-8', errors='ignore')
        str = f.read()
        print(str)
    finally:
        if f:
            f.close()


def openfile2():
    with open('C:/Users/xulinchao/PycharmProjects/liaoxuefeng/xlc.txt', 'rb') as f:
        print(f.read())


def writefile():
    # 写入字串的话，会直接将内存中的字符写进去，所以说什么样的编码，就会怎么样写进去。
    with open('write', 'a+') as f:
        f.write('just do it!!!')
        print(f.read())


from io import StringIO


def OpenString():
    f = StringIO()
    f.write('Hi')
    f.write(',')
    f.write('Yai')
    # print(f.getvalue())
    f.write('\nxcommander......\nYes，I do it！')
    # 当f用来读的时候，stream的position已经到了写的最后一个位置，所以readline读出来是空的，只需要重置位置即可，seek(0)，回到写的第一个
    #
    # print(f.getvalue())
    xlc = StringIO("OMG!\nYes,Baby!\nFuck me,plz!")
    # print(xlc.getvalue())
    while True:
        x = xlc.readline()
        # print(x)
        if x == '':
            break
        print(x.strip())
    f.seek(0)
    while True:
        x = f.read()
        if x == '':
            break
        print(x.strip())
    # strip()函数是跳出首尾空格
    xlc.write('\nxcommander......\nYes，I do it！')
    print('--------------------------------------test-1------------------')

    ysw = StringIO("1\n2\n3")
    # 如果预先定义个字符流，然后再写，可能会覆盖，这时候，我们就可以通过xlc.tell()知道其光标所在位置，然后将光标拨到那个位置,进行
    # 读写
    ysw.seek(6)
    ysw.write(" 4\n 5\n 6")
    print('-----------------------location position is %d' % ysw.tell())

    while True:
        x = ysw.read()
        if x == '':
            break
        print(x.strip())
    print('----------------------test--------------------------')
    print(ysw.getvalue())
    print('-----------------------end---------------------------')


from io import BytesIO


def OpenBytes():
    b = BytesIO()
    # python 默认为unicode，所以一般字串都是unicode，所以中文也是unicode
    b.write('闫苏婉'.encode('utf-8'))
    print(b.getvalue())
    b1 = BytesIO(b'\xe9\x97\xab\xe8\x8b\x8f\xe5\xa9\x89')
    print(b1.getvalue())
    print(b1.getvalue().decode('utf-8'))


import os
import shutil


def operateSO():
    print(os.name)
    # 环境变量都是以字典形式存储的
    print(os.environ)
    print(os.environ.get('PATH'))
    # 查看当前目录的绝对路径
    # 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
    print(os.path.abspath('.'))
    # jion只不过显示出即将新建目录的名字，并不会创建目录
    s = os.path.join(r'C:\Users\xulinchao\PycharmProjects', 'yansuwan')
    # 创建目录用mkidr
    # 删掉一个目录
    if os.path.isdir(s):
        os.rmdir(s)
    else:
        os.mkdir(s)
    # 注意合并路径要用join，分割路径用split,split是以路径符作为分割，将最后一个和前面分开，形成元组。而splitext()是以文件的后后缀名
    # 将路径分成两部分，一个是后缀名，以及前面
    k = r'C:\Users\xulinchao\PycharmProjects\liaoxuefeng\xlc.txt'
    g = r'C:\Users\xulinchao\PycharmProjects\liaoxuefeng\xulinchao.txt'
    l = r'C:\Users\xulinchao\PycharmProjects\liaoxuefeng\yansuwan.txt'
    print(os.path.split(k))
    print(os.path.splitext(k))
    print('-----------------------------------------------remove-----------------------')
    if os.path.isfile(k) and not os.path.isfile(g):
        os.rename(k, g)
    else:
        with open(k, 'w', encoding='utf-8') as f:
            f.write('许林超')
    if os.path.exists(l):
        os.remove(l)
    else:
        with open(l, 'w', encoding='utf-8') as f:
            f.write('闫苏婉')
    oldpath = os.getcwd()
    os.chdir('../')
    dir = [x for x in os.listdir('.') if os.path.isdir(x)]
    print(dir)
    os.chdir(oldpath)
    pyfile = [x for x in os.listdir('.') if os.path.splitext(x)[1] == '.py']
    print(pyfile)


def file_practice(s):
    if os.path.isdir(s):
        oldpath = os.getcwd()
        os.chdir(s)
        for i in os.listdir('.'):
            info = os.lstat(os.path.join('./', i))
            print(i, info, sep='  ')
    else:
        print('your path  is wrong!!!')


def file_practice2(s, k):
    if os.path.isdir(s):
        oldpath = os.getcwd()
        os.chdir(s)
        for i in os.walk(os.path.join(os.getcwd(), '.'), True):
            for j in i[2]:
                if j.find(k) != -1:
                    print(os.path.join(os.getcwd(), j))

                else:
                    pass

        os.chdir(oldpath)
    else:
        print('your path is wrong~~~')


import os, os.path


def search(path, s):
    for x in os.listdir(path):
        fp = os.path.join(path, x)
        if os.path.isfile(fp) and s in x:
            print(fp)
        elif os.path.isdir(fp):
            search(fp, s)


def new_practice(path, s):
    if os.path.isdir(path):
        for i in os.listdir(path):
            fp = os.path.join(path, i)
            # print(fp)
            if os.path.isfile(fp):
                if str(i).find(s) != -1:
                    print(fp)
            elif os.path.isdir(fp):
                new_practice(fp, s)

    else:
        pass


# python中把变量从内存中变成可存储或者可传输的过程叫做序列化，序列化后，就可以把对象内容写入磁盘，或者网络传输到起其他机器中去
# 反之，把序列化对象变成内存中变量叫做反序列化。
# pickle 序列化
import pickle


def pickle_test():
    d = dict(name='bob', age=20, socre=99)
    print(os.getcwd())
    fp = os.path.join(os.getcwd(), 'xxx.txt')
    if not os.path.isfile(fp):
        # 序列化首先要先dumps，序列化成二进制bytes，然后二进制文件写进去
        with open(fp, 'wb') as f:
            pickle.dump(d,f)
            #f.write(pickle.dumps(d))

    else:
        with open(fp, 'rb') as s:
            print(s.read())

        os.remove(fp)
def pickle_f():
    fp = os.path.join(os.getcwd(), 'xxx.txt')
    if os.path.isfile(fp):
        with open(fp,'rb') as f:
            d=pickle.load(f)
            print(d)


class Student(object):
    def __init__(self,name,age,socre):
        self.name=name
        self.age=age
        self.socre=socre
# json序列化,json是许多语言都认可的
# 注意json序列化一个对象的时候，需要定制规则，也就是函数,反序列化也需要定制规则，也就是函数
def student(obj):
    return {
        'name':obj.name,
        'age':obj.age,
        'socre':obj.socre
    }
def student_s(obj):
    print(obj)
    return Student(obj['name'],obj['age'],obj['socre'])


def json_object():
    s=Student('Bob',23,88)
    #print(json.dumps(s,default=student))
    fp=os.path.join(os.getcwd(),'ysw.txt')
    if not os.path.exists(fp):
        with open(fp,'w',encoding='utf-8') as f:
            json.dump(s,f,default=lambda obj:obj.__dict__)

def json_f():
    fp = os.path.join(os.getcwd(), 'ysw.txt')
    if os.path.exists(fp):
        with open(fp,'r',encoding='utf-8') as f:
            #print(f.read())
            s=json.load(f,object_hook=student_s)
            print(s)


import json
def json_s():
    d=dict(name='bob', age=20, socre=99)
    print(json.dumps(d))





if __name__ == '__main__':
    # print('------------------------------StringIO-------------------------------')
    # OpenString()
    # print('------------------------------BytesIO--------------------------------')
    # OpenBytes()
    # print('------------------------------operate file--------------------------')
    # operateSO()
    # print('---------------------------------test--------------------------------')
    # file_practice('../')
    # print('---------------------------------test2-------------------------------')
    # file_practice2(os.getcwd(), 'xulinchao')
    # print('---------------------------------test3-------------------------------------')
    # new_practice(os.getcwd(), 'xulinchao')
    # print('-----------------------------------test4--------------------------------')
    # search(os.getcwd(), 'xulinchao')
    # print(os.getcwd())
    # pickle_test()
    # pickle_f()
    # json_s()
    # print('xlc')
    json_object()
    # json_f()

    pass
