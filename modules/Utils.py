# -*- coding: utf-8 -*-
##################################################################
##								##
##	     The Legend Of Zelda - A Link to the Rogue		##
##	    Un projet de Methode de Developpement (MDD) 	##
##								##
##			      Utils.py				##
##								##
## LEVEQUE Dorian & ROUE Evan 	S2P 	ENIB	     22/04/2016 ##
##################################################################

def goto(x, y):
        s_x = str(int(x+1))
        s_y = str(int(y+1))
        txt = "\033[" + s_y + ";" + s_x + "H\n"
        sys.stdout.write(txt)
