import time
from threading import Thread,current_thread

def method1():
    print("enter in method1",current_thread().name)
    time.sleep(1)
    print("exit from method1")

def method2():
    print("enter in method2")
    time.sleep(1)
    print("exit from method2")
    
def method3():
    print("enter in method3")
    print("exit from method3")
    time.sleep(1)
    
t1  = Thread(target=method1,name="firest thread")
t2  = Thread(target=method2,name="second thread")
t3  = Thread(target= method3)

t1.start()
t2.start()
t3.start()

print(t1.name)
print(t2.name)
print(t3.name)