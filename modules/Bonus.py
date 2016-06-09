# -*- coding: utf-8 -*-
##################################################################
##                                                                ##
##             The Legend Of Zelda - A Link to the Rogue                ##
##            Un projet de Methode de Developpement (MDD)         ##
##                                                                ##
##                              Bonus.py                                ##
##                                                                ##
## LEVEQUE Dorian & ROUE Evan         S2P         ENIB             01/04/2016 ##
##################################################################

def create():
        bonus = dict()
        bonus["name"] = ""
        bonus["amount"] = -1
        return bonus

def getName(b):
        return b["name"]
        
def setName(b, name):
        b["name"] = name
        return

def getAmount(b):
        return b["amount"]
        
def setAmount(b, amount):
        b["amount"] = amount
        return
