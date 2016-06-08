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
        s_x = str(int(x)+1)
        s_y = str(int(y))
        txt = "\033[" + s_y + ";" + s_x + "H"
        sys.stdout.write(txt)

def write(text, color="white", backgroundColor="black", textForm = []):
        
        # appliquer de la couleur si indique en parametre
        foreground = dict()
        foreground["black"] = 30
        foreground["red"] = 31
        foreground["green"] = 32
        foreground["yellow"] = 33
        foreground["blue"] = 34
        foreground["magenta"] = 35
        foreground["cyan"] = 36
        foreground["light gray"] = 37
        foreground["dark gray"] = 90
        foreground["light red"] = 91
        foreground["light green"] = 92
        foreground["light yellow"] = 93
        foreground["light blue"] = 94
        foreground["light magenta"] = 95
        foreground["light cyan"] = 96
        foreground["white"] = 97
        
        background = dict()
        background["black"] = 40
        background["red"] = 41
        background["green"] = 42
        background["yellow"] = 43
        background["blue"] = 44
        background["magenta"] = 45
        background["cyan"] = 46
        background["light gray"] = 47
        background["dark gray"] = 100
        background["light red"] = 101
        background["light green"] = 102
        background["light yellow"] = 103
        background["light blue"] = 104
        background["light magenta"] = 105
        background["light cyan"] = 106
        background["white"] = 107
        
        for c in foreground : 
                if c == color:
                        foreColor = str(int(foreground[c]))
                        sys.stdout.write("\033["+foreColor+"m")
                        break
        for b in background :
                if b == backgroundColor:
                        backColor = str(int(background[b]))
                        sys.stdout.write("\033["+backColor+"m")
                        break
        
        # appliquer une mise en forme si indique en parametre
        form = dict()
        form["bold"] = 1
        form["underline"] = 4
        
        for i in textForm:
                for f in form:
                        if f == i:
                                param = str(int(form[f]))
                                sys.stdout.write("\033["+param+"m")
                
        # ecrire dans le terminal:
        sys.stdout.write(text.encode("utf-8"))
        
        # Re-initialisation de la mise en forme et des couleurs
        sys.stdout.write("\033[0m")


if __name__=="__main__":
        #Test 1

        goto(1,20)
        write("test1\n", "red", "white", ["bold"])
        
        goto(10,50)
        write("test2\n", "blue", "light gray", ["underline"])
        
        goto(12,60)
        write("test3\n", "green", "black", ["bold", "underline"])
        
