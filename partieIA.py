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
        dataPartie = placerPlusPetitGoblet(dataPartie, vLigne, vColonne)


    return dataPartie

"""
 
"""

def placerGobeletIAComplexe(dataPartie):
    findPlace = False
    dataG = dataPartie["dataGrille"]
    regex2 = "[o0O]{2}"
    coorP = []
    DicoCoupsPossible = {}
    for i in range(1,4): # Ligne
            for j in range(1,4): # Colonne
                if(dataG.get( str(i)+str(j))== None):
                    coorP =  [i, j]
                valVerifL = valVerifL + str(dataG.get(str(i)+str(j)), "")
                
                if(dataG.get( str(j)+str(i))== None):
                    coorP = [i,j]
                valVerifC = valVerifC + str(dataG.get(str(j)+str(i)), "")
                
                if(match(regex2, valVerifL) or match(regex2, valVerifC)):

                    dataPartie = placerPlusPetitGoblet(dataPartie, coorP[0], coorP[1])
                    findPlace = True
    
    if(findPlace == False):
        for k in range(1,4):
            if(utilitaire.placeOk(dataPartie, k, 2, 2, 2)):
                dataPartie = placerPlusPetitGoblet(dataPartie, 2, 2)
                findPlace = True
        for l in range(1,4):
            if(utilitaire.placeOk(dataPartie, k, 1, 1, 2)):
                dataPartie = placerPlusPetitGoblet(dataPartie, 2, 2)
                findPlace = True
            elif(utilitaire.placeOk(dataPartie, k, 1, 3, 2)):
                dataPartie = placerPlusPetitGoblet(dataPartie, 2, 2)
                findPlace = True
            elif(utilitaire.placeOk(dataPartie, k, 3, 1, 2)):
                dataPartie = placerPlusPetitGoblet(dataPartie, 2, 2)
                findPlace = True
            elif(utilitaire.placeOk(dataPartie, k, 3, 3, 2)):
                dataPartie = placerPlusPetitGoblet(dataPartie, 2, 2) 
                findPlace = True
        
    return dataPartie
                
            
    
        

def placerPlusPetitGoblet(dataPartie, vLigne, vColonne):
    for symbole in range(1,4):

        if(utilitaire.placeOk(dataPartie, symbole, vLigne, vColonne, 2)):
            
            EntrerDicoV =  utilitaire.EntrerDico(dataPartie, symbole, vLigne, vColonne, 2)
            dataPartie = EntrerDicoV[0]
            findPlace = True
            break

    return dataPartie

