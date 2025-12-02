from threading import Thread, current_thread


def method(a, b, c):
    for i in range(a, b + 1, c):
        print(current_thread().getName, i)


t1 = Thread(target=method, name=" first thread", args=(1, 10, 1))

t1.start()
t1.name
