# __str__
class Student(object):
    def __init__(self,name):
        self.name=name

if __name__ == '__main__':
    s=Student('Michael ')
    print(s)