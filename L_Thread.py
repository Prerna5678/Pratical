from threading import Thread
import time

def user_login(username,email,password):
    print(f"{username},{email}")

    time.sleep(2)
    
    if password=="12345":
        print(f"{username} has login succesfully")

    else:
        print(f"{username} invalid password")

users=[
    ("Alice","alice@gmail.com","12345"),
    ("Bob","bob@gmail.com","abcde"),
    ("Charlie","charlie@gmail.com","12345"),
    ("David","david@gmail.com","12345"),
    ("Eva","eva@gmail.com","12345")
]

threads=[]

for user in users:
    t=Thread(target=user_login,args=user)
    threads.append(t)
    t.start()

print("Main program finished! (users are logged in ....)")