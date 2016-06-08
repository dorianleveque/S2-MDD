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
import Utils

def create():
	return init()

def init():
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

def regen(g):
	Dungeon.generate(g["dungeon"], Dungeon.getPlayer(g["dungeon"]))

def restart(g):
        g = init()

def run(g, dt):
        if Dungeon.run(g["dungeon"], dt) == "win":
		return "win"

        player = Dungeon.getPlayer(g["dungeon"])
        if Entity.getHealth(player) <= 0:
                return "lose"
        
        return "run"

def show(g):
        Dungeon.show(g["dungeon"])
        
        # -- Interface du joueur --
        player = Dungeon.getPlayer(g["dungeon"])
        offsetX = 84
        offsetY = 2
        
        # Clear
        for i in range(1, 41):
                Utils.goto(offsetX, i+1)
                Utils.write(29*" "+"\n")

        # Link
        Utils.goto(offsetX+1, offsetY+1)
        Utils.write("Link", "green")
        
        # Health
        health = Entity.getHealth(player)
        maxHealth = Entity.getMaxHealth(player)
        Utils.goto(offsetX+1, offsetY+3)
        Utils.write("Health : " + str(health) + " / " + str(maxHealth))
        Utils.goto(offsetX+1, offsetY+4)
        healthBar = int(round((health/maxHealth)*10))*"♥ "
        Utils.write(healthBar.decode("utf-8"), "red")
        
def interact(g, settings, keyRead):
        # chargement des nouvelles touches:   
        keyM = g["keyManager"]
        for keyName in keyM:
                for k in settings:
                        if keyName == k:
                                keyM[keyName]["key"] = settings[k]


#        for keyName in keyM:
#                if keyM[keyName]["key"] == keyRead:
#                        if keyM[keyName]["status"] == False:
#                                keyM[keyName]["status"] = True
#                        else: keyM[keyName]["status"] = False 
#                else: keyM[keyName]["status"] = False"""
        
        player = Dungeon.getPlayer(g["dungeon"])
        playerSpeedValue = 15

        if keyM["Up"]["key"] == keyRead:
                Entity.setSpeed(player, 0, -playerSpeedValue)
        elif keyM["Down"]["key"] == keyRead:
                Entity.setSpeed(player, 0, playerSpeedValue)
        elif keyM["Left"]["key"] == keyRead:
                Entity.setSpeed(player, -playerSpeedValue*2, 0)
        elif keyM["Right"]["key"] == keyRead:
                Entity.setSpeed(player, playerSpeedValue*2, 0)
        elif keyM["Action"]["key"] == keyRead:
                Dungeon.launchArrow(g["dungeon"], player)

        
if __name__ == "__main__":
        game = create()
        print game
