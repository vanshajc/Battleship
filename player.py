#player.py - coded by Shreya; meant to be the interface for a player 
import abc 
import socket
class Player(object): 
	__metaclass__ = abc.ABCMeta 
	def __init__(self):
		print 'Initialized'
	
	def connect(self):
		HOST = '192.168.1.174'    # The remote host
		PORT = 5003              # The same port as used by the server
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print 'Connecting...'
		s.connect((HOST, PORT))
		data = s.recv(1024)
		s.close()

 	@abc.abstractmethod 
 	def move(self):
 		return (x, y) 

 	@abc.abstractmethod
 	def getBoard(self):
 		return 

 	@abc.abstractmethod 
 	def recieveBoard(self): 
 		return 
