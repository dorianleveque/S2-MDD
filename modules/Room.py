# -*- coding: utf-8 -*-
##################################################################
##								##
##	     The Legend Of Zelda - A Link to the Rogue		##
##	    Un projet de Methode de Developpement (MDD) 	##
##								##
##			      Room.py				##
##								##
## LEVEQUE Dorian & ROUE Evan 	S2P 	ENIB	     01/04/2016 ##
##################################################################

# Modules système
from xml.dom.minidom import parse

# Modules personnalisés
import Chest
import Arrow
import Mob
import Utils

def create(dungeonName, roomName):
        # -- Initialisation du dictionnaire --
        r = dict()
        r["upRoom"]=None
        r["downRoom"]=None
        r["leftRoom"]=None
        r["rightRoom"]=None
        
        # -- Parsage du fichier XML correspondant --
        path = "./../assets/rooms/" + dungeonName + "/" + roomName + ".xml"
        doc = parse(path)
        rootBeacon = doc.documentElement

        # Récupération du background
        background = rootBeacon.getElementsByTagName("background")[0].firstChild.nodeValue
        for line in background:
                r["background"].append(list(line))

        # Récupération des mobs
        mobs = rootBeacon.getElementsByTagName("mobs")
        nb_mobs = mobs.length
        for i in range(nb_mobs):
                mob = Mob.create()
                Mob.setType(mob, mobs[i].getAttribute("type"))
                Mob.setPosition(mob, int(mobs[i].getAttribute("x")), int(mobs[i].getAttribute("y")))
                Mob.setHealth(mob, int(mobs[i].getAttribute("health")))
                Mob.setStrength(mob, float(mobs[i].getAttribute("strength")))
                Mob.setResistance(mob, float(mobs[i].getAttribute("resistance")))
                Mob.setDamage(mob, int(mobs[i].getAttribute("damage")))
                Mob.setSprite(mob, mobs[i].firstChild.nodeValue)
                r["mobs"].append(mob)
        
        # Récupération des coffres
        chests = rootBeacon.getElementsByTagName("chests")
        nb_chests = chests.length
        for i in range(nb_chests):
                chest = Chest.create()
                Chest.setPosition(chest, int(chests[i].getAttribute("x")), int(chests[i].getAttribute("y")))
                
                # Ajout des items
                items = chests[i].childNodes
                
                if item.nodeName == "bonus":
                        bonus = Bonus.create()
                        
                        chests.setContent(c, Chest.getContent(c).append(bonus))
                elif item.nodeName == "bow":
                        bow = Bow.create()
                        
                        chests.setContent(c, Chest.getContent(c).append(bonus))
                
                /*Mob.setType(mob, mobs[i].getAttribute("type"))
                Mob.setPosition(mob, int(mobs[i].getAttribute("x")), int(mobs[i].getAttribute("y")))
                Mob.setHealth(mob, int(mobs[i].getAttribute("health")))
                Mob.setStrength(mob, float(mobs[i].getAttribute("strength")))
                Mob.setResistance(mob, float(mobs[i].getAttribute("resistance")))
                Mob.setDamage(mob, int(mobs[i].getAttribute("damage")))
                Mob.setSprite(mob, mobs[i].firstChild.nodeValue)
                r["mobs"].append(mob)*/

        return r

def show(r):
        # Affichage du fond
        for y in range(0, len(r["background"])):
                for x in range(0, len(r["background"][y])):
                        goto(x, y)
                        sys.stdout.write(r["background"][y][x])
        
        # Affichage des coffres
        for currentChest in r["chests"]:
                x, y = Chest.getPosition(currentChest)
                goto(x, y)
                Chest.show(currentChest)
        
        # Affichage des mobs
        for currentMob in r["mobs"]:
                x, y = Mob.getPosition(currentMob)
                goto(x, y)
                Mob.show(currentMob)
        
        # Affichage des projectiles
        for currentArrow in r["arrows"]:
                x, y = Arrow.getPosition(currentArrow)
                goto(x, y)
                Arrow.show(currentArrow)

def getChestByPosition(r, x, y):
        # On parcourt la liste des coffres de la salle
        for currentChest in r["chests"]:
                if Chest.getPosition(currentChest) == (x,y):
                        return currentChest
        
        return None

def getMobByPosition(r, x, y):
        # On parcourt la liste des mobs de la salle
        for currentMob in r["mobs"]:
                if Mob.getPosition(currentMob) == (x,y):
                        return currentMob
        
        return None

def getUpRoom(r):
        return r["upRoom"]

def setUpRoom(r, up_room):
        r["upRoom"] = up_room

def getDownRoom(r):
        return r["downRoom"]

def setDownRoom(r, down_room):
        r["downRoom"] = down_room

def getLeftRoom(r):
        return r["leftRoom"]

def setLeftRoom(r, left_room):
        r["leftRoom"] = left_room

def getRightRoom(r):
        return r["rightRoom"]

def setRightRoom(r, right_room):
        r["rightRoom"] = right_room

# Tests
if __name__ == __main__:
        room = create("forest", "forest_1")
        goto(0, 0)
        room.show()

        