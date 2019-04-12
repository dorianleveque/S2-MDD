# -*- coding: utf-8 -*-
##################################################################
##                                                              ##
##           The Legend Of Zelda - A Link to the Rogue          ##
##          Un projet de Methode de Developpement (MDD)         ##
##                                                              ##
##                           Chest.py                           ##
##                                                              ##
## LEVEQUE Dorian & ROUE Evan   S2P     ENIB         01/04/2016 ##
##################################################################

# Modules personnalisés
import Bow
import Bonus

def create():
        chest = dict()
        chest["items"]=[]
        chest["bonus"]=[]
        chest["x"]=-1
        chest["y"]=-1
        return chest

def addItem(c, i):
        c["items"].append(i)
        return
        
def addBonus(c, b):
        c["bonus"].append(b)
        return

def getPosition(c):
        return (c["x"], c["y"])

def setPosition(c, x, y):
        c["x"] = x
        c["y"] = y
        return

def getItems(c):
        return c["items"]

def getBonus(c):
        return c["bonus"]
        
def isInside(c, item):
        if item in c["items"]:
                return True
        else:
                return False

if __name__ == "__main__":
        test = True
        print "TESTING Chest.py :",

        # Test
        chest = create()
        setPosition(chest, 5, 4)

        if not getPosition(chest) == (5, 4):
                test = False

        bow = Bow.create()
        addItem(chest, bow)

        if not isInside(chest, bow):
                test = False

        if test == True:
                print "OK"
        else:
                print "FAILED"
                raise RuntimeError("Test failed in Chest.py !")
