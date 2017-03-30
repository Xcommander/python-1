# 进程
import os
def fork_test():
    print('Process (%s) start .....'%(os.getpid()))
    # fork会创造出两个进程，一个是子进程，一个是父进程，对于子进程来说，fork的结果是0，对于父进程来说，fork的结果是子进程的id，
    # 所以根据返回值不同，来判断子进程和父进程
    pid=os.fork()
    if pid==0:
        print("I\'m child process (%s) and my parent process is (%s)"%(os.getpid(),os.getppid()))
    else:
        print("I\'m parent process (%s) and my child process is (%s)"%(os.getpid(),pid))

if __name__ == '__main__':
    fork_test()