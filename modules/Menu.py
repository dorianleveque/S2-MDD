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

# Modules personnalisés
import Utils


# constructeur du menu #

def create():
        menu = dict()
        menu["current"] = dict()
        menu["windows"] = dict()
        menu["transitions"] = []        #<-------------- A MODIFIER
        
        # recuperation des infos du fichier xml pour la construction du menu
        path = "./../assets/menu/Menu.xml"
        doc = parse(path)
        rootElement = doc.documentElement
        
        # recuperation des noms et des données de chaque fenetre pour la creation du dictionnaire menu
        windowNodes = rootElement.getElementsByTagName("windows")
        windowSize = windowNodes.length
        
        for i in range(windowSize):
                node = windowNodes[i]
                
                #Permet de recuperer le nom de la fenetre pour chaque balise i
                windowName = node.getAttribute("name")
                #print node.attributes.keys()  #permet de recuperer le nom de chaque attribut
                
                
                
                #Recuperation des donnees de chaque fenetre                      #Data
                data = []
                
                #Recuperation du fond de la fenetre
                background=dict()
                background["content"] = []
                background["color"] = []
                
                backgroundNode = rootElement.getElementsByTagName("background")[i]

                background["content"] = backgroundNode.firstChild.nodeValue          #Recuperation du texte stocke entre les balises

                
                if backgroundNode.hasAttributes():
                        color = backgroundNode.getAttribute("color")
                        backgroundColor = backgroundNode.getAttribute("backgroundColor")
                        background["color"] = (color, backgroundColor)
                
               
               
                #Recuperation des textes de la fenetre
                texts=[]
                textNodes = node.getElementsByTagName("text")                       # Balises de texte dans liste textNodes
                numberText = textNodes.length                                       # Nombre de balises text de la fenetre
                for t in range(numberText):
                        # la variable nodeT stocke, a chaque tour de boucle une balise text dans l'ordre où elle se trouve dans le fichier
                        nodeT = textNodes[t]                                     
                        text=dict()
                        
                        text["content"] = nodeT.firstChild.nodeValue
                        x = nodeT.getAttribute("x")
                        y = nodeT.getAttribute("y")
                        text["position"] = (x,y)
                        
                        color = nodeT.getAttribute("color")
                        backgroundColor = nodeT.getAttribute("backgroundColor")
                        text["color"] = (color, backgroundColor)
                        
                        text["form"] = nodeT.getAttribute("form")
                        
                        texts.append(text)
                
                #Recuperation des buttons de la fenetre
                button=dict()
                button["selected"]=None
                button["list"]=[]
                
                buttonNodes = node.getElementsByTagName("button")
                numberButton = buttonNodes.length
                for b in range(numberButton):
                        # la variable nodeB stocke, a chaque tour de boucle une balise button dans l'ordre où elle se trouve dans le fichier
                        nodeB = buttonNodes[b]
                        buttonName = nodeB.firstChild.nodeValue
                        button["list"].append(buttonName)
                        
                        #Attribuer un bouton de selectionner pour l'initialisation dans chacune des fenetres
                        button["selected"]=buttonNodes[0].firstChild.nodeValue

                data = {"background": background, "texts": texts, "buttons": button}
                
                window = {windowName : data}
                menu["windows"].update(window)
        return menu


# Renvoie le nom de la fenetre courante
def getCurrentWindowName(menu):
        return menu["current"]["name"]

# Renvoie les donnees de la fenetre courante
def getCurrentWindowData(menu):
        return menu["current"]["data"]



# Renvoie le texte-image du fond de la fenetre
def getCurrentWindowBackgroundContent(menu):
        return menu["current"]["data"]["background"]["content"]

# Renvoie les couleurs de l'image de fond de la fenetre
def getCurrentWindowBackgroundColor(menu):
        return menu["current"]["data"]["background"]["color"]



# Renvoie la liste des boutons
def getCurrentWindowButtonList(menu):
        return menu["current"]["data"]["buttons"]["list"]

# Renvoie le bouton selectionne 
def getCurrentWindowButtonSelected(menu):
        return menu["current"]["data"]["buttons"]["selected"]



# Renvoie les textes avec leurs parametres
def getCurrentWindowText(menu):
        return menu["current"]["data"]["texts"]



# Attribue le nom et les donnees à afficher dans la fenetre courante
def setCurrentWindow(menu, windowName):
        for window in menu["windows"]:
                if window == windowName:
                        name = window
                        data = menu["windows"][window]
                        menu["current"].update({"name": name, "data": data})  #current["Name"], current["data"]
                        break

def getBackgroundWindowContent(menu):
        return menu["windows"]["frameWork"]["background"]["content"]

def getBackgroundWindowColor(menu):
        return menu["windows"]["frameWork"]["background"]["color"]


# Affiche la fenetre courante
def show(menu):
        #Afficher le fond de la fenetre
        Utils.goto(0,0)                                                         # A reutiliser pour affichage
        background = getBackgroundWindowContent(menu)
        color, backgroundColor = getBackgroundWindowColor(menu)
        Utils.setTextColor(color, backgroundColor)
        sys.stdout.write(background)
        
        Utils.goto(0,0)  
        foreground = getCurrentWindowBackgroundContent(menu)
        color, backgroundColor = getCurrentWindowBackgroundColor(menu)
        Utils.setTextColor(color, backgroundColor)
        sys.stdout.write(foreground)
        
        
        #affichage des boutons
        #xb = 60
        #yb = 36
        #for b in list(getCurrentWindowButtonList(menu)):
                #Utils.goto(xb,yb+b)
                #button = b
                #sys.stdout.write(button)
                
        
        
        
        #affichage des textes
        for t in list(getCurrentWindowText(menu)):
                texte = t["content"]
                color, backgroundColor = t["color"]
                form = t["form"]
                x, y = t["position"]

                Utils.goto(x,y)
                Utils.setTextForm(form)
                Utils.setTextColor('"'+color+'"', '"'+backgroundColor+'"')
                sys.stdout.write(texte)
                Utils.resetText()
                
        
        
        
        
        
        

#def interact():
        
#def changeWindow():

#def createTransition():

#def addTransition():

if __name__=="__main__":
        #initialisation
        menu = create()
        setCurrentWindow(menu,"mainMenu")
        
        #print menu["current"]
        #print getCurrentWindowName(menu)
        #print getCurrentWindowData(menu)
        #print getCurrentWindowBackgroundContent(menu)
        show(menu)

        