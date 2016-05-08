# -*- coding: utf-8 -*-
##################################################################
##								##
##	     The Legend Of Zelda - A Link to the Rogue		##
##	    Un projet de Methode de Developpement (MDD) 	##
##								##
##			      Arrow.py				##
##								##
## LEVEQUE Dorian & ROUE Evan 	S2P 	ENIB	     01/04/2016 ##
##################################################################

def create():
        arrow = dict()
        arrow["x"] = -1
        arrow["y"] = -1
        arrow["vx"] = -1
        arrow["vy"] = -1
        arrow["damage"] = -1
        return

def getPosition(a):
        return (a["x"], a["y"])
        
def setPosition(a, x, y):
        a["x"] = x
        a["y"] = y
        return

def getSpeed(a):
        return (a["vx"], a["vy"])
        
def setSpeed(a, vx, vy):
        a["vx"] = vx
        a["vy"] = vy
        return

def getDamage(a):
        return a["damage"]
        
def setDamage(a, damage):
        a["damage"] = damage
        return