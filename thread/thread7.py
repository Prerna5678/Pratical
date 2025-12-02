import time
from threading import Thread,current_thread

def method1():
    for i in range(1,6):
        print(i)
        #time.sleep(1)
    

def method2():
    for i in range(10,51,10):
        print(i)
        #time.sleep(1)
    
print("welcome")
t1  = Thread(target=method1,name="firest thread",daemon=True)
t2  = Thread(target=method2,name="second thread",daemon=True)


t1.start()
t2.start()

print("bye")
print(t1.isDaemon())
print(t2.isDaemon())