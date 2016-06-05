# -*- coding: utf-8 -*-
##################################################################
##								##
##	     The Legend Of Zelda - A Link to the Rogue		##
##	    Un projet de Methode de Developpement (MDD) 	##
##								##
##			      Game.py				##
##								##
## LEVEQUE Dorian & ROUE Evan 	S2P 	ENIB	     01/04/2016 ##
##################################################################

# Modules systeme

# Modules personnalisés
import Dungeon
import Settings
import Entity

def create():
        game = dict()
        game["dungeon"] = Dungeon.create("forest")
        
        settings = Settings.create()
        game["keyManager"] = dict()
        for keyName in settings:
                dataKey = dict()
                dataKey.update({"key": settings[keyName], "status": False})
                game["keyManager"].update({keyName: dataKey})
                
        Dungeon.generate(game["dungeon"])
        return game

def restart(g):
        Dungeon.generate(g["dungeon"])

def run(g):
        player = Dungeon.getPlayer(g["dungeon"])
        if keyM["Up"]["status"] == True:
                Entity.setSpeed

        Dungeon.run(g["dungeon"])
        
        Dungeon.show(g["dungeon"])

def interact(g, keyRead):
        keyM = g["keyManager"]
        for keyName in keyM:
                if keyM[keyName]["key"] == keyRead:
                        if keyM[keyName]["status"] == False: keyM[keyName]["status"] = True
                        else: keyM[keyName]["status"] = False 
                else: keyM[keyName]["status"] = False

def collide(g):
        Dungeon.switchRoom(g["dungeon"])
        
        # recuperation de la position du joueur
        x, y = Dungeon.getPlayer(g["dungeon"], "player")
        currentRoom = Dungeon.getCurrentRoom(g["dungeon"])
        keyM = g["keyManager"]
        
        if keyM["Up"]["status"] == True and Dungeon.isFree(currentRoom, x, y-1):
                #movePlayer(direction)
                Dungeon.getP(g["dungeon"], "player", x, y-1)
        if keyM["Left"]["status"] == True and Dungeon.isFree(currentRoom, x-1, y):
                Dungeon.setEntityPosition(g["dungeon"], "player", x-1, y)
        if keyM["Down"]["status"] == True and Dungeon.isFree(currentRoom, x, y+1):
                Dungeon.setEntityPosition(g["dungeon"]), "player", x, y+1)
        if keyM["Right"]["status"] == True and Dungeon.isFree(currentRoom, x+1, y):
                Dungeon.setEntityPosition(g["dungeon"], "player", x+1, y)
                
        
        #x, y = Entity.getPosition(r["player"])
        #currentRoom = Dungeon.getCurrentRoom(g["dungeon"])

        #if (key == "z") and (Room.get(currentRoom, x, y-1) == " "): 
                #y = y - 1             # le joueur se déplace vers Direction Haut
        #elif (key == "q") and (Room.get(currentRoom, x-1, y) == " "): 
                #x = x - 1             # le joueur se déplace vers Direction Gauche
        #elif (key == "s") and (Room.get(currentRoom, x, y+1) == " "): 
                #y = y + 1             # le joueur se déplace vers Direction Bas
        #elif (key == "d") and (Room.get(currentRoom, x+1, y) == " "): 
                #x = x + 1             # le joueur se déplace vers Direction Droite

        #if(Room.get(currentRoom, x, y - 1) == " "):

        #Player.setPosition(g["player"], x, y)

        
        #elif key == "p":                      # appel de la fonction pause
#                return "pause"
        

def move(g):
        # Permet de deplacer les entitees
        #Dungeon.liveMobs()
        Dungeon.move(g["dungeon"])
        
def getDungeon(g):
        return g["dungeon"]
        
if __name__ == "__main__":
        game = create()
        print game