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
import Entity
import Chest
import Utils

def create():
        #creation d'un joueur:
        player=dict()
        player["entity"] = Entity.create(2, 2, 100, 0, 1, 1, "P")
        player["inventory"] = Chest.create()
       
        return player

def getPosition(player):
        return Entity.getPosition(player["entity"])

def setPosition(player,x,y):
        Entity.setPosition(player["entity"], x, y)
        return

def move(player, direction):
        Entity.move(p["entity"], direction)

def show(p):
	x, y = Entity.getPosition(p["entity"])
        Utils.goto(x+2, y+2)
        Utils.write(Entity.getSprite(p["entity"])+'\n')

def getHealth(p):
        return Entity.getHealth(p)

def setHealth(p, health):
        Entity.setHealth(p["entity"], health)
        return

def getXp(p):
        return Entity.getXp(p)

def setXp(p, xp):
        Entity.setXp(p["entity"], xp)
        return

def getStrength(p):
        return Entity.getStrength(p)

def setStrength(p, strength):
        Entity.setStrength(p["entity"], strength)
        return

def getResistance(p):
        return Entity.getResistance(p)

def setResistance(p, resistance):
        Entity.setResistance(p["entity"], resistance)
        return

def getDamage(p):
        return Bow.getDamage(getSelectedBow(p))

def getSelectedBow(p):
        return Chest.getContent(p["inventory"])[p["selectedBow"]]

def getInventory(p):
       return p["inventory"]

def getSprite(p):
        return Entity.getSprite(p)

def setSprite(p, sprite):
       Entity.setSprite(p["entity"], sprite)
       return

if __name__ == "__main__":
       p = create()
       show(p)
       move(p, "right")
       move(p, "right")
       show(p)
