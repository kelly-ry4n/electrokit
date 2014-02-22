
import socket

s = socket.socket()
host = socket.gethostname()
port = 1337

s.bind((host,port))

s.listen(5)

while True:
	c, addr = s.accept()
	c.recv(50)
	print 'Got connection from {}'.format(addr)
	c.send('{"FUCK":"SOCKETS"}')
	c.close()