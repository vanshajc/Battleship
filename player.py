#player.py - coded by Shreya; meant to be the interface for a player 
 
 import abc 

 class Player(object): 
 	__metaclass__ = abc.ABCMeta 

 	@abc.abstractmethod 
 	def hit((x, y)): 
 		return 
 		
 	@abc.abstractmethod 
 	def miss((x, y)): 
 		return 
