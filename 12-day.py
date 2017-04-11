# ^行的开头.^\d表示以数字开头。\d表示数字开头，\w表示以数字或者字母开头
# $表示行的结尾。\d$表示以数字结尾
# 这里行首和行尾表示
# (A|B)表示匹配A or B
# \s表示空格
# 对于特殊字符,用\来转义
# []表示一个值，只能有一个值
# ()表示要提取的分组
# *表示0次或者多次


import re, time


def match():
    start = time.time()
    for i in range(1, 4000):
        if (re.match(r'^[\d+]{3}-[\d+]{3,8}$', '021-1123')):
            pass
        else:
            print('error')
            break
    end = time.time()
    print('直接匹配的时间为%f' % (end - start))
    pass


def compile_match():
    start = time.time();
    express = re.compile(r'^[\d+]{3}-[\d+]{3,8}$')
    for i in range(1, 4000):
        if (express.match('021-1123')):
            pass
        else:
            print('error')
            break
    end = time.time()
    print('编译之后匹配的时间为%f' % (end - start))
    pass


def expression_practice(email):
    # someone@gmail.com
    print(re.match(r'^.*@[\]',email))
    if re.match(r'^(\w+)com$',email):
        print('正确，输入的邮箱：%s'%email)
    else:
        print('错误，输入的邮箱：%s' % email)

    pass


if __name__ == '__main__':
    print(re.match(r'^\d{3}-\d{3,8}$', '001-2335'))
    test = '用户输入的正则表达式'
    if re.match(r'正则表达式', test):
        print('OK')
    else:
        print('Failed')
    print(re.match(r'^[0-9a-z]+\s+\d{0,9}py$', '22 12py'))
    print(re.split(r'[\s]+', 'a b    d  c'))
    print(re.split(r'[\s\,\;]+', 'a,c,,ddd,p;ddd fff'))
    print(re.match(r'python', 'python is best'))
    m = re.match(r'^(\d{3})(-)(\d{3,9})$', "003-2222")
    # group(0)始终表示原始字符,分组的时候注意，先整体匹配，在通过()，来分割成小组
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
    # groups()表示打印所有的分组，通过元组表示
    print(m.groups())
    t = '22:52:14'
    time1 = re.match(r'^(0[0-9]|1[0-9]|2[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:'
                     r'(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
    print(time1.groups())
    # 正则表达式默认是贪婪匹配
    print(re.match(r'^(\d+)(0*)$', '123400').groups())
    # 贪婪匹配后加上？表示非贪婪匹配，尽量少匹配,一般以后面表达式优先选择，后面的表达式，一般以$优先，按照贪婪匹配，没有$,
    # 后面的也按照前面的非贪婪匹配
    # 当一个表达式使用非贪婪匹配，那么后面的部分是否有$，有则先按照后面贪婪匹配，在决定前面的非贪婪，如果没有，那么后面和前面都是非贪婪
    # 匹配
    print(re.match(r'^(\d+?)(0*)$', '23300').groups())
    # 正则表达式match的时候做了两个事，先预编译正则表达式，然后在匹配，当我们这个正则表达式用几千次的，可以先预编译过来在匹配
    # python 中字符串前面加上r'xxx'是不转义特殊字符的，例如'\t','\n',r'\n'之后,变成了正常字符。对于正则表达式来说，先加r，是为了先
    # 不转义，然后在根据得到的字符串去匹配.r'xxx'去掉转义，得到一个新的表达式，然后用新的表达式和字符去匹配
    match()
    compile_match()
    #expression_practice('xulinchao@wind-mobi.com')
    print(re.match(r'\\n',r'\n'))
    print(r'\n')

    pass
