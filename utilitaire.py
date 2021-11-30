from re import match
from random import randrange
import bonus

def placeOk(data, symbole, vLigne, vColonne):
    dataPlace = data["dataGrille"].get(str(vLigne)+str(vColonne))
    
    if(vColonne < 0 or vColonne > 4 or vLigne < 0 or vLigne > 4 or symbole < 0 or symbole > 4):
        return False
    if(dataPlace == None):
        return True
    elif(symbole == 3):
        if(dataPlace == "O" or dataPlace == "X"):
            return False
        else:
            return True
    elif(symbole == 2):
        if(dataPlace == "0" or dataPlace == "O" or dataPlace == "x" or dataPlace == "X"):
            return False
        else:
            return True
    elif(symbole == 1):
        if(dataPlace == "." or dataPlace == "o" or dataPlace == "0" or dataPlace == "x" or dataPlace == "O" or dataPlace == "X"):
            return False
        else:
            return True
    

"""
11 22 33 
31 22 13
"""
def win(data, player, conditions):
    dataG = data.get("dataGrille")
    dataP1 = data.get("player1")
    dataP2 = data.get("player2")
    regexW = "[.xX]{3}|[o0O]{3}"
    valVerifL = ""
    valVerifC = ""
    tabVal = []
    valVerifD1 = str(dataG.get("11"))+str(dataG.get("22"))+str(dataG.get("33"))
    valVerifD2 = str(dataG.get("31"))+str(dataG.get("22"))+str(dataG.get("13"))
    for i in range (1, 4):
        for j in range(1,4):

            valVerifL = valVerifL + str(dataG.get(str(i)+str(j)))
            valVerifC = valVerifC + str(dataG.get(str(j)+str(i)))
            if(match(regexW, valVerifL) != None or match(regexW, valVerifC) != None or match(regexW, valVerifD1) != None or match(regexW, valVerifD2) != None ):
                
                AfficheGrille(data, player)
                if(conditions):
                    print("\n   --- Joueur ",player," Gagne ---\n")
                    input("\nPressez entrer pour revenir au menu.\n ")
                               
                return 4
                
            tabVal.append(dataG.get(str(i)+str(j)))
        
                
        valVerifL = ""
        valVerifC = ""

    if(len(dataG) > 8):
                 
        RMoy = dataP1.get("moyen")+dataP2.get("moyen")
        if(tabVal.count("X")+tabVal.count("X")>3 and (RMoy==0 or (RMoy==1 and data.get("player"+str(player).get("moyen"))))):
            print("Egalité entre les deux joueurs.")
            return 5

    if(dataP1.get("petit")==0 and dataP1.get("moyen")==0 and dataP1.get("grand")==0 and dataP2.get("petit")==0 and dataP2.get("moyen")==0 and dataP2.get("grand")==0):
        print("Egalité entre les deux joueurs.")
        return 3
    
    else:
        return 0


def AfficheGrille(data, player):
    dataG = data.get("dataGrille")
    dataP1 = data.get("player1")
    dataP2 = data.get("player2")
    print("\n           1     2     3")
    print("        +-----+-----+-----+")
    for i in range (1,4):
        print("    ",str(i)," | ",dataG.get(str(i)+'1', " ")," | ",dataG.get(str(i)+"2", " ")," | ",dataG.get(str(i)+"3", " ")," |")
        print("        +-----+-----+-----+")
    print("\n +------------+--------------------------+--------------------------+-------------------------+")
    if(player == 1):    
        print(" | Joueur ",str(player)," | ", "Petit (.) (N°1) : [",dataP1.get("petit"), "] | Moyens (x) (N°2) : [",dataP1.get("moyen"), "] | Grand (X) (N°3) : [",dataP1.get("grand"), "] | ")
    elif(player == 2):
        print(" | Joueur ",str(player)," | ", "Petit (o) (N°1) : [",dataP2.get("petit"), "] | Moyens (0) (N°2) : [",dataP2.get("moyen"), "] | Grand (O) (N°3) : [",dataP2.get("grand"), "] |")
    print(" +------------+--------------------------+--------------------------+-------------------------+")

def placerGobeletIASimple(dataPartie):
    findPlace = False
    
    while findPlace == False:
        vLigne = randrange(1, 4)
        vColonne = randrange(1, 4)
        for symbole in range(1,4):
            if(placeOk(dataPartie, symbole, vLigne, vColonne)):
                
                EntrerDicoV =  EntrerDico(dataPartie, symbole, vLigne, vColonne, 3)
                dataPartie = EntrerDicoV[0]
                findPlace = True
                break


    return dataPartie


def placerGoblet(dataPartie, player, errorEnter):
    if(player == 3):
        bonus.animationLoad()
    AfficheGrille(dataPartie, player)
    try:
        symbole = int(input("\nEntrez un numéro de symbole : "))
        vLigne = int(input("Entrez un numéro de ligne : "))
        vColonne = int(input("Entrez un numéro de colonne : "))
        EntrerDicoV =  EntrerDico(dataPartie, symbole, vLigne, vColonne, player)
        dataPartie = EntrerDicoV[0]
        errorEnter = EntrerDicoV[1]
        if(errorEnter == True):
            print("\nCombinaison impossible, essayez autre chose.")
        #voir si il faut mettre une tab ici
        return dataPartie, errorEnter 
    except ValueError:
        placerGoblet(dataPartie, player, errorEnter)
    


def EntrerDico(dataPartie, symbole, vLigne, vColonne, player):
    errorEnter = False
    if(placeOk(dataPartie, symbole, vLigne, vColonne)):
        if(symbole == 1 and player == 1 and dataPartie["player1"]["petit"] > 0):
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "."
            dataPartie["player1"]["petit"] = dataPartie["player1"]["petit"] -1
        elif(symbole == 2 and player == 1 and dataPartie["player1"]["moyen"] > 0):
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "x"
            dataPartie["player1"]["moyen"] = dataPartie["player1"]["moyen"] -1
        elif(symbole == 3 and player == 1 and dataPartie["player1"]["grand"] > 0):
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "X"
            dataPartie["player1"]["grand"] = dataPartie["player1"]["grand"] -1
        elif(symbole == 1 and (player == 2 or player == 3) and dataPartie["player2"]["petit"] > 0):
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "o"
            dataPartie["player2"]["petit"] = dataPartie["player2"]["petit"] -1
        elif(symbole == 2 and (player == 2 or player == 3) and dataPartie["player2"]["moyen"] > 0):
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "0"
            dataPartie["player2"]["moyen"] = dataPartie["player2"]["moyen"] -1
        elif(symbole == 3 and (player == 2 or player == 3) and dataPartie["player2"]["grand"] > 0):
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "O"
            dataPartie["player2"]["grand"] = dataPartie["player2"]["grand"] -1
        else:
            print("Vous avez placé tout vos gobelets")
    else:
        errorEnter = True
    return dataPartie, errorEnter