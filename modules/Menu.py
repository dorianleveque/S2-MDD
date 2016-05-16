# -*- coding: utf-8 -*-
##################################################################
##								##
##	     The Legend Of Zelda - A Link to the Rogue		##
##	    Un projet de Methode de Developpement (MDD) 	##
##								##
##			      Menu.py				##
##								##
## LEVEQUE Dorian & ROUE Evan 	S2P 	ENIB	     03/05/2016 ##
##################################################################

# Modules système
from xml.dom.minidom import parse
import sys
import select
# Modules personnalisés
import Utils
import Game


# constructeur du menu #
def create():
        menu = dict()
        menu["current"] = dict()
        menu["windows"] = dict()       # dictionnaire contenant toutes les informations de chaque fenetres 
        menu["transitions"] = []       # liste de nom des fenetres precedemment parcouru                  #<-------------- A MODIFIER
        
        # recuperation des infos du fichier xml pour la construction du menu
        path = "assets/menu/Menu.xml"           # chemin d'acces du fichier xml
        #path = "./../assets/menu/Menu.xml"
        doc = parse(path)
        rootElement = doc.documentElement
        
        # Recuperation du cadre appliqué sur chaque fenetres du jeu
        frameNodes = rootElement.getElementsByTagName("frame")
        frame = frameNodes[0].firstChild.nodeValue.split("\n")
        frameData = dict()
        frameData["frame"] = []
        for frameLine in frame:
                frameData["frame"].append(list(frameLine))
        menu["current"].update(frameData)
        
        
        
        
        # recuperation des noms et des données de chaque fenetre pour la creation du dictionnaire menu
        windowNodes = rootElement.getElementsByTagName("windows")       # windowNodes est une liste de toutes les balises windows
        windowSize = windowNodes.length
        
        
        
        # Pour chaque balise se nommant "windows" de la liste "windowNodes", 
        # on récupère son nom ("windowName") et ses donnees ("data") pour les placées dans le dictionnaire "menu",
        # qui aura pour clé le nom de celle-ci.
        
        for i in range(windowSize):
                # Recuperation du nom de la fenetre pour chaque balise i
                windowTag = windowNodes[i]
                                
                windowName = windowTag.getAttribute("name")
                #print windowTag.attributes.keys()  #permet de recuperer le nom de chaque attribut
                
                
                
                #Recuperation des donnees de chaque fenetre                      #Data
                data = []
                
                #Recuperation du fond de la fenetre
                background=dict()
                background["text"] = []
                background["color"] = []
                
                backgroundTag = windowTag.getElementsByTagName("background")[0]
                container = backgroundTag.firstChild.nodeValue.split("\n")       # Recuperation du texte stocke entre les balises background

                for line in container:
                        background["text"].append(list(line))

                
                if backgroundTag.hasAttributes():
                        color = backgroundTag.getAttribute("color")
                        backgroundColor = backgroundTag.getAttribute("backgroundColor")
                        background["color"] = (color, backgroundColor)
                else:
                        background["color"] = (" "," ")
               
               
                #Recuperation des textes de la fenetre
                texts=[]
                textTag = windowTag.getElementsByTagName("text")                  # textTag est une liste de toutes les balises nommées "text" de chaque fenetre
                numberText = textTag.length                                       # Nombre de balises text de la fenetre
                for t in range(numberText):
                        # la variable thisText stocke, a chaque tour de boucle une balise text dans l'ordre où elle se trouve dans le fichier
                        thisText = textTag[t]                                     
                        text=dict()
                        
                        text["text"] = thisText.firstChild.nodeValue # Recuperation du contenue de la fenetre
                        x = thisText.getAttribute("x")                  # Recuperation de la position du text en x,y 
                        y = thisText.getAttribute("y")
                        text["position"] = (x,y)
                        
                        color = thisText.getAttribute("color")          # Recuperation de la couleur à affecter au text
                        backgroundColor = thisText.getAttribute("backgroundColor")
                        text["color"] = (color, backgroundColor)
                        
                        text["form"] = []                               # Recuperation de la forme de text à affecter
                        parameterForm = thisText.getAttribute("form")        
                        for i in parameterForm.split(", "):
                                text["form"].append(i)
                        
                        texts.append(text)                              # Ajout du dictionnaire de donnees text à la liste texts de la fenetre i
                
                
                
                #Recuperation des buttons de la fenetre
                button=dict()
                button["selected"]=None
                button["list"]=[]
                
                buttonTag = windowTag.getElementsByTagName("button")
                numberButton = buttonTag.length
                for b in range(numberButton):
                        # la variable thisButton stocke, a chaque tour de boucle une balise button dans l'ordre où elle se trouve dans le fichier
                        thisButton = buttonTag[b]
                        dataButton = dict()
                        
                        dataButton["name"] = thisButton.firstChild.nodeValue
                        x = thisButton.getAttribute("x")
                        y = thisButton.getAttribute("y")
                        dataButton["position"] = (x,y)
                        
                        #buttonName = thisButton.firstChild.nodeValue
                        button["list"].append(dataButton)
                        
                        #Attribuer un bouton de selectionner pour l'initialisation dans chacune des fenetres
                        button["selected"]=buttonTag[0].firstChild.nodeValue

                data = {"background": background, "texts": texts, "buttons": button}
                
                window = {windowName : data}
                menu["windows"].update(window)
        return menu


# Attribue le nom et les donnees à afficher dans la fenetre courante
def setCurrentWindow(menu, windowName):
        for window in menu["windows"]:
                if window == windowName:
                        name = window
                        data = menu["windows"][window]
                        menu["current"].update({"name": name, "data": data}) # Attribue le nom et le contenu de la fenetre courante dans le dictionnaire menu["current"]
                        break

# Renvoie le nom de la fenetre courante
def getCurrentWindowName(menu):
        return menu["current"]["name"]
# ---------------------
# Renvoie le cadre 
def getFrame(menu):
        return menu["current"]["frame"]

# Renvoie le texte-image du fond de la fenetre courante
def getBackground(menu):
        return menu["current"]["data"]["background"]["text"]

# Renvoie les couleurs de l'image de fond de la fenetre courante
def getBackgroundColor(menu):
        return menu["current"]["data"]["background"]["color"]


# Affiche la fenetre courante
def show(menu):
        showFrame(menu)
        showBackground(menu)
        showTexts(menu)
        showButtons(menu)
        
def showFrame(menu):
        # Afficher le cadre de la fenetre
        Utils.setTextColor("white", "black")
        
        frame = getFrame(menu)
        for y in range(0, len(frame)):
                Utils.goto(0, y)
                for x in range(0, len(frame[y])):
                        sys.stdout.write(frame[y][x].encode("utf-8"))
                sys.stdout.write('\n')

def showBackground(menu):      
        # Afficher le fond de la fenetre courante
        color, backgroundColor = getBackgroundColor(menu)
        Utils.setTextColor(color, backgroundColor)
        
        background = getBackground(menu)
        for y in range(0, len(background)):
                for x in range(0, len(background[y])):
                        if background[y][x] != " ":
                                Utils.goto(x+2,y+1)                                           # A reutiliser pour affichage
                                sys.stdout.write(background[y][x].encode("utf-8"))
                sys.stdout.write('\n')


# Renvoie la liste des boutons
def getButtonList(menu):
        return menu["current"]["data"]["buttons"]["list"]       # renvoie un dictionnaire {'name'= nom du bouton, 'position' = tupple (x,y)}

# Renvoie le bouton selectionne 
def getButtonSelected(menu):
        return menu["current"]["data"]["buttons"]["selected"]   # renvoie le nom du bouton selectionne

# Affecter un bouton selectionne
def setButtonSelected(menu, buttonName):
        menu["current"]["data"]["buttons"]["selected"] = buttonName     # Définie le bouton selectionne


def showButtons(menu):
        # Afficher les boutons de la fenetre courante
        for button in list(getButtonList(menu)):
                name = button["name"]
                x, y = button["position"]
                
                Utils.goto(x,y)
                if name == getButtonSelected(menu):
                        Utils.setTextColor("black", "white")
                        sys.stdout.write("> "+name.encode("utf-8")+"\n")
                else : 
                        Utils.setTextColor("white", "black")
                        sys.stdout.write("  "+name.encode("utf-8")+"\n")
                Utils.resetTextFormat()        

# Renvoie les textes avec leurs parametres
def getTexts(menu):
        return menu["current"]["data"]["texts"]                 # renvoie une liste de dictionnaire contenant chaque parametre de chaque text
                                                                # {'text'= texte, 'position'=(x,y), 'color'=(color, backgroundColor), 'form'=forme du texte}

def showTexts(menu):
        Utils.resetTextFormat()
        # Afficher les texts de la fenetre
        for t in list(getTexts(menu)):
                Utils.resetTextFormat()
                text = t["text"]
                color, backgroundColor = t["color"]
                form = t["form"]
                x, y = t["position"]

                Utils.goto(x,y)
                Utils.setTextForm(form)
                Utils.setTextColor(color, backgroundColor)
                
                sys.stdout.write(text.encode("utf-8")+"\n")
                


def interact(menu, key):
        
        # Changer le bouton selectionne de la fenetre     
        buttonSelected = getButtonSelected(menu)
        buttonList = getButtonList(menu)
        
        # Recherche du numero d'index dans buttonList
        index = 0
        for i in range(0, len(buttonList)):
                if buttonList[i]["name"] == buttonSelected:
                        break
                index += 1      

        if key == "z": 
                if index-1 >= 0:
                        setButtonSelected(menu, buttonList[index-1]["name"])
        elif key == "s":
                if index+1 <= len(buttonList)-1:
                        setButtonSelected(menu, buttonList[index+1]["name"])
        
        # Valider le choix de la fenetre
        elif key == "d": 
                changeWindow(menu) # Changement de fenetre



def addTransition(menu, nextWindow):
        menu["transitions"].append(nextWindow)

def getTransition(menu):
        return menu["transitions"]


def changeWindow(menu):
        
        buttonSelected = getButtonSelected(menu)
        
        if buttonSelected == "Return" or buttonSelected == "Resume":
                transitionSize = len(getTransition(menu))
                setCurrentWindow(menu, menu["transitions"][transitionSize-1])
        if buttonSelected == "Quit":
                quit() 
        
        else:
                addTransition(menu, getCurrentWindowName(menu))
                setCurrentWindow(menu, buttonSelected)



if __name__ == "__main__":
        #initialisation
        menu = create()
        setCurrentWindow(menu,"mainMenu")
        
        print menu["current"]
        setCurrentWindow(menu,"Options")
        print menu["current"]
        #print getCurrentWindowName(menu)
        #print getCurrentWindowData(menu)
        #print getCurrentWindowBackgroundContent(menu)
        #show(menu)
        #def isData():
                ##recuperation des elements clavier
                #return select.select([sys.stdin], [], [], 0.0) == ([sys.stdin], [], [])
        
 
        
        #while True:
                #getCurrentWindowButtonSelected(menu)
                #if isData():
                        #key = sys.stdin.read(1)
                        #interact(menu, key)
        