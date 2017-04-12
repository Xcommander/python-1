from datetime import datetime


def Display_time():
    print(datetime.now())
    print(type(datetime.now()))
    dt=datetime(2019,12,2,23,4,5)
    print(datetime(2019,12,2,23,4,5))
    print('--------------------timestamp-------------------')
    print(dt.timestamp())


if __name__ == '__main__':
    Display_time()