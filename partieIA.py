import utilitaire
from re import match
from random import randrange

def PartieIA():
    ficL = open("C:\\Users\\Ulysse Dahiez\\Documents\\AP3\\Algorithmique\\DM_1\\config.txt", "r")
    IALevel = int(list(str(ficL.read()))[1])
    ficL.close()
    IA(IALevel)
    
                
    return

def IA(IALevel):
    dataPartie = {"player1":{"1":2,"2":3,"3":2}, "player2":{"1":2,"2":3,"3":2}, "dataGrille":{}}
    
    Symbole = ""
    joueur = 1
    playerAv = True
    while utilitaire.win(dataPartie, joueur, True) == 0 or playerAv == True:
        if(joueur == 1):
            if(IALevel == 3):
                dataPartie = placerGobeletIASimple(dataPartie)

            if(IALevel == 4):
                dataPartie = placerGobeletIAComplexe(dataPartie)
            joueur = 2
            playerAv = False
        else:
            joueur = 1
            utilitaire.AfficheGrille(dataPartie, 1)
            dataPartie = utilitaire.placerGoblet(dataPartie, 1)[0]
        
    return

def placerGobeletIASimple(dataPartie):
    findPlace = False
    
    while findPlace == False:
        vLigne = randrange(1, 4)
        vColonne = randrange(1, 4)
        for symbole in range(1,4):

            if(utilitaire.placeOk(dataPartie, symbole, vLigne, vColonne, 2)):
                
                EntrerDicoV =  utilitaire.EntrerDico(dataPartie, symbole, vLigne, vColonne, 2)
                dataPartie = EntrerDicoV[0]
                findPlace = True
                break


    return dataPartie

"""
 
"""

def placerGobeletIAComplexe(dataPartie):
    findPlace = False
    dataG = dataPartie["dataGrille"]
    regexW = "[o0O]{3}"
    DicoCoupsPossible = {}
    for i in range(1,4):
            for j in range(1,4):
                valVerifL = valVerifL + str(dataG.get(str(i)+str(j)))
                valVerifC = valVerifC + str(dataG.get(str(j)+str(i)))
                if(match(regexW, valVerifL) or match(regexW, valVerifC)):
                    return
    
    while findPlace == False:
        vLigne = 1
        vColonne = 1
        

  
        for symbole in range(1,4):

            if(utilitaire.placeOk(dataPartie, symbole, vLigne, vColonne, 2)):
                
                EntrerDicoV =  utilitaire.EntrerDico(dataPartie, symbole, vLigne, vColonne, 2)
                dataPartie = EntrerDicoV[0]
                findPlace = True
                break

    return

