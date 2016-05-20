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
import Room
import Player

def create():
        game = dict()
        game["player"] = Player.create()
        game["dungeon"] = Dungeon.create("forest")
        
        Dungeon.generate(game["dungeon"])
        Player.setPosition(game["player"], 40, 20)
        
        return game

def show(g):        
        # Affichage du donjon
        Dungeon.show(g["dungeon"])
        
        # Affichage du joueur
        Player.show(g["player"])

def interact(g, key):
        x, y = Player.getPosition(g["player"])
        currentRoom = Dungeon.getCurrentRoom(g["dungeon"])

        if (key == "z") and (Room.get(currentRoom, x, y-1) == " "): 
                y = y - 1             # le joueur se déplace vers Direction Haut
        elif (key == "q") and (Room.get(currentRoom, x-1, y) == " "): 
                x = x - 1             # le joueur se déplace vers Direction Gauche
        elif (key == "s") and (Room.get(currentRoom, x, y+1) == " "): 
                y = y + 1             # le joueur se déplace vers Direction Bas
        elif (key == "d") and (Room.get(currentRoom, x+1, y) == " "): 
                x = x + 1             # le joueur se déplace vers Direction Droite

        #if(Room.get(currentRoom, x, y - 1) == " "):

        Player.setPosition(g["player"], x, y)
        switchRoom(g)
        
        #elif key == "p":                      # appel de la fonction pause
#                return "pause"

#def collider(g):
        ## Permet de gerer les colisions des entites 
        

#def move(g):
        # Permet de deplacer les entite


def switchRoom(g):
        x, y = Player.getPosition(g["player"])
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

        Player.setPosition(g["player"], x, y)



