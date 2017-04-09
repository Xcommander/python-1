import queue, random
from multiprocessing import freeze_support
from  multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


task_queue = queue.Queue()
result_queue = queue.Queue()

QueueManager.register('get_task_queue', callable=return_task_queue)
QueueManager.register('get_result_queue', callable=return_result_queue)

manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'xulinchao')

if __name__ == '__main__':
    freeze_support()
    manager.start()
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    for i in range(10):
        n = random.randint(1, 1000)
        print('put task %s' % n)
        task.put(n)

    print('try to get task ......')
    for i in range(10):
        try:
            n = result.get(timeout=10)
            print('Result %s' % n)
        except:
            print('queue empty')

    manager.shutdown()
    print('manager exit....')

    pass
