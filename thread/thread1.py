from threading import Thread
import time


def method1():
    print("Enter in method1")
    time.sleep(5)
    print("Exit from method1")


def method2():
    print("Enter in method2")
    time.sleep(5)
    print("Exit from method2")


def method3():
    print("Enter in method3")
    time.sleep(5)
    print("Exit from method3")


t1 = Thread(target=method1)
t2 = Thread(target=method2)
t3 = Thread(target=method3)
t1.start()
t2.start()
t3.start()
