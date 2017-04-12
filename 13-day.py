from datetime import datetime,timedelta,timezone
import enum


def Display_time():
    print(datetime.now())
    print(type(datetime.now()))
    dt=datetime(2019,12,2,23,4,5)
    print(datetime(2019,12,2,23,4,5))
    print('--------------------timestamp-------------------')
    print(dt.timestamp())
    print('-------------------timestamp 转化成标准时间-----------')
    print(datetime.fromtimestamp(datetime(2016,12,3,22,21,23).timestamp()))

def do_time():
    print('str --> datetime')
    print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))
    print(datetime.now().strftime('%y  %b %d '))
    print(datetime.now()+timedelta(hours=10,days=1))

#时区时间，互相转换，必须先拿到utc时间，然后换成带时区的utc时间，在进行时区转换，时区转换用astimezone
def Time_zone():
    dz=datetime.utcnow()
    dt=dz.replace(tzinfo=timezone.utc)
    bj=dt.astimezone(timezone(timedelta(hours=8)))
    print(bj)


#拿到的时间都是不带时区的，通过replace转换成时区的，然后在通过时区转换成所需要的时区
#把不带时区的time转换成带时区的，接下来通过带时区的转换成标准时区，转换成带时区调用replace函数

def to_timestamp(dt_str,tz_str):
    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    dz=dt.replace(tzinfo=timezone(timedelta(hours=int(tz_str[4]))))
    return dz.timestamp()





if __name__ == '__main__':
    Time_zone()
    t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    assert t1 == 1433121030.0, t1
    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    assert t2 == 1433121030.0, t2
    print('Pass')