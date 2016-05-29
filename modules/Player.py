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

# Modules systèmes

# Modules personnalisés
import Chest
import Utils

def create():
        #creation d'un joueur:
        player=dict()
        player["x"]=3
        player["y"]=2
        player["health"]=100
        player["xp"]=0.0
        player["strength"]=1
        player["resistance"]=1
        player["damage"] = 0
        player["sprite"]="P"
        player["inventory"] = Chest.create()
        return player

#def getPosition(player):
        #x = player["x"]
        #y = player["y"]
        #return (x,y)

#def setPosition(player,x,y):
        #player["x"] = x
        #player["y"] = y

#def show(player):
	#x, y = getPosition(player)
        #Utils.goto(x+2, y+2)
        #Utils.write(player["sprite"]+'\n')

#def getHealth(player):
        #return player["health"]

#def setHealth(player, health):
        #player["health"] = health

#def getXp(player):
        #return player["xp"]

#def setXp(player, xp):
        #player["xp"] = xp

#def getStrength(player):
        #return player["strength"]

#def setStrength(player, strength):
        #player["strength"] = strength

#def getResistance(player):
        #return player["resistance"]

#def setResistance(player, resistance):
        #player["resistance"] = resistance

#def getDamage(player):
        #return player["damage"]

#def getSelectedBow(player):
        #return Chest.getContent(player["inventory"])[player["selectedBow"]]

#def getInventory(player):
       #return player["inventory"]

#def getSprite(player):
        #return player["sprite"]

#def setSprite(player, sprite):
        #player["sprite"] = sprite

if __name__ == "__main__":
       p = create()
       show(p)
       move(p, "right")
       move(p, "right")
       show(p)
