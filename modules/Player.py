# -*- coding: utf-8 -*-
##################################################################
##								##
##	     The Legend Of Zelda - A Link to the Rogue		##
##	    Un projet de Methode de Developpement (MDD) 	##
##								##
##			     Player.py	        		##
##								##
## LEVEQUE Dorian & ROUE Evan 	S2P 	ENIB	     09/04/2016 ##
##################################################################

# Modules personnalisés
import Chest
import Utils

def create():
        #creation d'un joueur:
        player=dict()
        player["x"] = 0
        player["y"] = 0  
       
        return player

def getPosition(player):
        x = player["x"]
        y = player["y"]
        
        return (x,y)
        

def setPosition(player,x,y):
        player["x"] = x
        player["y"] = y

#def getHealth(p):
#        return Health

#def setHealth(p, health):
        

#def getXp(p):
#        return Xp

#def setXp(p):
        

#def getStrength(p):
#        return strength

#def setStrength(p, strength):
        

#def getResistance(p):
#        return resistence

#def setResistence(p, resistence):
        

#def getDamage(p):
 #       return damage

#def setDamage(p, damage):
        

#def getSelectedBow(p):
#        return

#def getInventory(p):
 #       return