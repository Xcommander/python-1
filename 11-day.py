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


if __name__ == '__main__':
    subprocess_test()

    # fork_test()
    pass
