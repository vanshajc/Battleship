import socket
import sys
import time
import os
import subprocess as sp
import board
import player
from thread import *
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5003 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
s.listen(2)
print 'Socket now listening'

print 'Looking for 2 players.'
p1 = s.accept();

print 'Found 1 Player. Looking for 1 player.'
p2 = s.accept();
 
print '2 Players Found. Game will begin.'

p1[0].send('Requesting List of Ships')
p2[0].send('Requesting List of Ships')
d1 = p1[0].recv(1024)
print d1

s.close()

