#Shreya.py
import socket 
import time 
HOST = '192.168.1.174'    # The remote host
PORT = 5003              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Connecting...')
s.connect((HOST, PORT))
data = s.recv(1024)

print(data) 
s.send(('2,2 2,7').encode())
time.sleep(0.1)
s.send(('1,0 5,0').encode())
time.sleep(0.1)
s.send(('3,4 6,4').encode())