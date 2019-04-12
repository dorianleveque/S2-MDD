# -*- coding: utf-8 -*-
##################################################################
##                                                              ##
##           The Legend Of Zelda - A Link to the Rogue          ##
##          Un projet de Methode de Developpement (MDD)         ##
##                                                              ##
##                            Main.py                           ##
##                                                              ##
## LEVEQUE Dorian & ROUE Evan   S2P     ENIB         01/04/2016 ##
##################################################################

# Modules système
import sys
import os
import time
import select
import tty 
import termios


# Modules personnalisés
sys.path.append('./modules/')
import Game
import Player
import Menu
import Settings
import Utils


# Interaction clavier
old_settings = termios.tcgetattr(sys.stdin)

# Donnee du jeu
direction = "None"
dt = 0.01

game = Game.create()
settings = Settings.create()
menu = Menu.create()

refresh = True

def init():
        #interaction clavier
        tty.setcbreak(sys.stdin.fileno())
        
        #cacher le curseur
        os.system('setterm -cursor off')        
        Menu.setCurrentWindow(menu, "mainMenu")
        Menu.show(menu)

def run():
        n = 0
        gameState = "run"
        global game, menu, refresh
        
        while True:
                interact()
                if Menu.gameWindow(menu):
                        gameState = Game.run(game, dt)
                        if gameState == "run":
                                if(n % 10):
                                        #effacer la console 
                                        #sys.stdout.write("\033[2J")
                                        Menu.show(menu)
                                        Game.show(game)
                        elif gameState == "lose":
                                Menu.setCurrentWindow(menu, "lose")
                                Menu.show(menu)
                                gameState = "run"
                        elif gameState == "win":
                                Menu.setCurrentWindow(menu, "win")
                                Menu.show(menu)
                                gameState = "run"
                else:
                        if refresh==True:
                                Menu.show(menu)
                time.sleep(dt)
                n += 1

def interact(): 
        global direction, refresh, game, menu
       
        refresh = False
        #gestion des evenements clavier
        if isData():                                    #si une touche est appuyee
                refresh = True                
                key = sys.stdin.read(1)
                if Menu.gameWindow(menu):               # si on est sur le fenetre de jeu alors ...
                        Game.interact(game, settings, key)

                        if key == "p":
                                Menu.setCurrentWindow(menu, "pause")       # faire apparaitre le menu Pause
                else: 
                        if key == "z": 
                                Menu.changeSelectedButton(menu, "buttonUp")

                        elif key == "s":
                                Menu.changeSelectedButton(menu, "buttonDown")
                        
                        elif key == "\n":
                                # Execute les commandes présentent dans la liste de commande à executer du bouton selectionne
                                buttonCmdList = Menu.getButtonList(menu, Menu.getIndexOfSelectedButton(menu, Menu.getButtonList(menu), Menu.getButtonSelected(menu,"name")),"cmd")
                                
                                for cmd in buttonCmdList:
                                        exec cmd
        
                if key == "\x1b": 
                        quit()                          # \x1b = touche echap / appel de la fonction qui permet de quitter le jeu
        
        while isData():
                #sys.stdin.read(5)
                termios.tcflush(sys.stdin, termios.TCIFLUSH)   # Permet de vider, le buffer des touches d'entree


def changeKey(keyName):        
        while not isData():     # Tant qu'il n'y a pas d'autres touche de rentrée
                Menu.setButtonSelected(menu, "state", True)
                Menu.showButtons(menu)
                
        Menu.setButtonSelected(menu, "state", False)
        read = sys.stdin.read(1)  
        canChange = True
        for key in settings:
                if read == settings[key] or read == 'p':
                        canChange = False
        if canChange:
                Settings.setKey(settings,keyName,read)
                Menu.setButtonName(menu, read)
        Menu.showButtons(menu)

def isData():
        #recuperation des elements clavier
        return select.select([sys.stdin], [], [], 0.0) == ([sys.stdin], [], [])     

def quit():
        global old_settings
        #restauration des parametres du terminal
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        
        #rendre visible le curseur
        os.system('setterm -cursor on')
        os.system('setterm -clear all')
        sys.exit()
init()
run()
