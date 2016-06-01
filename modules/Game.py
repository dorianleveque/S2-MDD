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

def create():
        game = dict()
        game["dungeon"] = Dungeon.create("forest")
        game["keySetting"] = Settings.create()
        print game["keySetting"]
        Dungeon.generate(game["dungeon"])        
        return game

def restart(g):
        Dungeon.generate(g["dungeon"])

def show(g):        
        # Affichage du donjon
        Dungeon.show(g["dungeon"])

def interact(g, key):
        return

def collide():
        Dungeon.collide()
        
        
        
        x, y = Entity.getPosition(r["player"])
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
        switchRoom(g)
        
        #elif key == "p":                      # appel de la fonction pause
#                return "pause"

#def collide(g):
        ## Permet de gerer les colisions des entites 
        

def move(g):
        # Permet de deplacer les entite
        Dungeon.liveMobs()
        Dungeon.move()
        
        

def switchRoom(g):
        #x, y = Player.getPosition(g["player"])
        currentRoom = Dungeon.getCurrentRoom(g["dungeon"])

        if x < 2:
                Dungeon.setCurrentRoom(g["dungeon"], Room.getLeftRoom(currentRoom))
                x = 78
        
        if x > 78: # Taille max en x des salles
                Dungeon.setCurrentRoom(g["dungeon"], Room.getRightRoom(currentRoom))
                x = 2

        if y < 2:
                Dungeon.setCurrentRoom(g["dungeon"], Room.getUpRoom(currentRoom))
                y = 38

        if y > 38: # Taille max en y des salles
                Dungeon.setCurrentRoom(g["dungeon"], Room.getDownRoom(currentRoom))
                y = 2
                
if __name__ == "__main__":
        game = create()
        print game