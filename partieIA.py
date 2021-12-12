import utilitaire
from re import match
from random import randrange

def PartieIA():
    ficL = open("config.txt", "r")
    IALevel = int(list(str(ficL.read()))[1])
    ficL.close()
    IA(IALevel)
    
                
    return

    """
    fonctionne 
    "dataGrille":{"21":"o","22":"O"}

    fonctionne pas
    "dataGrille":{"12":"o","22":"O"}
    "dataGrille":{"13":"o","33":"O"}
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


def placerGobeletIAComplexe(dataPartie):
    findPlace = False
    dataG = dataPartie["dataGrille"]
    regex2 = "[o0Oe]{3}"
    valVerifL = ""
    valVerifC = ""
    ListOC = [[(2,2)],[(1,1),(1,3),(3,1),(3,3)],[(1,2),(2,1),(2,3),(3,2)]]
    myListToChange = [".","x"]

    valVerifD1 = str(dataG.get("11", "e"))+str(dataG.get("22", "e"))+str(dataG.get("33", "e"))
    valVerifD2 = str(dataG.get("31", "e"))+str(dataG.get("22", "e"))+str(dataG.get("13", "e"))


    if(findPlace ==False):
        
        if(valVerifD1.count("e")==0 and (valVerifD1.count(".") +  valVerifD1.count("x") == 1) ):
            
            for p in range(1,4):
                
                if(utilitaire.placeOk(dataPartie, p, valVerifD1.find(".")+1, valVerifD1.find(".")+1, 2) and valVerifD1.count(".") == 1 ):
                   
                    dataPartie = placerPlusPetitGoblet(dataPartie, valVerifD1.find(".")+1, valVerifD1.find(".")+1)[0]
                    findPlace = True
                    break

                if(utilitaire.placeOk(dataPartie, p, valVerifD1.find("x")+1, valVerifD1.find("x")+1, 2) and valVerifD1.count("x") == 1):
                    
                    dataPartie = placerPlusPetitGoblet(dataPartie, valVerifD1.find("x")+1, valVerifD1.find("x")+1)[0]
                    findPlace = True
                    break
            
    

        
        if(valVerifD2.count("e")==0 and (valVerifD2.count(".") + valVerifD2.count("x") == 1)):
            
            tabD2 = [(3,1),(2,2),(1,3)]
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
                
                    elif(utilitaire.placeOk(dataPartie, p, q[0], valVerifD2.find("X")+1, 2)):
                        
                        dataPartie = placerPlusPetitGoblet(dataPartie, q[0], q[1])[0]
                        findPlace = True
                        break
                    
                
                
        
        for r in myListToChange:

            valVerifD1 = valVerifD1.replace(r,"e")
            valVerifD2 = valVerifD1.replace(r,"e")
        
        if(match(regex2, valVerifD1) != None and valVerifD1.count("e")==1 and findPlace == False):
                
            dataPartie = placerPlusPetitGoblet(dataPartie, valVerifD1.find("e")+1, valVerifD1.find("e")+1)[0]
            
            findPlace = True

        if(match(regex2, valVerifD2) != None and valVerifD2.count("e")==1 and findPlace == False):
            
            for n in range(1,4):
                for o in range(1,4):
                    if(utilitaire.placeOk(dataPartie, o, valVerifD2.find("e")+1, n , 2)):
                        dataPartie = placerPlusPetitGoblet(dataPartie, valVerifD2.find("e")+1, n)[0]
                        findPlace = True

    if(findPlace == False):
        
        for i in range(1,4): # Ligne
            for j in range(1,4): # Colonne
                if(findPlace == False): 

                        
                    symbo = str(dataG.get(str(i)+str(j), "e")) 
                    if(symbo == "." or symbo== "x"):
                        symbo = "e"
                    valVerifL = valVerifL + symbo
                    
                    for m in range(1,4):
                        pOL = utilitaire.placeOk(dataPartie, m, i, valVerifL.find("e")+1 , 2)
                        pOC = utilitaire.placeOk(dataPartie, m, valVerifC.find("e")+1, i , 2)
                    


                    if( match(regex2, valVerifL) != None  and valVerifL.count("e")==1 and pOL == True ):
                        
                        dataPartie = placerPlusPetitGoblet(dataPartie, i, valVerifL.find("e")+1)[0]
                        
                        findPlace = True
                        break

                    #pour les lignes
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
    # pour alligner deux pions
    print("fp : ", findPlace)

    
    if(findPlace == False and (dataG.get("22") != "o" or dataG.get("22") != "0" or dataG.get("22") != "O" and( dataG.get("22") == "X" or dataG.get("22") != None))):
        print("ca passe")
        listS = ["o","0","O"]
        for t in range(1,4):
            for u in range(1,4):
                
                thisCurentVal = dataG.get(str(t)+str(u))
                boolTCV = (thisCurentVal == "o" or  thisCurentVal == "0" or thisCurentVal == "O")
                if(findPlace == False and boolTCV and ( u != 2 and t != 2)):
                    
                    for v in range(1,4):
                        thisVal = dataG.get(str(t+1)+str(u))
                        
                        if(u+1 < 4 and utilitaire.placeOk(dataPartie, v, t+1, u, 2) and thisVal != "o" and thisVal != "0" and thisVal != "O" and findPlace == False):  
                            dataPartie = placerPlusPetitGoblet(dataPartie, t+1, u)[0]
                            findPlace = True
                            break
                        thisVal = dataG.get(str(t)+str(u+1))
                        if(t+1 < 4 and utilitaire.placeOk(dataPartie, v, t, u+1, 2) and thisVal != "o" and thisVal != "0" and thisVal != "O" and findPlace == False):  
                            dataPartie = placerPlusPetitGoblet(dataPartie, t, u+1)[0]
                            findPlace = True
                            break

                        thisVal = dataG.get(str(t-1)+str(u))
                        if(u-1 < 0, utilitaire.placeOk(dataPartie, v, t-1, u, 2) and thisVal != "o" and thisVal != "0" and thisVal != "O" and findPlace == False):  
                            dataPartie = placerPlusPetitGoblet(dataPartie, t-1, u)[0]
                            findPlace = True
                            break

                        thisVal = dataG.get(str(t)+str(u-1))
                        if(t-1 < 0, utilitaire.placeOk(dataPartie, v, t, u-1, 2) and thisVal != "o" and thisVal != "0" and thisVal != "O" and findPlace == False):  
                            dataPartie = placerPlusPetitGoblet(dataPartie, t, u-1)[0]
                            findPlace = True
                            break
                       



    if(findPlace == False):
        
        for l  in range (0,len(ListOC)):
            for s in range (0, len(ListOC[l])):
                lenLOC = len(ListOC[l])
                if(lenLOC>0):
                    
                    m = randrange(0,len(ListOC[l]))
                    
                    for k in range(1,4):
                        if(findPlace == False):

                            thisVal = dataG.get(str(ListOC[l][m][0])+str(ListOC[l][m][1]))
                            if(utilitaire.placeOk(dataPartie, k, ListOC[l][m][0], ListOC[l][m][1], 2) and thisVal != "o" and thisVal != "0" and thisVal != "O"):
                                
                                dataPartie = placerPlusPetitGoblet(dataPartie, ListOC[l][m][0], ListOC[l][m][1])[0]
                                findPlace = True
                                break
                    del ListOC[l][m]
            
                        
    return dataPartie
                
            
    
        

def placerPlusPetitGoblet(dataPartie, vLigne, vColonne):
    findPlace = False
    for symbole in range(1,4):

        if(utilitaire.placeOk(dataPartie, symbole, vLigne, vColonne, 2)):
            
            EntrerDicoV =  utilitaire.EntrerDico(dataPartie, symbole, vLigne, vColonne, 2)
            dataPartie = EntrerDicoV[0]
            findPlace = True
            break

    return dataPartie, findPlace

