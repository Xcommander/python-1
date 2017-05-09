import base64


def base64_test():
    s = base64.b64encode(b'binary\x00string')
    print(s)
    print(base64.b64decode(s))
    k = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
    print(k)
    print(base64.urlsafe_b64decode(k))
    f = base64.urlsafe_b64encode("在python中使用BASE 64编码".encode('utf-8'))
    print(f)
    print(base64.urlsafe_b64decode(f).decode('utf-8'))


def safe_base64_decode(s):
    if isinstance(s, bytes):
        k = len(s) % 4
        if k == 0:
            b = base64.b64decode(s)
        else:
            tmp = b'=' * k
            b = base64.b64decode(s + tmp)

        return b
    else:
        return False


if __name__ == '__main__':
    assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
    assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
    print(base64.urlsafe_b64encode(b'abcd'))

