from threading import Thread
import time

Cust_login=[{"username":"prerna","password":12},
            {"username":"namarata","password":23}
            ]

def login():
    for i in Cust_login:
        
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        Cust_login = {'username': username, 'password': password}
    
'''
def login1():
    for i in range(2):
        username = input("Enter your username 2: ")
        password = input("Enter your password 2: ")
        time.sleep(1)
        Cust_login = {'username': username, 'password': password}
        print(Cust_login)
'''
t1=Thread(target=login,kwargs={"username":"prerna","password":"12"})
#t2=Thread(target=login1)
t1.start()
#t2.start()