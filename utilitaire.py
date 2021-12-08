from re import match
import bonus

def placeOk(data, symbole, vLigne, vColonne, player):
    dataPlace = data["dataGrille"].get(str(vLigne)+str(vColonne))
    dataP = data["player"+str(player)]

    if(dataP.get(str(symbole))==0):
        return False
    else:
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
                
                
                if(conditions== True):
                    AfficheGrille(data, player)
                    print("\n   --- Joueur ",player," Gagne ---\n")
                    input("\nPressez entrer pour revenir au menu.\n ")
                               
                return 4
                
            tabVal.append(dataG.get(str(i)+str(j)))
        
                
        valVerifL = ""
        valVerifC = ""

    if(len(dataG) > 8):
                 
        RMoy = dataP1.get("2")+dataP2.get("2")
        if(tabVal.count("X")+tabVal.count("X")>3 and (RMoy==0 or (RMoy==1 and data.get("player"+str(player).get("2"))))):
            print("Egalité entre les deux joueurs.")
            return 5

    if(dataP1.get("1")==0 and dataP1.get("2")==0 and dataP1.get("3")==0 and dataP2.get("1")==0 and dataP2.get("2")==0 and dataP2.get("3")==0):
        print("Egalité entre les deux joueurs.")
        return 3
    
    else:
        return 0


def AfficheGrille(data, player):
    dataG = data.get("dataGrille")
    dataP1 = data.get("player1")
    dataP2 = data.get("player2")
    print("\n              1     2     3")
    print("            +-----+-----+-----+")
    for i in range (1,4):
        print("        ",str(i)," | ",dataG.get(str(i)+'1', " ")," | ",dataG.get(str(i)+"2", " ")," | ",dataG.get(str(i)+"3", " ")," |")
       
        print("            +-----+-----+-----+")
        
    print("\n +------------+--------------------------+--------------------------+-------------------------+")
    if(player == 1):    
        print(" | Joueur ",str(player)," | ", "Petit (.) (N°1) : [",dataP1.get("1"), "] | Moyens (x) (N°2) : [",dataP1.get("2"), "] | Grand (X) (N°3) : [",dataP1.get("3"), "] | ")
    elif(player == 2):
        print(" | Joueur ",str(player)," | ", "Petit (o) (N°1) : [",dataP2.get("1"), "] | Moyens (0) (N°2) : [",dataP2.get("2"), "] | Grand (O) (N°3) : [",dataP2.get("3"), "] |")
    print(" +------------+--------------------------+--------------------------+-------------------------+")





def placerGoblet(dataPartie, player):
    errorEnter = False
    try:
        symbole = int(input("\nEntrez un numéro de symbole : "))
        vLigne = int(input("Entrez un numéro de ligne : "))
        vColonne = int(input("Entrez un numéro de colonne : "))
        it_is = True
    except ValueError:
        it_is = False

    if(placeOk(dataPartie, symbole, vLigne, vColonne, player)):

        if(it_is):
            EntrerDicoV =  EntrerDico(dataPartie, symbole, vLigne, vColonne, player)
            dataPartie = EntrerDicoV[0]
            errorEnter = EntrerDicoV[1]
            return dataPartie, errorEnter
        else:
            AfficheGrille(dataPartie, player)
            print("\n     +-------------------------+")
            print("     | Combinaison impossible. |")
            print("     +-------------------------+\n")
            dataPartie = placerGoblet(dataPartie, player)[0]
            return dataPartie, errorEnter
    else:   
        AfficheGrille(dataPartie, player)
        print("\n     +-------------------------+")
        print("     | Combinaison impossible. |")
        print("     +-------------------------+\n")
        dataPartie = placerGoblet(dataPartie, player)[0]
        return dataPartie, errorEnter



def EntrerDico(dataPartie, symbole, vLigne, vColonne, player):
    errorEnter = False
    if(placeOk(dataPartie, symbole, vLigne, vColonne, player)):
        if(symbole == 1 and player == 1 and dataPartie["player1"]["1"] > 0):
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "."
            dataPartie["player1"]["1"] = dataPartie["player1"]["1"] -1
        elif(symbole == 2 and player == 1 and dataPartie["player1"]["2"] > 0):
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "x"
            dataPartie["player1"]["2"] = dataPartie["player1"]["2"] -1
        elif(symbole == 3 and player == 1 and dataPartie["player1"]["3"] > 0):
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "X"
            dataPartie["player1"]["3"] = dataPartie["player1"]["3"] -1
        elif(symbole == 1 and player == 2  and dataPartie["player2"]["1"] > 0):
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "o"
            dataPartie["player2"]["1"] = dataPartie["player2"]["1"] -1
        elif(symbole == 2 and player == 2  and dataPartie["player2"]["2"] > 0):
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "0"
            dataPartie["player2"]["2"] = dataPartie["player2"]["2"] -1
        elif(symbole == 3 and player == 2  and dataPartie["player2"]["3"] > 0):
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "O"
            dataPartie["player2"]["3"] = dataPartie["player2"]["3"] -1
        else:
            print("Vous avez placé tout vos gobelets de taille ", symbole)
    else:
        errorEnter = True
    return dataPartie, errorEnter