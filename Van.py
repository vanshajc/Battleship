
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
s.send('1,0 1,1')
time.sleep(0.1)
s.send('2,0 2,1')
time.sleep(0.1)
s.send('2,0 2,1')
time.sleep(0.1)
s.send('2,0 2,1')
time.sleep(0.1)
s.send('2,0 2,1')
time.sleep(0.1)
s.send('2,0 2,1')
time.sleep(0.1)
s.send('2,0 2,1')

data = s.recv(1024)
print data