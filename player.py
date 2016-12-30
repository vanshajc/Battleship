#player.py - coded by Shreya; meant to be the interface for a player 
 
 import abc 

 class Player(object): 
 	__metaclass__ = abc.ABCMeta 

 	@abc.abstractmethod 
 	def hit(self): 
 		return (x, y)
 		
 	@abc.abstractmethod 
 	def miss(self): 
 		return (x, y)

 	@abc.abstractmethod
 	def getBoard(self):
 		return 
