import socket

host = socket.gethostname()
port = 9090

print(host,port)

s = socket.socket()
s.bind((host,port))
s.listen(1)
a,c = s.accept()

while True:
    msg = input("Enter the message")
    a.send(msg.encode())

    if msg == "bye":
        break

    msg2 = a.recv(1024)
    a.send(msg2.decode())

    if msg2.encode() == "bye":
        break

