#---python 中的exception
def exception_s():
    try:
        print('try..........')
        i = 10 // 0
        print('result :', i)
    except ZeroDivisionError as e:
        #logging 只是记录错误，而不会干扰代码执行，而raise抛出错误后，没有被捕捉到就会报错，代码就会停止。
        logging.exception(e)
    finally:
        print('finally .....')


def foo(s):
    n=int(s)
    if n==0:
        raise ValueError('invalid value xlc : %s'%s)
    else:
        return 10/int(s)


def bar1(s):
    try:
        foo(s)
    except ValueError as v:
        print('Error is ',v)
        raise
    finally:
        pass

def bar(s):
    return foo(s)*2



def slang(s):
    x=int(s)
    assert x!=0,'x is zero!!!'
    return 10/x

def crab(s):
    n=int(s)
    logging.info('n=%d'%n)
    return 10/n

import logging
logging.basicConfig(level=logging.INFO)
if __name__ == '__main__':
    #bar1('0')
    crab('0')

