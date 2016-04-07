# -*- coding: utf-8 -*-

def goto(x, y):
        s_x = str(int(x+1))
        s_y = str(int(y+1))
        txt = "\033[" + s_y + ";" + s_x + "H"
        sys.stdout.write(txt)
