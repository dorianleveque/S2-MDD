# -*- coding: utf-8 -*-
##################################################################
##                                                              ##
##           The Legend Of Zelda - A Link to the Rogue          ##
##          Un projet de Methode de Developpement (MDD)         ##
##                                                              ##
##                           Utils.py                           ##
##                                                              ##
## LEVEQUE Dorian & ROUE Evan   S2P     ENIB         22/04/2016 ##
##################################################################

import sys

def goto(x=0, y=0):
        s_x = str(int(x))
        s_y = str(int(y))
        txt = "\033[" + s_y + ";" + s_x + "H"
        sys.stdout.write(txt)
