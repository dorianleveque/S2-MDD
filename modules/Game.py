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
	Dungeon.generate(g["dungeon"], Dungeon.getPlayer(g["dungeon"]))
        
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
        
        # Strength
        strength = Entity.getStrength(player)
        Utils.goto(offsetX+1, offsetY+6)
        Utils.write("Strength : + " + str((strength-1)*100) + "%")
        
        # Resistance
        resistance = Entity.getResistance(player)
        Utils.goto(offsetX+1, offsetY+8)
        Utils.write("Resistance : + " + str((resistance-1)*100) + "%")
        
        # Damage
        damage = Entity.getDamage(player)
        Utils.goto(offsetX+1, offsetY+10)
        Utils.write("Damage : " + str(damage))
        
def interact(g, settings, keyRead):
        # Actualiser les nouvelles touches du fichier settings:   
        keyM = g["keyManager"]
        for keyName in keyM:
                for k in settings:
                        if keyName == k:
                                keyM[keyName]["key"] = settings[k]


       #for keyName in keyM:
               #if keyM[keyName]["key"] == keyRead:
                       #if keyM[keyName]["status"] == False:
                               #keyM[keyName]["status"] = True
                       #else: keyM[keyName]["status"] = False 
               #else: keyM[keyName]["status"] = False
        Utils.goto(5, 44)
        print(g["keyManager"])
        
        
        if keyM["Up"]["key"] == keyRead:
                keyM["Up"]["status"] = True
        elif keyM["Down"]["key"] == keyRead:
                keyM["Up"]["status"] = False
        
        
        
        
        player = Dungeon.getPlayer(g["dungeon"])
        playerSpeedValue = 15

        if keyM["Up"]["status"]:
                Entity.setSpeed(player, 0, -playerSpeedValue)
                
        elif keyM["Down"]["status"]:
                Entity.setSpeed(player, 0, playerSpeedValue)
                
        elif keyM["Left"]["status"]:
                Entity.setSpeed(player, -playerSpeedValue*2, 0)
                
        elif keyM["Right"]["status"]:
                Entity.setSpeed(player, playerSpeedValue*2, 0)
                
        elif keyM["Shoot"]["status"]:
                Dungeon.launchArrow(g["dungeon"], player)
        
if __name__ == "__main__":
        game = create()
        print game
