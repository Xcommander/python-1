# struct test，把字节转换成数据，以及数据转换成字节。
# >把数据转换成二进制字节，<是把二进制数据转换成数据
import os
import struct


def struct_test():
    path = os.getcwd()
    print(path)
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == ".bmp":
            with open(file, "rb") as f:
                b = f.read(30)
                x = struct.unpack("<ccIIIIIIHH", b)
                if x[0] == b'B' and x[1] == b'M':
                    print("大小为%s * %s,颜色数为%s" % (x[6], x[7], x[9]))

    pass


import hashlib


def hashlib_test():
    md5 = hashlib.md5()
    md5.update("I'am xulinchao".encode("utf-8"))
    md5.update("I'am yansuwan".encode("utf-8"))
    print(md5.hexdigest())
    pass


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
db_src = {
    "michael": "123456",
    "bob": "abc999",
    "alice": "alice2008"
}

# 没使用一次hashlib.md5都要重新获取实例
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode("utf-8"))
    return md5.hexdigest()


def login(user, password):
    if db[user] == calc_md5(password):
        print("%s 登录成功" % user)
    else:
        print("%s 登录失败" % user)

def start_login():
    for key,value in db_src.items():
        login(key,value)


if __name__ == '__main__':
    start_login()
