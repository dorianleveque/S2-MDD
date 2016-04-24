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
sys.path.append('./modules/')

# Modules personnalisés
import Game
import Utils
import Player

# Interaction clavier
old_settings = termios.tcgetattr(sys.stdin)

# Donnee du jeu
direction = "None"


######### Test ###########
player = Player .create()
#########################


def init():
        #interaction clavier
        tty.setcbreak(sys.stdin.fileno())
        
        run()


def show():
        #affichage du joueur
        sys.stdout.write("O\n")
        

def run():        
        while True:
                interact()
                move()
        
def move():
        global player, direction      
       
        #deplacement du joueur:
        x, y = Player.getPosition(player)

        if direction == 'Up': Player.setPosition(player, x, y+1)
        if direction == 'Down': Player.setPosition(player, x, y-1)
        if direction == 'Right': Player.setPosition(player, x+1, y)
        if direction == 'Left': Player.setPosition(player, x-1, y)
        direction = " "

        print Player.getPosition(player)    
        

def interact(): 
        global direction
       
        #gestion des evenements clavier
        if isData():                                    #si une touche est appuyee
                read = sys.stdin.read(1)
                if read == "\x1b": 
                        quit()                          # \x1b = touche echap / appel de la fonction qui permet de quitter le jeu
                elif read == "z": 
                        direction = "Up"                # le joueur se déplace vers Direction Haut
                elif read == "q": 
                        direction = "Left"              # le joueur se déplace vers Direction Gauche
                elif read == "s": 
                        direction = "Down"              # le joueur se déplace vers Direction Bas
                elif read == "d": 
                        direction = "Right"             # le joueur se déplace vers Direction Droite
                #elif read == "p":                      # appel de la fonction pause
                #elif read == "\x08": 
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)   # Permet de vider, le buffer des touches d'entree

                

def isData():
        #recuperation des elements clavier
        return select.select([sys.stdin], [], [], termios.TCIOFLUSH) == ([sys.stdin], [], [])

def quit():
        #restauration des parametres du terminal
        global old_settings
        
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        sys.exit()
init()  
