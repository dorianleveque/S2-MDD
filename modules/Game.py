# -*- coding: utf-8 -*-
##################################################################
##                                                              ##
##           The Legend Of Zelda - A Link to the Rogue          ##
##          Un projet de Methode de Developpement (MDD)         ##
##                                                              ##
##                            Game.py                           ##
##                                                              ##
## LEVEQUE Dorian & ROUE Evan   S2P     ENIB         01/04/2016 ##
##################################################################

# Modules systeme

# Modules personnalisés
import Dungeon
import Settings
import Entity

def create():
        game = dict()
        game["dungeon"] = Dungeon.create("forest")
        
        settings = Settings.create()
        game["keyManager"] = dict()
        for keyName in settings:
                dataKey = dict()
                dataKey.update({"key": settings[keyName], "status": False})
                game["keyManager"].update({keyName: dataKey})
                
        Dungeon.generate(game["dungeon"])
        return game

def restart(g):
        Dungeon.generate(g["dungeon"])

def run(g, dt):
        Dungeon.run(g["dungeon"], dt)

def show(g):
        Dungeon.show(g["dungeon"])

def interact(g, keyRead):
        keyM = g["keyManager"]
#        for keyName in keyM:
#                if keyM[keyName]["key"] == keyRead:
#                        if keyM[keyName]["status"] == False:
#                                keyM[keyName]["status"] = True
#                        else: keyM[keyName]["status"] = False 
#                else: keyM[keyName]["status"] = False"""
        
        player = Dungeon.getPlayer(g["dungeon"])
        playerSpeedValue = 20

        if keyM["Up"]["key"] == keyRead:
                Entity.setSpeed(player, 0, -playerSpeedValue)
        elif keyM["Down"]["key"] == keyRead:
                Entity.setSpeed(player, 0, playerSpeedValue)
        elif keyM["Left"]["key"] == keyRead:
                Entity.setSpeed(player, -playerSpeedValue*2, 0)
        elif keyM["Right"]["key"] == keyRead:
                Entity.setSpeed(player, playerSpeedValue*2, 0)

def getDungeon(g):
        return g["dungeon"]
        
if __name__ == "__main__":
        game = create()
        print game
