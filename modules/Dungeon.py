# -*- coding: utf-8 -*-
##################################################################
##                                                                ##
##             The Legend Of Zelda - A Link to the Rogue                ##
##            Un projet de Methode de Developpement (MDD)         ##
##                                                                ##
##                             Dungeon.py                                ##
##                                                                ##
## LEVEQUE Dorian & ROUE Evan         S2P         ENIB             01/04/2016 ##
##################################################################

# Modules système
import os
import math
import random

# Modules personnalisés
import Room
import Entity
import Player
import Utils

def create(name):
        d = dict()
        d["name"] = name
        d["currentRoom"] = None
        return d

def generate(d, player = None):
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
                while getRoomByPosition(placedRooms, x, y) != -1:
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

        # On place le joueur dans la 1ere salle
        if player != None:
                Room.addEntity(d["currentRoom"], player)
        else:
                Room.addEntity(d["currentRoom"], Player.create())

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

def switchRoom(d):
        oldRoom = d["currentRoom"]
        player = Room.getPlayer(oldRoom)
        x, y = Entity.getPosition(player)

        if x < 2 or x > 78 or y < 2 or y > 38:
                Room.removeEntity(oldRoom, player)

                if x < 2:
                        setCurrentRoom(d, Room.getLeftRoom(oldRoom))
                        x = 78
        
                if x > 78: # Taille max en x des salles
                        setCurrentRoom(d, Room.getRightRoom(oldRoom))
                        x = 2

                if y < 2:
                        setCurrentRoom(d, Room.getUpRoom(oldRoom))
                        y = 38

                if y > 38: # Taille max en y des salles
                        setCurrentRoom(d, Room.getDownRoom(oldRoom))
                        y = 2

                Entity.setPosition(player, x, y)
                Room.addEntity(d["currentRoom"], player)

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

def run(d, dt):
        switchRoom(d)
        return Room.run(d["currentRoom"], dt)        

def show(d):
        Room.show(d["currentRoom"])

def getEntityPosition(d, entity):
        return Room.getEntityPosition(getCurrentRoom(d), entity)

def setEntityPosition(d, entity, x, y):
        return Room.setEntityPosition(getCurrentRoom(d), entity, x, y)

def getPlayer(d):
        return Room.getPlayer(d["currentRoom"])
        
def launchArrow(d, player):
        return Room.launchArrow(d["currentRoom"], player)
        
def openChest(d):
        return Room.openChest(d["currentRoom"])

def isFree(d, x, y):
        return Room.isFree(d, x, y)
