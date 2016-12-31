
import socket
import time

HOST = '192.168.1.174'    # The remote host
PORT = 5003              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Connecting...'
s.connect((HOST, PORT))
data = s.recv(1024)

print data

# do this for each ship location. 
s.send('0,0 0,1')
time.sleep(0.1)
s.send('1,0')
time.sleep(0.1)
s.send('2,0')
time.sleep(0.1)
s.send('3,0')
time.sleep(0.1)
s.send('4,0')
time.sleep(0.1)
s.send('5,0')
time.sleep(0.1)
s.send('6,0')
time.sleep(0.1)
s.send('7,0')

while 1:
	data = s.recv(1024)
	print data
	if (data == 'Game Over')
		break
	inp = raw_input("Enter a move:") #python 3 is input()
	s.send(inp)