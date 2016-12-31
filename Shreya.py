#Shreya.py
import socket 
HOST = '192.168.1.174'    # The remote host
PORT = 5003              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Connecting...')
s.connect((HOST, PORT))
data = s.recv(1024)

print("Data") 
s.sendall('2,2 7,7') 
s.sendall('1,0 5,1')
s.sendall('3,4 6,7')