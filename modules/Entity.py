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

#def create(entity, x, y, health, xp, strength, resistance, sprite):
        ## creation d'une entité :
        #entity["x"] = x
        #entity["y"] = y
        #entity["health"] = health
        #entity["xp"] = xp
        #entity["strength"] = strength
        #entity["resistance"] = resistance
        #entity["sprite"] = sprite
        
        #return entity

def getPosition(e):
        x = e["x"]
        y = e["y"]
        return (x,y)

def setPosition(e,x,y):
        e["x"] = x
        e["y"] = y

def getSpeed(e):
        vx = e["vx"]
        vy = e["vy"]
        return (vx,vy)

def setSpeed(e,vx,vy):
        e["vx"] = vx
        e["vy"] = vy


def simulate(e, dt):
        x,y = getPosition(e)
        vx,vy = getSpeed(e)
        
        x = x + vx * dt
        y = y + vy * dt
        return (x, y)
        
        
        #if direction == "up":
                #entity["y"] += -1
        #if direction == "down":
                #entity["y"] += 1
        #if direction == "right":
                #entity["x"] += 1
        #if direction == "left":
                #entity["x"] += -1

#def collide():
        #x, y = Player.getPosition(g["player"])
        #currentRoom = Dungeon.getCurrentRoom(g["dungeon"])

        #if (key == "z") and (Room.get(currentRoom, x, y-1) == " "): 
                #y = y - 1             # le joueur se déplace vers Direction Haut
        #elif (key == "q") and (Room.get(currentRoom, x-1, y) == " "): 
                #x = x - 1             # le joueur se déplace vers Direction Gauche
        #elif (key == "s") and (Room.get(currentRoom, x, y+1) == " "): 
                #y = y + 1             # le joueur se déplace vers Direction Bas
        #elif (key == "d") and (Room.get(currentRoom, x+1, y) == " "): 
                #x = x + 1             # le joueur se déplace vers Direction Droite

def show(e, color="white"):
        x,y = getPosition(e)
        x = int(round(x))
        y = int(round(y))
        sprite = getSprite(e)
        Utils.goto(x+2, y+2)
        Utils.write(sprite+'\n', color)
        
def getType(e):
        return e["type"]
        
def setType(e, type):
        e["type"] = type

def getHealth(e):
        return e["health"]

def setHealth(e, health):
        e["health"] = health

def getXp(e):
        return e["xp"]

def setXp(e, xp):
        e["xp"] = xp

def getStrength(e):
        return e["strength"]

def setStrength(e, strength):
        e["strength"] = strength

def getResistance(e):
        return e["resistance"]

def setResistance(e, resistance):
        e["resistance"] = resistance

def getSprite(e):
       return e["sprite"]

def setSprite(e, sprite):
       e["sprite"] = sprite

def getDamage(e):
        return e["damage"]

def setDamage(e, damage):
        e["damage"] = damage

if __name__ == "__main__":
       e = create(2, 2, 300, 0, 1, 1, "Test")
       show(e)
       move(e, "right")
       move(e, "right")
       show(e)

