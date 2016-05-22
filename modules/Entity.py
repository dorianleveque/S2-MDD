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

def create(x, y, health, xp, strength, resistance, sprite):
        # creation d'une entité :
        entity=dict()
        entity["x"] = x
        entity["y"] = y
        entity["health"] = health
        entity["xp"] = xp
        entity["strength"] = strength
        entity["resistance"] = resistance
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

def show(e):
        Utils.goto(e["x"]+2, e["y"]+2)
        Utils.write(e["sprite"]+'\n')

def getHealth(e):
        return e["health"]

def setHealth(e, health):
        e["health"] = health
        return

def getXp(e):
        return e["xp"]

def setXp(e, xp):
        e["xp"] = xp
        return

def getStrength(e):
        return e["strength"]

def setStrength(e, strength):
        e["strength"] = strength
        return

def getResistance(e):
        return e["resistance"]

def setResistance(e, resistance):
        e["resistance"] = resistance
        return

def getSprite(e):
       return e["sprite"]

def setSprite(e, sprite):
       e["sprite"] = sprite
       return

if __name__ == "__main__":
       e = create()
       show(e)
       move(e, "right")
       move(e, "right")
       show(e)
