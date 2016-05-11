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
                #Permet de recuperer le nom de la fenetre pour chaque balise i
                windowTag = windowNodes[i]
                                
                windowName = windowTag.getAttribute("name")
                #print windowTag.attributes.keys()  #permet de recuperer le nom de chaque attribut
                
                
                
                #Recuperation des donnees de chaque fenetre                      #Data
                data = []
                
                #Recuperation du fond de la fenetre
                background=dict()
                background["content"] = []
                background["color"] = []
                
                backgroundTag = windowTag.getElementsByTagName("background")[0]
                container = backgroundTag.firstChild.nodeValue
                
                ##for line in container:
                        ##background["content"].append(line)
                #print container,
                        
                
                
                background["content"] = container
                #backgroundTag.firstChild.nodeValue          #Recuperation du texte stocke entre les balises

                
                if backgroundTag.hasAttributes():
                        color = backgroundTag.getAttribute("color")
                        backgroundColor = backgroundTag.getAttribute("backgroundColor")
                        background["color"] = (color, backgroundColor)
                else:
                        background["color"] = (" "," ")
               
               
                #Recuperation des textes de la fenetre
                texts=[]
                textTag = windowTag.getElementsByTagName("text")                       # Balises de texte dans liste textTag
                numberText = textTag.length                                       # Nombre de balises text de la fenetre
                for t in range(numberText):
                        # la variable thisText stocke, a chaque tour de boucle une balise text dans l'ordre où elle se trouve dans le fichier
                        thisText = textTag[t]                                     
                        text=dict()
                        
                        text["content"] = thisText.firstChild.nodeValue
                        x = thisText.getAttribute("x")
                        y = thisText.getAttribute("y")
                        text["position"] = (x,y)
                        
                        color = thisText.getAttribute("color")
                        backgroundColor = thisText.getAttribute("backgroundColor")
                        text["color"] = (color, backgroundColor)
                        
                        text["form"] = thisText.getAttribute("form")
                        
                        texts.append(text)
                
                
                
                #Recuperation des buttons de la fenetre
                button=dict()
                button["selected"]=None
                button["list"]=[]
                
                buttonTag = windowTag.getElementsByTagName("button")
                numberButton = buttonTag.length
                for b in range(numberButton):
                        # la variable thisButton stocke, a chaque tour de boucle une balise button dans l'ordre où elle se trouve dans le fichier
                        thisButton = buttonTag[b]
                        buttonName = thisButton.firstChild.nodeValue
                        button["list"].append(buttonName)
                        
                        #Attribuer un bouton de selectionner pour l'initialisation dans chacune des fenetres
                        button["selected"]=buttonTag[0].firstChild.nodeValue

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

def getBackgroundWindow(menu):
        return menu["windows"]["frame"]["background"]



# Affiche la fenetre courante
def show(menu):
       
        
        #Afficher le fond de la fenetre
        Utils.goto(0,0)                                                         # A reutiliser pour affichage
        background = getBackgroundWindow(menu)["content"]
        color, backgroundColor = getBackgroundWindow(menu)["color"]
        Utils.setTextColor(color, backgroundColor)
        sys.stdout.write(background)

        Utils.resetTextFormat()    
        
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

if __name__ == "__main__":
        #initialisation
        menu = create()
        setCurrentWindow(menu,"options")
        
        #print menu["current"]
        #print getCurrentWindowName(menu)
        #print getCurrentWindowData(menu)
        #print getCurrentWindowBackgroundContent(menu)
        show(menu)

        