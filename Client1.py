import socket

host='192.168.29.225'
port=1000

s = socket.socket()
s.connect((host,port))

msg = s.recv(1024)
print(msg.decode())


print("connected with client side")