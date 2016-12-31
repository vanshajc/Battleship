import socket
import sys
import time
import os
import subprocess as sp
from board import Board
import player
from thread import *
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5003 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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

ships1 = []
ships2 = []
for i in range(8):
	d1 = p1[0].recv(1024)
	d2 = p2[0].recv(1024)
	print repr(d1)
	print repr(d2)
	s1 = []
	s2 = []
	for n in d1.split():
		s1.append((int(n[0]), int(n[2]), 'not hit'))
	for n in d2.split():
		s2.append((int(n[0]), int(n[2]), 'not hit'))
	ships1.append(s1)
	ships2.append(s2)

print 'Finished reading list of ships'

b1 = Board(ships1)
b2 = Board(ships2)

b1.printBoard()
print '---------------------------------'
b2.printBoard()
print '---------------------------------'

turn = 0
while 1:
	if turn%2 == 0:
		p1[0].send(b2.toString())
		d1 = p1[0].recv(1024)
		if not d1:
			break
		b2.update((int(d1[0]), int(d1[2])))
		print d1
	if turn%2 == 1:
		p2[0].send(b1.toString())
		d2 = p2[0].recv(1024)
		if not d2:
			break
		b1.update((int(d2[0]), int(d2[2])))
		print d2

	if (b1.hasEnded()):
		print "Player 2 Wins!"
		break
	if b2.hasEnded():
		print "Player 1 Wins!"
		break
	turn +=1

s.close()

