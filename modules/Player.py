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
        player["x"] = 1
        player["y"] = 1
        player["health"] = 100
        player["xp"] = 0
        player["strength"] = 1
        player["resistance"] = 1
        player["inventory"] = Chest.create()
        player["sprite"] = 'P'
       
        return player

def getPosition(player):
        x = player["x"]
        y = player["y"]
        
        return (x,y)
        

def setPosition(player,x,y):
        player["x"] = x
        player["y"] = y


def move(player, direction):
        if direction == "up":
                player["y"] += -1
        if direction == "down":
                player["y"] += 1
        if direction == "right":
                player["x"] += 1
        if direction == "left":
                player["x"] += -1

def show(p):
        Utils.goto(p["x"]+2, p["y"]+2)
        Utils.write(p["sprite"]+'\n')        

def getHealth(p):
        return p["health"]

def setHealth(p, health):
        p["health"] = health
        return

def getXp(p):
        return p["xp"]

def setXp(p, xp):
        p["xp"] = xp
        return

def getStrength(p):
        return p["strength"]

def setStrength(p, strength):
        p["strength"] = strength
        return

def getResistance(p):
        return p["resistance"]

def setResistence(p, resistance):
        p["resistance"] = resistance
        return

def getDamage(p):
        return Bow.getDamage(getSelectedBow(p))

#def setDamage(p, damage):
        bow = getSelectedBow(p)
        Bow.setDamage(bow)

def getSelectedBow(p):
        return Chest.getContent(p["inventory"])[p["selectedBow"]]

def getInventory(p):
       return p["inventory"]

def getSprite(p):
       return p["sprite"]

def setSprite(p, sprite):
       p["sprite"] = sprite
       return

if __name__ == "__main__":
       p = create()
       show(p)
       move(p, "right")
       move(p, "right")
       show(p)
