# -*- coding: utf-8 -*-
##################################################################
##								##
##	     The Legend Of Zelda - A Link to the Rogue		##
##	    Un projet de Methode de Developpement (MDD) 	##
##								##
##			     Dungeon.py	        		##
##								##
## LEVEQUE Dorian & ROUE Evan 	S2P 	ENIB	     01/04/2016 ##
##################################################################

# Modules système
import os
import math
import random

# Modules personnalisés
import Room
import Utils

def create(name):
        d = dict()
        d["name"] = name
        d["currentRoom"] = None

        return d

def generate(d):
        # On récupère la liste des salles possibles pour ce donjon
        roomFiles = os.listdir("./assets/rooms/" + d["name"] + "/")
        roomsTotalNumber = len(roomFiles)
        remainingRooms = []
        for i in range(roomsTotalNumber):
                room = Room.create(d["name"], d["name"] + "_" + str(i+1))
                remainingRooms.append(room)
        
        # On choisit aléatoirement la première salle
        d["currentRoom"] = pickUpRandomRoom(remainingRooms)
        
        # Appel de la fonction récursive pour déterminer les salles adjacentes
        recursiveGeneration(d, remainingRooms, d["currentRoom"], 1, roomsTotalNumber)

# Cette fonction génère les salles adjacentes à une case donnée. Elle est, par construction, récursive.
# Elle etudie pour chaque direction, s'il faut mettre (ou non), une salle aléatoire prise dans la liste des salles restantes.
# Si oui, alors la fonction se rappelle-elle même pour définir les salles adjacentes de la salle venant d'être placé.
def recursiveGeneration(d, remainingRooms, currentRoom, roomLevel, roomsTotalNumber):
        # Réglage des coefficients
        depthCoefficient = 0.1
        remainingRoomCoefficient = 1
        
        if(len(remainingRooms) == 0):
                return
        
        for door in ["up", "down", "left", "right"]:
                # Calcule la probabilité
                #depthDrivenCoefficient = math.exp(-(roomLevel * depthCoefficient))
                #remainingRoomDrivenCoefficient = remainingRoomCoefficient*(len(remainingRooms) / roomsTotalNumber)
                #probability = int(round(depthDrivenCoefficient*remainingRoomDrivenCoefficient*random.random()+0.5, 0))
                probability = int(round(random.random(), 0))
                
                if(roomLevel >= 7):     # Sécurité afin d'éviter d'avoir des donjons trop profonds
                        p = 0

                if((probability >= 1) and (len(remainingRooms) != 0)):
                        addRoom = pickUpRandomRoom(remainingRooms)

                        if door == "up":
                                if(Room.getUpRoom(currentRoom) == None):
                                        Room.setUpRoom(currentRoom, addRoom)
                                        Room.setDownRoom(addRoom, currentRoom)
                        elif door == "down":
                                if(Room.getDownRoom(currentRoom) == None):
                                        Room.setDownRoom(currentRoom, addRoom)
                                        Room.setUpRoom(addRoom, currentRoom)
                        elif door == "left":
                                if(Room.getLeftRoom(currentRoom) == None):
                                        Room.setLeftRoom(currentRoom, addRoom)
                                        Room.setRightRoom(addRoom, currentRoom)
                        elif door == "right":
                                if(Room.getRightRoom(currentRoom) == None):
                                        Room.setRightRoom(currentRoom, addRoom)
                                        Room.setLeftRoom(addRoom, currentRoom)

                        recursiveGeneration(d, remainingRooms, addRoom, roomLevel + 1, roomsTotalNumber)

# Renvoie une salle prise aléatoirement dans la liste des salles restantes et l'enleve de la liste
def pickUpRandomRoom(remainingRooms):
        index = random.randint(0, len(remainingRooms) - 1)
        room = remainingRooms[index]
        del remainingRooms[index]
        return room

def show(d):
        Room.show(d["currentRoom"])
        #Utils.goto(100, 42)
        #Utils.write(str(d["currentRoom"])+'\n')

def getCurrentRoom(d):
        return d["currentRoom"]

def setCurrentRoom(d, currentRoom):
        d["currentRoom"] = currentRoom
        return

def getName(d):
        return d["name"]

def setName(d, name):
        d["name"] = name
        return
