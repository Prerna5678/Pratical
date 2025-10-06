from threading import Thread
import time


def method():
    for i in range(1, 6):
        time.sleep(2)
        print("method : ", i)


t = Thread(target=method)
t.start()

for i in range(10, 51, 10):
    print("method : ", i)
    time.sleep(1)
