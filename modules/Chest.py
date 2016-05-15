# -*- coding: utf-8 -*-
##################################################################
##								##
##	     The Legend Of Zelda - A Link to the Rogue		##
##	    Un projet de Methode de Developpement (MDD) 	##
##								##
##			      Chest.py				##
##								##
## LEVEQUE Dorian & ROUE Evan 	S2P 	ENIB	     01/04/2016 ##
##################################################################

# Modules personnalisés
import Bow
import Bonus

def create():
        chest = dict()
        chest["content"]=None
        chest["x"]=-1
        chest["y"]=-1
        return chest

def addItem(c, i):
        c["content"].append(i)
        return

def getPosition(c):
        return (c["x"], c["y"])

def setPosition(c, x, y):
        c["x"] = x
        c["y"] = y
        return

def getContent(c):
        return c["content"]
        
def isInside(c, Item):    #test du getContent
        return true

if __name__ == "__main__":
        chest = create()
        setPosition(chest, 5, 4)
