import time
from threading import Thread,current_thread

def method1():
    t11 = Thread()
    print("t11 :",t11.isDaemon)
    

def method2():
    t22 = Thread()
    print("t22 :",t22.isDaemon)    

print("welcome")
t1  = Thread(target=method1,name="firest thread",daemon=True)
t2  = Thread(target=method2,name="second thread",daemon=False)


t1.start()
t2.start()

print("bye")
#print(t1.isDaemon())
#print(t2.isDaemon())