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
import random

# Modules personnalisés
import Room


def create(name):
        d = dict()
        d["name"] = name
        d["currentRoom"] = None

        return d

def generate(d):
        # On récupère la liste des salles possibles pour ce donjon
        roomFiles = os.listdir("./../assets/rooms/" + d["name"] + "/")
        rooms = []
        for i in range(len(roomFiles)):
                room = Room.create(d["name"], d["name"] + "_" + str(i))
                rooms.append(room)
        
        d["currentRoom"] = rooms[Math.random]

def show(d):
        Room.show(d["currentRoom"])