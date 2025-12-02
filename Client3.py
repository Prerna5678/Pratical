import socket

host='192.168.29.63'
port=1000

s = socket.socket()
s.connect((host,port))

while True:
    msg = s.recv(2024)
    print(msg.decode())

    if msg.decode() == "bye":
        break

    msg2 = input("Enter the message")
    s.send(msg2.encode())

    if msg2.encode() == "bye":
        break