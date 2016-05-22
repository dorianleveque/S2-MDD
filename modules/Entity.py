# -*- coding: utf-8 -*-
##################################################################
##                                                              ##
##           The Legend Of Zelda - A Link to the Rogue          ##
##          Un projet de Methode de Developpement (MDD)         ##
##                                                              ##
##                           Entity.py                          ##
##                                                              ##
## LEVEQUE Dorian & ROUE Evan   S2P     ENIB         09/04/2016 ##
##################################################################

# Modules systèmes

# Modules personnalisés
import Utils

def create():
        #creation d'un joueur:
        entity=dict()
        entity["x"] = 
        entity["y"] = 
        entity["health"] = 100
        entity["xp"] = 0
        entity["strength"] = 1
        entity["resistance"] = 1
        entity["inventory"] = Chest.create()
        entity["sprite"] = 'P'
        
        return entity

def getPosition(entity):
        x = entity["x"]
        y = entity["y"]
        
        return (x,y)

def setPosition(entity,x,y):
        entity["x"] = x
        entity["y"] = y

def move(entity, direction):
        if direction == "up":
                entity["y"] += -1
        if direction == "down":
                entity["y"] += 1
        if direction == "right":
                entity["x"] += 1
        if direction == "left":
                entity["x"] += -1

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

def setResistance(p, resistance):
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
       e = create()
       show(p)
       move(e, "right")
       move(e, "right")
       show(e)
