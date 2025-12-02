from threading import Thread, current_thread


class MyThread(Thread):
    def __init__(self, a, b, c):
        # super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def run(self):
        for i in range(self.a, self.b + 1, self.c):
            print(i)


c1 = MyThread(10, 50, 10)

c1.start()
# print(c1.name)
# print(c1.getName)
