import time
from threading import Thread


class Task1(Thread):
    def disp1(self):
        print("Hi from disp1")
        time.sleep(1)
        print("Bye from disp1")

    def run(self):
        self.disp1()


class Task2(Thread):
    def disp2(self):
        print("Hi from disp2")
        time.sleep(1)
        print("Bye from disp2")

    def run(self):
        self.disp2()


t1 = Task1()
t2 = Task2()

t1.start()
t2.start()
