#player.py - coded by Shreya; meant to be the interface for a player 
 
 import abc 

 class Player(object): 
 	__metaclass__ = abc.ABCMeta 

 	@abc.abstractmethod 
 	def move(self):
 		return (x, y) 

 	@abc.abstractmethod
 	def getBoard(self):
 		return 

 	@abc.abstractmethod 
 	def recieveBoard(self): 
 		return 
