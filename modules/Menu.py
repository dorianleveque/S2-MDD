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
        menu["temp"] = []               # liste de nom de fenetre temporaire pour savoir d'où on vient 
        
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
                        for i in parameterForm.split("/"):
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
                        
                        dataButton["cmd"] = []
                        cmd = thisButton.getAttribute("cmd")
                        for c in cmd.split("/"):
                                dataButton["cmd"].append(c)                        
                        
                        button["list"].append(dataButton)
                        
                        #Attribuer un bouton de selectionner pour l'initialisation dans chacune des fenetres
                        button["selected"] = dict()
                        dataButton2 = {"name": buttonTag[0].firstChild.nodeValue, "state":False}
                        button["selected"].update(dataButton2)

                data = {"background": background, "texts": texts, "buttons": button}
                
                window = {windowName : data}
                menu["windows"].update(window)
        return menu


# Attribue le nom et les donnees à afficher dans la fenetre courante
def setCurrentWindow(menu, windowName):
        menu["current"].update({"name": windowName})

# Renvoie le nom de la fenetre courante
def getCurrentWindowName(menu):
        return menu["current"]["name"]

# Renvoie le nom de la fenetre courante
def getCurrentWindowName2(menu):
        return "'"+menu["current"]["name"]+"'"

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
        windowName = getCurrentWindowName(menu)
        return menu["windows"][windowName]["background"]["text"]

# Renvoie les couleurs de l'image de fond de la fenetre indiquée
def getBackgroundColor(menu):
        windowName = getCurrentWindowName(menu)
        return menu["windows"][windowName]["background"]["color"]


# Affiche la fenetre courante
def show(menu):
        showFrame(menu)
        showBackground(menu)
        showTexts(menu)
        showButtons(menu)
        
def showFrame(menu):
        # Afficher le cadre de la fenetre que si on est pas en jeu
        if not gameWindow(menu):
                frame = getFrame(menu)
                for y in range(0, len(frame)):
                        Utils.goto(0, y)
                        for x in range(0, len(frame[y])):
                                Utils.write(frame[y][x], 'dark gray', 'black')
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


# Renvoie la liste des boutons de la fenetre courante
def getButtonList(menu):
        windowName = getCurrentWindowName(menu)
        return menu["windows"][windowName]["buttons"]["list"]       # renvoie un dictionnaire {'name'= nom du bouton affiche dans terminal, 'position' = tupple (x,y), 'target' = liste de nom de fenetre}

# Renvoie le bouton selectionne 
def getButtonSelectedName(menu):
        windowName = getCurrentWindowName(menu)
        return menu["windows"][windowName]["buttons"]["selected"]["name"]   # renvoie le nom du bouton selectionne

# Affecter un bouton selectionne
def setButtonSelectedName(menu, buttonName):
        windowName = getCurrentWindowName(menu)
        menu["windows"][windowName]["buttons"]["selected"]["name"] = buttonName     # Définie le bouton nom selectionne

def getButtonSelectedState(menu):
        windowName = getCurrentWindowName(menu)
        return menu["windows"][windowName]["buttons"]["selected"]["state"]   # renvoie l'etat du bouton selectionne Vrai ou Faux

def setButtonSelectedState(menu, state):
        windowName = getCurrentWindowName(menu)
        menu["windows"][windowName]["buttons"]["selected"]["state"] = state         # Definie l'etat du bouton selectionnee
        

def setButtonName(menu, newKey):
        windowName = getCurrentWindowName(menu)
        buttonList = getButtonList(menu)
        buttonSelected = getButtonSelectedName(menu)
        index = getIndexOfSelectedButton(menu, buttonList, buttonSelected)
        
        menu["windows"][windowName]["buttons"]["list"][index]["name"] = newKey
        setButtonSelectedName(menu, newKey)                


def showButtons(menu):
        # Afficher les boutons de la fenetre courante
        for button in list(getButtonList(menu)):
                name = button["name"]
                x, y = button["position"]
                
                Utils.goto(x,y)
                if name == getButtonSelectedName(menu):
                        if getButtonSelectedState(menu):
                                Utils.write("> "+name+"\n", "black", "red")
                        else:
                                Utils.write("> "+name+"\n", "black", "white")
                else : 
                        Utils.write("  "+name+"\n", "white", "black")      

# Renvoie les textes avec leurs parametres
def getTexts(menu):
        windowName = getCurrentWindowName(menu)
        return menu["windows"][windowName]["texts"]                 # renvoie une liste de dictionnaire contenant chaque parametre de chaque text
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

def changeSelectedButton(menu, action):
        
        # Changer le bouton selectionne de la fenetre      
        buttonSelected = getButtonSelectedName(menu)
        buttonList = getButtonList(menu)
        index = getIndexOfSelectedButton(menu, buttonList, buttonSelected)
        
        if action == "buttonUp":
                if index-1 >= 0:
                        setButtonSelectedName(menu, buttonList[index-1]["name"])
                        
        elif action == "buttonDown":
                if index+1 <= len(buttonList)-1:
                        setButtonSelectedName(menu, buttonList[index+1]["name"])


def addTemporyCommande(menu, commande):
        menu["temp"].append(commande)

def executeTemporyCommandes(menu):
        tempList = menu["temp"]
        for t in tempList:
                exec t
                tempList.remove(t)
                        
def getIndexOfSelectedButton(menu, buttonList, buttonSelected):         # renvoie l'index du bouton selectionne de la liste button
        # Recherche de l'index dans buttonList
        index = 0
        for i in range(0, len(buttonList)):
                if buttonList[i]["name"] == buttonSelected:
                        return index
                index += 1

def getButtonActions(menu, index):
        windowName = getCurrentWindowName(menu)
        return menu["windows"][windowName]["buttons"]["list"][index]["cmd"] # renvoie la liste de commande du bouton selectionne et valide


if __name__ == "__main__":
        #initialisation
        menu = create()
        setCurrentWindow(menu,"mainMenu")
        
        print menu["current"]
        
        addTemporyCommande(menu,'setCurrentWindow(menu,'+getCurrentWindowName(menu)+')')
        print menu["temp"]
        print getTemporyCommandes(menu) 
        print menu["temp"]
        setCurrentWindow(menu, 'options')
        print menu["current"]
        exec getTemporyCommandes(menu)
        
        print menu["current"]
        #print getButtonActions(menu, getIndexOfSelectedButton(menu, getButtonList(menu), getButtonSelectedName(menu)))
        #print executButtonAction(menu, getButtonActions(menu, getIndexOfSelectedButton(menu, getButtonList(menu), getButtonSelectedName(menu))))
        ##setCurrentWindow(menu,"Options")
        #print menu["current"]
        #print getCurrentWindowName(menu)
        #print getCurrentWindowData(menu)
        #print getCurrentWindowBackgroundContent(menu)
        #show(menu)