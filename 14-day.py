from collections import namedtuple,deque


def namedtuple_test():
    cricle = namedtuple("Cricle", ['x', 'y', 'z'])
    p=cricle(2,3,6)
    print(p.x,p.y,p.z)
    if isinstance(p,tuple):
        print('It\'s a tuple')

def deque_test():
    q=deque(['a','b','c'])
    q.append('d')
    q.appendleft('y')
    print(q)

if __name__ == '__main__':

    deque_test()
    l=list([1,2,3])
    print(l)
    for i in len(l):
        print(l[i])
        l.pop()
    print(l)
