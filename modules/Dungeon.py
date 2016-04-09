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

# Modules personnalisés
import Room

def create(name):
        d = dict()
        d["name"] = name
        d["currentRoom"] = None

        return d

def generate(d):
        # On récupère la liste des salles possibles pour ce donjon

        room

def show(d):
        Room.show(d["currentRoom"])