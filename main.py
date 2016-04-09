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
import modules.Game

def goto(x, y):
        s_x = str(int(x+1))
        s_y = str(int(y+1))
        txt = "\033[" + s_y + ";" + s_x + "H"
        sys.stdout.write(txt)
