# __author__: liqinsong
# data: 2019/1/7

import threading

gLock = threading.Lock()  # 创建锁

VALUE = 0

def add_value():
    global VALUE

    gLock.acquire()
    for x in range(1000000):
        VALUE += 1
    gLock.release()
    print(VALUE)


def main():
    for x in range(2):
        t = threading.Thread(target = add_value)
        print(t.name)
        t.start()


if __name__ == '__main__':
    main()

