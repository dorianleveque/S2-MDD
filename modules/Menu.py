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
import select
# Modules personnalisés
import Utils


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
                        
                        dataButton["target"] = []
                        target = thisButton.getAttribute("target")
                        for i in target.split(", "):
                                dataButton["target"].append(i)
                        
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

# Savoir si on se trouve dans la fenetre de jeu
def gameWindow(menu):
        if getCurrentWindowName(menu) == "game":
                return True
        else:
                return False
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
        if not gameWindow(menu):
                frame = getFrame(menu)
                for y in range(0, len(frame)):
                        Utils.goto(0, y)
                        for x in range(0, len(frame[y])):
                                Utils.write(frame[y][x], 'white', 'black')
                        Utils.write("\n")


def showBackground(menu):      
        # Afficher le fond de la fenetre courante
        color, backgroundColor = getBackgroundColor(menu)
        background = getBackground(menu)
        
        for y in range(0, len(background)):
                for x in range(0, len(background[y])):
                        if background[y][x] != " ":
                                Utils.goto(x,y)                                           # A reutiliser pour affichage
                                Utils.write(background[y][x]+"\n", color, backgroundColor)


# Renvoie la liste des boutons
def getButtonList(menu):
        return menu["current"]["data"]["buttons"]["list"]       # renvoie un dictionnaire {'name'= nom du bouton affiche dans terminal, 'position' = tupple (x,y), 'target' = liste de nom de fenetre}

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
                        Utils.write("> "+name+"\n", "black", "white")
                else : 
                        Utils.write("  "+name+"\n", "white", "black")      

# Renvoie les textes avec leurs parametres
def getTexts(menu):
        return menu["current"]["data"]["texts"]                 # renvoie une liste de dictionnaire contenant chaque parametre de chaque text
                                                                # {'text'= texte, 'position'=(x,y), 'color'=(color, backgroundColor), 'form'=forme du texte}

def showTexts(menu):
        # Afficher les texts de la fenetre
        for t in list(getTexts(menu)):
                text = t["text"]
                color, backgroundColor = t["color"]
                form = t["form"]
                x, y = t["position"]

                Utils.goto(x,y)
                Utils.write(text+"\n", color, backgroundColor, form)


def interact(menu, key):
   

        if key == "z": 
                changeSelectedButton(menu, "buttonUp")

        elif key == "s":
                changeSelectedButton(menu, "buttonDown")
        
        elif key == "d":
                changeSelectedButton(menu, "confirm")
                
        elif key == "p":
                if gameWindow(menu):
                        target = []
                        target.append("pause")
                        changeCurrentWindow(menu, target)

def changeSelectedButton(menu, action):
        
        # Changer le bouton selectionne de la fenetre     
        buttonSelected = getButtonSelected(menu)
        buttonList = getButtonList(menu)
        
        # Recherche de l'index dans buttonList
        index = 0
        for i in range(0, len(buttonList)):
                if buttonList[i]["name"] == buttonSelected:
                        break
                index += 1
        
        if action == "buttonUp":
                if index-1 >= 0:
                        setButtonSelected(menu, buttonList[index-1]["name"])
                        
        elif action == "buttonDown":
                if index+1 <= len(buttonList)-1:
                        setButtonSelected(menu, buttonList[index+1]["name"])
        
        # Valider le choix de la fenetre
        elif action == "confirm":
                if gameWindow(menu) == False:
                        changeCurrentWindow(menu, buttonList[index]["target"])                  # Changement de fenetre


def addPreviousWindow(menu, previousWindow):
        menu["transitions"].append(previousWindow)

def getPreviousWindow(menu):
        return menu["transitions"]


def changeCurrentWindow(menu, buttonTargetList):
        
        # Recherche dans la liste du bouton selectionne si celui-ci contient plus de 1 cible (target). On pourra considerer
        # ainsi qu'il s'agit du bouton retour.
        
        if len(buttonTargetList) >= 2: 
                index = getPreviousWindow(menu)
                setCurrentWindow(menu, index[-1]) 
                del index[-1]
        
        elif len(buttonTargetList) == 1:
                if buttonTargetList[0] != ' ':
                        addPreviousWindow(menu, getCurrentWindowName(menu))
                        setCurrentWindow(menu, buttonTargetList[0])



if __name__ == "__main__":
        #initialisation
        menu = create()
        setCurrentWindow(menu,"mainMenu")
        
        print menu["current"]
        ##setCurrentWindow(menu,"Options")
        #print menu["current"]
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
        