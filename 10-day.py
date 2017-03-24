'''
这是I/0测试章节
'''


#在python，文件或者字串读到内存中，最终都是unicode编码，在内存中。要显示什么，如何显示，就是将unicode流进行对应格式的编码，如
# str.encode('utf-8'),就是将unicode编码成utf-8来显示。然后读到内存中，就是要转化成unicode,用decode（xx），意思就是将编码xx，转化
#成unicode
def openfile():
    try:
        f = open('C:/Users/xulinchao/PycharmProjects/liaoxuefeng/xlc.txt', 'r', encoding='utf-8',errors='ignore')
        str = f.read()
        print(str)
    finally:
        if f:
            f.close()

def openfile2():
    with open('C:/Users/xulinchao/PycharmProjects/liaoxuefeng/xlc.txt', 'rb') as f:
        print(f.read())

def writefile():
    #写入字串的话，会直接将内存中的字符写进去，所以说什么样的编码，就会怎么样写进去。
    with open('write','a+') as f:
        f.write('just do it!!!')
        print(f.read())

from io import StringIO
def OpenString():
    f=StringIO()
    f.write('Hi')
    f.write(',')
    f.write('Yai')
    print(f.getvalue())
    f.write('\nxcommander......\nYes，I do it！')
    while True:
        x=f.readline()
        if x== '':
            break;
        print(x)



if __name__ == '__main__':
    openfile()
    openfile2()
    writefile()
    print('------------------------------StringIO-------------------------------')
    OpenString()
