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
        x, y = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        placedRooms = []

        # On récupère la liste des salles possibles pour ce donjon
        roomFiles = os.listdir("./assets/rooms/" + d["name"] + "/")
        roomsTotalNumber = len(roomFiles)
        remainingRooms = []
        for i in range(roomsTotalNumber):
                room = Room.create(d["name"], d["name"] + "_" + str(i+1))
                remainingRooms.append(room)
        
        # On choisit aléatoirement la première salle
        placedRooms.append((pickUpRandomRoom(remainingRooms), 0, 0))

        # Tant qu'il reste des salles
        while not(len(remainingRooms) == 0):
                # On en prend une au hasard
                currentRoom = pickUpRandomRoom(remainingRooms)

                # On se déplace sur la "grille" fictive (+x vers la droite, +y vers le haut)
                dx, dy = directions[random.randint(0, 3)]
                x, y = x + dx, y + dy

                # S'il y a déja une salle, alors on continue
                while not(getRoomByPosition(placedRooms, x, y) == -1):
                        x, y = x + dx, y + dy

                placedRooms.append((currentRoom, x, y))

        # Définit la première room
        d["currentRoom"] = placedRooms[0][0]

        # On place les portes correctement
        for currentPlacedRoom in placedRooms:
                currentRoom, x, y = currentPlacedRoom
                
                for direction in range(0, 4):
                        dx, dy = directions[direction]
                        adjx, adjy = x + dx, y + dy

                        addRoom = getRoomByPosition(placedRooms, adjx, adjy)

                        if not(addRoom == -1):
                                if direction == 0:
                                        if(Room.getUpRoom(currentRoom) == None):
                                                Room.setUpRoom(currentRoom, addRoom)
                                                Room.setDownRoom(addRoom, currentRoom)
                                elif direction == 1:
                                        if(Room.getRightRoom(currentRoom) == None):
                                                Room.setRightRoom(currentRoom, addRoom)
                                                Room.setLeftRoom(addRoom, currentRoom)
                                elif direction == 2:
                                        if(Room.getDownRoom(currentRoom) == None):
                                                Room.setDownRoom(currentRoom, addRoom)
                                                Room.setUpRoom(addRoom, currentRoom)
                                elif direction == 3:
                                        if(Room.getLeftRoom(currentRoom) == None):
                                                Room.setLeftRoom(currentRoom, addRoom)
                                                Room.setRightRoom(addRoom, currentRoom)

                Room.drawDoors(currentRoom)

def getRoomByPosition(placedRooms, x, y):
        for currentPlacedRoom in placedRooms:
                if (x == currentPlacedRoom[1]) and (y == currentPlacedRoom[2]):
                        return currentPlacedRoom[0]
        
        return -1


# Renvoie une salle prise aléatoirement dans la liste des salles restantes et l'enleve de la liste
def pickUpRandomRoom(remainingRooms):
        index = random.randint(0, len(remainingRooms) - 1)
        room = remainingRooms[index]
        del remainingRooms[index]
        return room

def show(d):
        Room.show(d["currentRoom"])

def interact():
        Room.interact()

def collide():
        Room.collide()

def move():
        Room.liveMob(d["currentRoom"])

def switchRoom(d):
        x, y = Room.getEntityPosition(d["currentRoom"])
        currentRoom = getCurrentRoom(d)

        if x < 2:
                Dungeon.setCurrentRoom(d, Room.getLeftRoom(currentRoom))
                x = 78
        
        if x > 78: # Taille max en x des salles
                Dungeon.setCurrentRoom(d, Room.getRightRoom(currentRoom))
                x = 2

        if y < 2:
                Dungeon.setCurrentRoom(d, Room.getUpRoom(currentRoom))
                y = 38

        if y > 38: # Taille max en y des salles
                Dungeon.setCurrentRoom(d, Room.getDownRoom(currentRoom))
                y = 2


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
