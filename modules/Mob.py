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
import math
import random
import Entity

def create():
        mob = dict()
        mob["x"]=3
        mob["y"]=2
        mob["vx"]=0
        mob["vy"]=0
        mob["health"]=100
        mob["xp"]=0.0
        mob["strength"]=1
        mob["resistance"]=1
        mob["sprite"]="M"
        mob["type"] = ""
        mob["state"] = "normal"
        mob["damage"] = -1
        return mob

def live(m, p, rDetec, dt):
        # recuperation de la position du mob
        mX, mY = Entity.getPosition(m)
        mvX, mvY = Entity.getSpeed(m)
        
        keepSameDirection = random.randbool()
        if not keepSameDirection: 
                direction = [(0,1),(0,-1),(-1,0),(1,0)]
                mvX, mvY = direction[random.randint(0,3)]
                        
                        
        if state(m, p, rDetec) == "normal":    
                Entity.setSpeed(mvX/2, mvY/2)
                
                
        elif state(m, p, rDetec) == "angry":
                Entity.setSpeed(2*mvX, 2*mvY)
                        
        elif state(m, p, rDetec) == "freeze":
                Entity.setSpeed(0, 0)

        return Entity.simulate(m, dt)

def state(m, p, rDetec):
        # recuperation de la position du mob
        mX, mY = Entity.getPosition(m)
        
        # recuperation de la position du joueur 
        pX, pY = Entity.getPosition(p)
        
        # Position du joueur par rapport au mob:
        playerPosition = math.sqrt((pX-mX)**2 + (pY-mY)**2)
        
        if playerPosition <= rDetec :
                m["state"] = "angry"
        else : 
                state = ["normal", "freeze"]
                m["state"] = state[random.randint(0,1)]
       
        return m["state"]


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
