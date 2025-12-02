import socket

host = socket.gethostname()
port=1000

s = socket.socket()
s.bind(host,port)
s.listen(1)
a,c = s.accept()

a.send("welcome to Prerna".encode())

print("server connected...")