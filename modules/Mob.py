# -*- coding: utf-8 -*-
##################################################################
##								##
##	     The Legend Of Zelda - A Link to the Rogue		##
##	    Un projet de Methode de Developpement (MDD) 	##
##								##
##			      Mob.py				##
##								##
## LEVEQUE Dorian & ROUE Evan 	S2P 	ENIB	     01/04/2016 ##
##################################################################

# Modules système

# Modules personnalisés
import Utils
import Entity

def create():
        mob = dict()
        mob["type"] = ""
        mob["state"] = "normal"
        mob["dir"] = (0, 0)
        mob["entity"] = Entity.create(-1, -1, -1, -1, -1, -1, "")
        mob["damage"] = -1
        return mob

def live(m, dt):
        x, y = Entity.getPosition(m["entity"])

        if m["type"] == "zombie":
                m["dir"] = (-m["dir"](0), m["dir"](1))
        elif m["type"] == "soldier":
                m["dir"] = (-m["dir"](0), m["dir"](1))
        elif m["type"] == "boss":
                m["dir"] = (
                x = 
                y = m["dir"] = 

        Entity.setPosition(m["entity"], x, y)

        return

def show(m):
        Entity.show(m)
        return

def getType(m):
        return m["type"]
        
def setType(m, type):
        m["type"] = type
        return

def getPosition(m):
        return Entity.getPosition(m["entity"])
     
def setPosition(m, x, y):
        Entity.setPosition(m["entity"], x, y)
        return

def getHealth(m):
        return Entity.getHealth(m["entity"]) 
        
def setHealth(m, health):
        Entity.setHealth(m["entity"], health)
        return

def getStrength(m):
        return Entity.getStrength(m["entity"])
        
def setStrength(m, strength):
        Entity.setStrength(m["entity"], strength)
        return

def getResistance(m):              
        return Entity.getResistance(m["entity"])

def setResistance(m, resistance):
        Entity.setResistance(m["entity"], resistance)
        return

def getDamage(m):
        return m["damage"]
        
def setDamage(m, damage):
        m["damage"] = damage
        return

def getSprite(m):
        return Entity.getSprite(m["entity"])
        
def setSprite(m, sprite):
        Entity.setSprite(m["entity"], sprite)
        return
