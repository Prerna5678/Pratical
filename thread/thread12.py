from threading import Thread, current_thread


class MyThread(Thread):
    pass


c1 = MyThread()

c1.start()
print(c1.name)
print(c1.getName)
