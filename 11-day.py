# 进程
import os


def fork_test():
    print('Process (%s) start .....' % (os.getpid()))
    # fork会创造出两个进程，一个是子进程，一个是父进程，对于子进程来说，fork的结果是0，对于父进程来说，fork的结果是子进程的id，
    # 所以根据返回值不同，来判断子进程和父进程
    pid = os.fork()
    if pid == 0:
        print("I\'m child process (%s) and my parent process is (%s)" % (os.getpid(), os.getppid()))
    else:
        print("I\'m parent process (%s) and my child process is (%s)" % (os.getpid(), pid))


from multiprocessing import Process


def run_proc(name):
    print("Run child porcess %s(%s)" % (name, os.getpid()))


def parent():
    print("Run parent process %s" % os.getpid())
    childProcess = Process(target=run_proc, args=('test',))
    print('child process start.....')
    childProcess.start()
    childProcess.join()
    print('child process end......')


import time, os, random, multiprocessing


def long_time_task(name):
    print('Run task process id %s( %s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s run  %0.2f second' % (name, (end - start)))


from multiprocessing import Pool


def pool_test():
    print('parent process id %s ' % os.getpid())
    p = Pool(8)
    for i in range(6):
        p.apply_async(func=long_time_task, args=(i,))
    print('Waiting for all subprocessess done....')
    p.close()
    p.join()
    print('All subprocessess done....')


import subprocess


def subprocess_test():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)


# 进程通信,记住args=（）是传递参数的，针对这个子进程的函数体，传入的参数
def Queue_write(q):
    print('Process to write : %s' % os.getpid())
    for value in list('NCAA'):
        print("Put %s to queue....." % value)
        q.put(value)
        time.sleep(random.random())


def Queue_read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        print('Get %s from queue.....' % q.get(True))


from multiprocessing import Queue


def Queue_main():
    print('Mian process %s' % os.getpid())
    q = Queue()
    pw = Process(target=Queue_write, args=(q,))
    pr = Process(target=Queue_read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()


import threading


def loop():
    print('Thread %s is running' % threading.current_thread().name)
    n = 0
    while n < 5:
        n+=1
        print(n)
        print('Thread %s >> %s' % (threading.current_thread().name, n))
        time.sleep(1)


    print('Thread %s ended' % threading.current_thread().name)


def main_thread():
    print('Thread %s is running ' % threading.current_thread().name)
    t = threading.Thread(target=loop, name="LoopThread")
    t.start()
    t.join()
    print('Thread %s ended' % threading.current_thread().name)


if __name__ == '__main__':
    main_thread()

    # fork_test()
    pass
