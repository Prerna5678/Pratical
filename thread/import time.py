import time
from threading import Thread


class Task1(Thread):
    def disp1(self):
        print("Hi from disp1")
        time.sleep(1)
        print("Bye from disp1")

    def run(self):
        disp1()
