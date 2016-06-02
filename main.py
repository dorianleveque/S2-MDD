# -*- coding: utf-8 -*-
##################################################################
##								##
##	     The Legend Of Zelda - A Link to the Rogue		##
##	    Un projet de Methode de Developpement (MDD) 	##
##								##
##			      Main.py				##
##								##
## LEVEQUE Dorian & ROUE Evan 	S2P 	ENIB	     01/04/2016 ##
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


# Interaction clavier
old_settings = termios.tcgetattr(sys.stdin)

# Donnee du jeu
direction = "None"

game = Game.create()
menu = Menu.create()

refresh = True

def init():
        #interaction clavier
        tty.setcbreak(sys.stdin.fileno())
        
        #cacher le curseur
        os.system('setterm -cursor off')
        #os.system('setterm -repeat off')
        
        Menu.setCurrentWindow(menu, "mainMenu")

def run():
        n = 0
        global game, menu
        while True:

                if Menu.gameWindow(menu):
                        #if(n % 10):
                                #effacer la console 
                                #sys.stdout.write("\033[2J")
                        Menu.show(menu)
                        Game.run(game)
                else:
                        if refresh==True:
                                Menu.show(menu)
                interact()
                time.sleep(0.2)
                n += 1

def interact(): 
        global direction, refresh, game
       
        refresh = False
        #gestion des evenements clavier
        if isData():                                    #si une touche est appuyee
                read = sys.stdin.read(1)
                time.sleep(0.2)
                #if Menu.gameWindow(menu):
                        #Menu.interact(menu, read)
                        #Game.interact(game, read)
                        
                #else:
                        #Menu.interact(menu, read)
                Game.interact(game, read)
                Menu.interact(menu, read)
                
                if read == "\x1b": 
                        quit()                          # \x1b = touche echap / appel de la fonction qui permet de quitter le jeu
                        
                refresh = True
                
                
        while isData():
                sys.stdin.read(5)
                #termios.tcflush(sys.stdin, termios.TCIFLUSH)   # Permet de vider, le buffer des touches d'entree

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
