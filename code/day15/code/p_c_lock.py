# __author__: liqinsong
# data: 2019/1/8

import threading
import random
import time


GMoney = 1000


class Prodcut(threading.Thread):
    def run(self):
        pass


class Consumer(threading.Thread):
    def run(self):
        pass


def main():
    for i in range(5):
        t = Prodcut()
        t.start()
