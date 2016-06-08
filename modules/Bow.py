# -*- coding: utf-8 -*-
##################################################################
##                                                                ##
##             The Legend Of Zelda - A Link to the Rogue                ##
##            Un projet de Methode de Developpement (MDD)         ##
##                                                                ##
##                              Bow.py                                ##
##                                                                ##
## LEVEQUE Dorian & ROUE Evan         S2P         ENIB             01/04/2016 ##
##################################################################

def create():
        bow = dict()
        bow["name"] = ""
        bow["damage"] = 0
        bow["sprite"] = ''
        return bow

def getName(b):
        return b["name"]

def setName(b, name):
        b["name"] = name
        return

def getDamage(b):
        return b["damage"]

def setDamage(b, damage):
        b["damage"] = damage
        return

def getSprite(b):
        return b["sprite"]

def setSprite(b, sprite):
        b["sprite"] = sprite
        return

if __name__ == "__main__":
        test = True
        print "TESTING Bow.py :",

        # Test
        bow = create()

        setName(bow, "Arc de Link")
        if not getName(bow) == "Arc de Link":
                test = False

        setDamage(bow, 100)
        if not getDamage(bow) == 100:
                test = False

        setSprite(bow, "|)")
        if not getSprite(bow) == "|)":
                test = False

        if test == True:
                print "OK"
        else:
                print "FAILED"
                raise RuntimeError("Test failed in Bow.py")
