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
import random
# Modules personnalisés
import Utils

def create():
        mob = dict()
        mob["x"]=3
        mob["y"]=2
        mob["health"]=100
        mob["xp"]=0.0
        mob["strength"]=1
        mob["resistance"]=1
        mob["sprite"]="M"
        mob["type"] = ""
        mob["state"] = "normal"
        mob["dir"] = (0, 0)
        mob["damage"] = -1
        return mob

#def setDirection(m):
        #direction = [(0,-1),(0,1),(-1,0)(1,0)]
        #m["dir"] = direction[random.randint(0,3)]

#def getDirection(m):
        #return mob["dir"]

#def setState(m):
        #state = ["normal", "angry", "freeze"]
        #currentState = getState
        
        

#def getState(m):
        #return m["state"]

#def live(m):
        #x, y = Entity.getPosition(m["entity"])

        ##if mob["type"] == "zombie":
                ##if mob["state"] == "normal":    
                        
                        ##Entity.collide()
                        
                        
                ##elif mob["state"] == "angry":
                        
                        
                ##elif mob["state"] == "freeze":  

                        
                
        ##elif mob["type"] == "soldier":
                ##if mob["state"] == "normal":
                ##elif mob["state"] == "angry":
                ##elif mob["state"] == "freeze": 
                
        ##elif mob["type"] == "boss":
                ##if mob["state"] == "normal":
                ##elif mob["state"] == "angry":
                ##elif mob["state"] == "freeze": 
        
        
        ###if m["type"] == "zombie":
                ###m["dir"] = (-m["dir"](0), m["dir"](1))
        ###elif m["type"] == "soldier":
                ###m["dir"] = (-m["dir"](0), m["dir"](1))
        ###elif m["type"] == "boss":
                ###m["dir"] = (
                ###x = 
                ###y = m["dir"] = 

        #Entity.setPosition(m["entity"], x, y)

        #return

#def show(m):
        #Entity.show(m)
        #return

#def getType(m):
        #return m["type"]
        
#def setType(m, type):
        #m["type"] = type
        #return

#def getPosition(m):
        #return Entity.getPosition(m["entity"])
     
#def setPosition(m, x, y):
        #Entity.setPosition(m["entity"], x, y)
        #return

#def getHealth(m):
        #return Entity.getHealth(m["entity"]) 
        
#def setHealth(m, health):
        #Entity.setHealth(m["entity"], health)
        #return

#def getStrength(m):
        #return Entity.getStrength(m["entity"])
        
#def setStrength(m, strength):
        #Entity.setStrength(m["entity"], strength)
        #return

#def getResistance(m):              
        #return Entity.getResistance(m["entity"])

#def setResistance(m, resistance):
        #Entity.setResistance(m["entity"], resistance)
        #return

#def getDamage(m):
        #return m["damage"]
        
#def setDamage(m, damage):
        #m["damage"] = damage
        #return

#def getSprite(m):
        #return Entity.getSprite(m["entity"])
        
#def setSprite(m, sprite):
        #Entity.setSprite(m["entity"], sprite)
        #return
