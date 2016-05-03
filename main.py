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
#import Game
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
        
        #cacher le curseur
        os.system('setterm -cursor off')
        os.system('setterm -repeat off')


def show():
        #effacer la console 
        sys.stdout.write("\033[1;1H")
        sys.stdout.write("\033[2J")
        #os.system('setterm -clear all')
       
        
        #affichage du joueur)
        #deplacement du joueur:
        x, y = Player.getPosition(player)
        Utils.goto(x,y)
        sys.stdout.write("Link")
        
        

def run():     
        cmp = 0
        while True:
                interact()
                move()
                if cmp%10==0 : 
                        show()
                time.sleep(0.02)
        
def move():
        global player, direction      
       
        #deplacement du joueur:
        x, y = Player.getPosition(player)
        dt = 0.25

        if direction == 'Up': Player.setPosition(player, x, y-1*dt)
        if direction == 'Down': Player.setPosition(player, x, y+1*dt)
        if direction == 'Right': Player.setPosition(player, x+2*dt, y)
        if direction == 'Left': Player.setPosition(player, x-2*dt, y)
        direction = " "

        
        #print Player.getPosition(player)    
        

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
        
        sys.exit()
init()
run()