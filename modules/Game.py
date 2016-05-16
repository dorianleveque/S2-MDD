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
import sys

# Modules personnalisés
import Dungeon
import Room
import Player
import Utils

def create():
        game = dict()
        game["player"] = Player.create()
        game["dungeon"] = Dungeon.create("forest")
        
        Dungeon.generate(game["dungeon"])
        Player.setPosition(game["player"], 1, 1)
        
        return game

def show(g):        
        # Affichage de l'interface
        
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

        if(Room.get(currentRoom, x, y - 1) == " ")

        Player.setPosition(g["player"], x, y)
        switchRoom(g)
        
        #elif key == "p":                      # appel de la fonction pause
#                return "pause"

def switchRoom(g):
        x, y = Player.getPosition(g["player"])
        currentRoom = Dungeon.getCurrentRoom(g["dungeon"])

        if x < 0:
                Dungeon.setCurrentRoom(g["dungeon"], Room.getLeftRoom(currentRoom))
                x = 79
        
        if x > 79: # Taille max en x des salles
                Dungeon.setCurrentRoom(g["dungeon"], Room.getRightRoom(currentRoom))
                x = 0

        if y < 0:
                Dungeon.setCurrentRoom(g["dungeon"], Room.getUpRoom(currentRoom))
                y = 37

        if y > 37: # Taille max en y des salles
                Dungeon.setCurrentRoom(g["dungeon"], Room.getDownRoom(currentRoom))
                y = 0

        Player.setPosition(g["player"], x, y)



