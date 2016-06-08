# -*- coding: utf-8 -*-
##################################################################
##                                                                ##
##             The Legend Of Zelda - A Link to the Rogue                ##
##            Un projet de Methode de Developpement (MDD)         ##
##                                                                ##
##                            Settings.py                                ##
##                                                                ##
## LEVEQUE Dorian & ROUE Evan         S2P         ENIB             31/05/2016 ##
##################################################################

def create():
        keyGame=dict()
        keyGame["Up"] = 'z'
        keyGame["Down"] = 's'
        keyGame["Left"] = 'q'
        keyGame["Right"] = 'd'
        keyGame["Shoot"] = 'e'
        keyGame["Chest"] = 'a'
        return keyGame

def getKey(keyGame,keyName):
        for k in keyGame:
                if k == keyName:
                        return keyGame[k]

def setKey(keyGame,keyName,key):
        keyGame[keyName] = key
        return
        
# Test
if __name__ == "__main__":
        gameSettings = create()
        print gameSettings

        print getKey(gameSettings,'Up')
        
        setKey(gameSettings, 'Up', 'a')
        
        print getKey(gameSettings, 'Up')
