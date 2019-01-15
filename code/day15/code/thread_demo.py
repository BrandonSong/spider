# __author__: liqinsong
# data: 2019/1/1

import threading
import time


class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print("%s正在写代码" %threading.current_thread())
            time.sleep(1)

class DrawThread(threading.Thread):
    def run(self):
        for x in range(3):
            print("%s正在画图" %threading.current_thread())
            time.sleep(1)


def main():
    t1 = CodingThread()
    t2 = DrawThread()

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()