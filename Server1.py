import socket

host = socket.gethostname()
port = 1000

print(host,port)

s = socket.socket()
s.bind((host,port))
s.listen(1)
s.accept()

print("connected server side...")

