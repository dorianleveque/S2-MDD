# -*- coding: utf-8 -*-

from xml.dom.minidom import parse;

def create(dungeonName, roomName):
        
        path = "./../assets/rooms/" + dungeonName + "/" + roomName + ".xml"
        doc = parse(path)
        rootBeacon = doc.documentElement
        
        r = dict()
        r["upRoom"]=None
        r["downRoom"]=None
        r["leftRoom"]=None
        r["rightRoom"]=None

        return r

def show(r):
        

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