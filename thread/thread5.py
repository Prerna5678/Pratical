import threading 

#help(threading)
#print(dir(threading))
'''
for i in dir(threading):    
    print(i)
'''
print(threading.current_thread().name)
print(threading.current_thread().getName)