import utilitaire
from re import match
from random import randrange

"""
PartieIA() regarde le niveau de l'ia renrté dans la config et lance la partie

"""


def PartieIA():
    ficL = open("config.txt", "r")
    IALevel = int(list(str(ficL.read()))[1])
    ficL.close()
    IA(IALevel)
    
                
    return

"""
IA() lance la partie
elle possède aussi le dictionnaire, ce qui est le squelette en quelque sort de la partie.
tant que personne ne gagne (entre le joueur et l'IA) la partie continue, 
elle appel une fonction différente en fonction du niveau de l'ia.
"""

def IA(IALevel):
    dataPartie = {"player1":{"1":2,"2":3,"3":2}, "player2":{"1":2,"2":3,"3":2},"dataGrille":{}}
    
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

            utilitaire.AfficheGrille(dataPartie, 1)
            dataPartie = utilitaire.placerGoblet(dataPartie, 1)[0]
            joueur = 1
        
        print(dataPartie)
        
    return

"""
placerGobeletIASimple() place des goblets de manière alléatoire dans le jeu.
mais elle ne peut jouer au dessus de d'un gobelet dont elle n'a pas le pouvoir.
"""

def placerGobeletIASimple(dataPartie):
    findPlace = False
    dataBase = dataPartie
    while findPlace == False:
        vLigne = randrange(1, 4)
        vColonne = randrange(1, 4)
        resPPPG = placerPlusPetitGoblet(dataPartie, vLigne, vColonne)
        dataPartie = resPPPG[0]
        findPlace = resPPPG[1]

    return dataPartie
"""
placerGobeletIAComplexe() se place de manière plus intéligente, elle ne cherche qu'à gagner 
et pas à contrer son adversaire
au fil du code des commentaires sont indiqué pour savoir ce que font les conditions.

cette classe est entièrement commenté car beaucoup plus complexe que le reste.

"""

def placerGobeletIAComplexe(dataPartie):
    findPlace = False
    dataG = dataPartie["dataGrille"]
    regex2 = "[o0Oe]{3}"
    valVerifL = ""
    valVerifC = ""
    ListOC = [[(2,2)],[(1,1),(1,3),(3,1),(3,3)],[(1,2),(2,1),(2,3),(3,2)]]
    myListToChange = [".","x"]

    #on aligne dans une string les ellements
    valVerifD1 = str(dataG.get("11", "e"))+str(dataG.get("22", "e"))+str(dataG.get("33", "e"))
    valVerifD2 = str(dataG.get("31", "e"))+str(dataG.get("22", "e"))+str(dataG.get("13", "e"))
    
    # Pour les diagonnales si elle peut être gangnante
    if(findPlace ==False):
        if(valVerifD1.count("e")==0 and (valVerifD1.count(".") +  valVerifD1.count("x") == 1) and valVerifD1.count("X") == 0 ):
        #si elle doit jouer au dessus d'un pion de l'adversaire elle le fait 
            for p in range(1,4): # pour regarder si une place est disponible
                
                # on peut regarder sa position avec sa position dans la string
                if(utilitaire.placeOk(dataPartie, p, valVerifD1.find(".")+1, valVerifD1.find(".")+1, 2) and valVerifD1.count(".") == 1 ):
                   
                    dataPartie = placerPlusPetitGoblet(dataPartie, valVerifD1.find(".")+1, valVerifD1.find(".")+1)[0]
                    findPlace = True
                    break
                
                if(utilitaire.placeOk(dataPartie, p, valVerifD1.find("x")+1, valVerifD1.find("x")+1, 2) and valVerifD1.count("x") == 1):
                    
                    dataPartie = placerPlusPetitGoblet(dataPartie, valVerifD1.find("x")+1, valVerifD1.find("x")+1)[0]
                    findPlace = True
                    break
            
    

        # pour la deuxième diagonnale
        if(valVerifD2.count("e")==0 and (valVerifD2.count(".") + valVerifD2.count("x") == 1) and valVerifD2.count("X") == 0):
        
            tabD2 = [(3,1),(2,2),(1,3)]
            #on regarde pour toute les positions de la diagonale si c'est placable
            for q in  tabD2:
                for p in range(1,4):
                    
                    if(utilitaire.placeOk(dataPartie, p, q[0], q[1], 2)):
                        
                        dataPartie = placerPlusPetitGoblet(dataPartie, q[0], q[1])[0]
                        findPlace = True
                        break

                    elif(utilitaire.placeOk(dataPartie, p, q[0], valVerifD2.find(".")+1, 2)):

                        dataPartie = placerPlusPetitGoblet(dataPartie, q[0], q[1])[0]
                        findPlace = True
                        break

                    elif(utilitaire.placeOk(dataPartie, p, q[0], valVerifD2.find("x")+1, 2)):

                        dataPartie = placerPlusPetitGoblet(dataPartie, q[0], q[1])[0]
                        findPlace = True
                        break
                
                
        
        #Pour les deux diagonnales
        for r in myListToChange:# changer les . x par des e dans la string
            
            valVerifD1 = valVerifD1.replace(r,"e")
            valVerifD2 = valVerifD2.replace(r,"e")
        # Si un placement est possible, on le fait avec la position du e 
        if(match(regex2, valVerifD1) != None and valVerifD1.count("e")==1 and findPlace == False):
            
            dataPartie = placerPlusPetitGoblet(dataPartie, valVerifD1.find("e")+1, valVerifD1.find("e")+1)[0]
            
            findPlace = True
        #pareil pour la deuxième diagonale mais comme x et y sont différent, on boucle sur y
        if(match(regex2, valVerifD2) != None and valVerifD2.count("e")==1 and findPlace == False):
           
            for n in range(1,4):
                if(findPlace == False):
                    for o in range(1,4):
                        
                        if(findPlace == False, utilitaire.placeOk(dataPartie, o, n, valVerifD2.find("e")+1 , 2)):
                            
                            dataPartie = placerPlusPetitGoblet(dataPartie, n, valVerifD2.find("e")+1)[0]
                            findPlace = True
                            break


    # Pour les lignes et les colonnes si elles peuvent être gagnante.


    if(findPlace == False):
        
        for i in range(1,4): # Ligne
            for j in range(1,4): # Colonne
                if(findPlace == False): 

                    # change les None . x par des e pour avoir la position
                    symbo = str(dataG.get(str(i)+str(j), "e")) 
                    if(symbo == "." or symbo== "x"):
                        symbo = "e"
                    valVerifL = valVerifL + symbo
                    

                    # regarde si une place est disponible dans les colonnes (et alignable)
                    for m in range(1,4):
                        pOL = utilitaire.placeOk(dataPartie, m, i, valVerifL.find("e")+1 , 2)
                        pOC = utilitaire.placeOk(dataPartie, m, valVerifC.find("e")+1, i , 2)
                    

                    #pour les colonnes
                    if( match(regex2, valVerifL) != None  and valVerifL.count("e")==1 and pOL == True ):
                        
                        dataPartie = placerPlusPetitGoblet(dataPartie, i, valVerifL.find("e")+1)[0]
                        
                        findPlace = True
                        break

                    #pareil pour les lignes
                    symb = str(dataG.get(str(j)+str(i), "e")) 
                    if(symb == "." or symb== "x"):
                        symb = "e"
                    valVerifC = valVerifC + symb
                    if(match(regex2, valVerifC) != None and valVerifC.count("e")==1 and pOC == True ):
                        
                        dataPartie = placerPlusPetitGoblet(dataPartie, valVerifC.find("e")+1, i)[0]
                        findPlace = True
                        break
                
            valVerifL = ""
            valVerifC = ""

    # si il n'y aucune combinaison gangnante en un coup, s'alligner avec un pions
    # unquement si la 'ia n'est pas en possetion du centre (sinon dans tout les cas on sera à coté d'elle)
    if(findPlace == False and (dataG.get("22") != "o" and dataG.get("22") != "0" and dataG.get("22") != "O" and( dataG.get("22") == "X" or dataG.get("22") != None))):
        
        
        for t in range(1,4):
            for u in range(1,4):
                
                thisCurentVal = str(dataG.get(str(t)+str(u)))
                
                boolTCV = ((thisCurentVal == "o") or  (thisCurentVal == "0") or (thisCurentVal == "O"))

                nimp = ( u == 2 and t == 2) == True
                if(findPlace == False and boolTCV and nimp == False): # l'ia regarde si la boucle ne la met pas au centre, et si elle est bien positionné sur une case qu'elle possède
                    # dans la suite on regarde tout autour d'elle si une case est disponible
                    for v in range(1,4):
                        thisVal = dataG.get(str(t+1)+str(u))
                        #en dessous
                        if(t+1 < 4 and utilitaire.placeOk(dataPartie, v, t+1, u, 2) and thisVal != "o" and thisVal != "0" and thisVal != "O" and findPlace == False):  
                            
                            dataPartie = placerPlusPetitGoblet(dataPartie, t+1, u)[0]
                            findPlace = True
                            break
                        thisVal = dataG.get(str(t)+str(u+1))
                        
                        #à droite
                        if(u+1 < 4 and utilitaire.placeOk(dataPartie, v, t, u+1, 2) and thisVal != "o" and thisVal != "0" and thisVal != "O" and findPlace == False):  
                            
                            dataPartie = placerPlusPetitGoblet(dataPartie, t, u+1)[0]
                            findPlace = True
                            break

                        thisVal = dataG.get(str(t-1)+str(u))
                        #au dessus
                        if(t-1 > 0 and utilitaire.placeOk(dataPartie, v, t-1, u, 2) and thisVal != "o" and thisVal != "0" and thisVal != "O" and findPlace == False):  
                            
                            dataPartie = placerPlusPetitGoblet(dataPartie, t-1, u)[0]
                            findPlace = True
                            break
                        # à gauche
                        thisVal = dataG.get(str(t)+str(u-1))
                        if(u-1 > 0 and utilitaire.placeOk(dataPartie, v, t, u-1, 2) and thisVal != "o" and thisVal != "0" and thisVal != "O" and findPlace == False):  
                            
                            dataPartie = placerPlusPetitGoblet(dataPartie, t, u-1)[0]
                            findPlace = True
                            break
                       

    # si aucune des précédentes combnaisons sont possible, se placer au milieu, ou dans les coins ou dans les arêtes
    
    if(findPlace == False):
        
        for l  in range (0,len(ListOC)):#parcours la liste de liste des cases
            for s in range (0, len(ListOC[l])):#parcours les cases
                lenLOC = len(ListOC[l])
                if(lenLOC>0):
                    
                    m = randrange(0,len(ListOC[l]))#prend une case à jouer au hasard 
                    
                    for k in range(1,4):
                        if(findPlace == False):

                            thisVal = dataG.get(str(ListOC[l][m][0])+str(ListOC[l][m][1])) #prend la valeur
                            if(utilitaire.placeOk(dataPartie, k, ListOC[l][m][0], ListOC[l][m][1], 2) and thisVal != "o" and thisVal != "0" and thisVal != "O"):
                                
                                dataPartie = placerPlusPetitGoblet(dataPartie, ListOC[l][m][0], ListOC[l][m][1])[0]
                                findPlace = True
                                break
                    del ListOC[l][m] #supprime de la liste si elle n'est pas disponnible (pour ne pas retomber dessus)
            
                        
    return dataPartie
                
            
"""
placerPlusPetitGoblet() place le plus petit gobelet place le plus petit gobelet à 
des coordonées donnée.
elle test avec placeOk si il n'est pas possible de placer le gobelet, 
alors elle renvoie un false en seconde position.


"""
        

def placerPlusPetitGoblet(dataPartie, vLigne, vColonne):
    findPlace = False
    for symbole in range(1,4):

        if(utilitaire.placeOk(dataPartie, symbole, vLigne, vColonne, 2)):
            
            EntrerDicoV =  utilitaire.EntrerDico(dataPartie, symbole, vLigne, vColonne, 2)
            dataPartie = EntrerDicoV[0]
            findPlace = True
            break

    return dataPartie, findPlace

