from re import match

"""

Dans ce fichier nous trouvons toutes les fonctions qui servent à la fois pour 
la partie deux joueur que pour la partie IA, ces fonctions sont les interactions avec la 
dataPartie, c'est à dire ce qui va modifier le cours de la partie ( modifier le dictionnaire)

"""

"""
placeOk sert à verifier si la place avec le symbole rentrée est bien disponnible
elle renvoie un boolean
si la place est ok True 
si elle ne l'est pas False

"""

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

win() retourne 0 tant qu'il n'y pas de combinaison gagnante
sinon elle va affichier le gagnant 
l'ia est toujours le joueur deux.

win verifie d'abord les digonal et apres les cases dans le sens des colonnes et dans le sens 
des lignes en même temps.

win() verifie aussi que les joureurs ne sont pas égalité. (si ils n'ont plus de jetons 
ou si il n'y a plus de place disponible)

elle vérifie tout ça selon ses coordonées qui sont le nom de l'ellement dans le dictionnaire.

dans cette partie j'ai utilisé une technique non vue en cours; les regex.
pour voir si les pions sont victorieux ou non, je mets les trois gobelets dans 
une string et je vois si la string match avec ma regex de victoire.
ma regex de victoire retourne true si 

"""

def win(data, player, conditions):
    dataG = data.get("dataGrille")
    dataP1 = data.get("player1")
    dataP2 = data.get("player2")
    regexW = "[.xX]{3}|[o0O]{3}" #regex 
    valVerifL = ""
    valVerifC = ""
    tabVal = []
    #fabrication des string de diagonnal pour le match avec la regex
    valVerifD1 = str(dataG.get("11"))+str(dataG.get("22"))+str(dataG.get("33"))
    valVerifD2 = str(dataG.get("31"))+str(dataG.get("22"))+str(dataG.get("13"))
    for i in range (1, 4):
        for j in range(1,4):

            # fabrication de la string pour le match avec la regex
            valVerifL = valVerifL + str(dataG.get(str(i)+str(j)))
            valVerifC = valVerifC + str(dataG.get(str(j)+str(i)))
            # annalyse si regex match avec une des diagonales ou une des ligne ou une des colonnes 
            if(match(regexW, valVerifL) != None or match(regexW, valVerifC) != None or match(regexW, valVerifD1) != None or match(regexW, valVerifD2) != None ):
            # ça passe si ça a matché
                
                if(conditions== True):
                    AfficheGrille(data, player)
                    print("\n     +------------------------+")
                    print("     |    Joueur ",player," Gagne    |")
                    print("     +------------------------+ \n")
                    input("\nPressez entrer pour revenir au menu.\n ")
                               
                return 4
            if(dataG.get(str(i)+str(j)) != None):
                tabVal.append(dataG.get(str(i)+str(j)))
        
                
        valVerifL = ""
        valVerifC = ""

   

    if(len(dataG) > 8):
                 
        GDMoy = dataP1.get("3")+dataP2.get("3")
        MGMoy = tabVal.count("x")+tabVal.count("0")
        MDMoy = dataP1.get("2")+dataP2.get("2")
        MMMoy = tabVal.count(".")+tabVal.count("o")

        # condition d'egalité, si toutes les cases prise ne sont plus jouable par aucun des joueurs
        
        if((MGMoy==5 and GDMoy==0) or (MDMoy == 0 and GDMoy == 0) or(MMMoy + MGMoy == 5 and GDMoy == 0 and MDMoy ==0) ):
            

            AfficheGrille(data, player)
            print("\n     +--------------------------------+")
            print("     | Egalité entre les deux joueurs |")
            print("     +--------------------------------+\n")
            input("\nPressez entrer pour revenir au menu.\n ")
            
            return 5
    
    #condition d'égalité si les deux joueurs n'ont plus de jetons 
    elif(dataP1.get("1")==0 and dataP1.get("2")==0 and dataP1.get("3")==0 and dataP2.get("1")==0 and dataP2.get("2")==0 and dataP2.get("3")==0):
        
        AfficheGrille(data, player)
        print("\n     +--------------------------------+")
        print("     | Egalité entre les deux joueurs |")
        print("     +--------------------------------+\n")
        input("\nPressez entrer pour revenir au menu.\n ")
        return 3
    
    else:
        return 0

"""

afficherGrille(), affiche la grille avec les nombres de gobelets restant au joueur 
qui est en train de jouer.

"""
def AfficheGrille(data, player):
    dataG = data.get("dataGrille")
    dataP1 = data.get("player1")
    dataP2 = data.get("player2")
    print("\n               1     2     3")
    print("            +-----+-----+-----+")
    for i in range (1,4):
        print("        ",str(i)," | ",dataG.get(str(i)+'1', " ")," | ",dataG.get(str(i)+"2", " ")," | ",dataG.get(str(i)+"3", " ")," |")
       
        print("            +-----+-----+-----+")
        
    print("\n +------------+")
    if(player == 1):    # on affiche ce qu'il reste au joueur
        print(" | Joueur ",str(player)," | ",)
        print(" +------------+------------+--------------------------+-------------------------+")
        print( " | Petit (.) (N°1) : [",dataP1.get("1"), "] | Moyens (x) (N°2) : [",dataP1.get("2"), "] | Grand (X) (N°3) : [",dataP1.get("3"), "] | ")

    elif(player == 2):
        print(" | Joueur ",str(player)," | ",)
        print(" +------------+------------+--------------------------+-------------------------+")
        print( " | Petit (.) (N°1) : [",dataP2.get("1"), "] | Moyens (x) (N°2) : [",dataP2.get("2"), "] | Grand (X) (N°3) : [",dataP2.get("3"), "] | ")

    print(" +-------------------------+--------------------------+-------------------------+")


"""
placerGobelet() place un gobelet en fonction de ce que rentre le joueur dans le jeu.

elle ne sert que pour les joueurs, les ia placent leurs gobelet dans la partie IA.
"""


def placerGoblet(dataPartie, player):
    errorEnter = False
    it_is = True
    replay = False
   
    symbole = input("\nEntrez un numéro de symbole : ")
    vLigne = input("Entrez un numéro de ligne : ")
    vColonne = input("Entrez un numéro de colonne : ")
    

    if(symbole.isnumeric() and vLigne.isnumeric() and vColonne.isnumeric()): # on verifie que ce sont bien des entiers pour ne pas faire planter au moment de la conversion
        if(int(symbole)<4 and int(symbole) > 0 and int(vLigne)<4 and int(vLigne) > 0 and int(vColonne)<4 and int(vColonne) > 0):
            symbole = int(symbole)
            vLigne = int(vLigne)
            vColonne = int(vColonne)
            
            it_is = True
        else:
            it_is = False
    else:
        it_is = False
    if(it_is == True):
        if(placeOk(dataPartie, symbole, vLigne, vColonne, player)):
            EntrerDicoV =  EntrerDico(dataPartie, symbole, vLigne, vColonne, player)
            dataPartie = EntrerDicoV[0]
            errorEnter = EntrerDicoV[1]
            return dataPartie, errorEnter
            
        else:   
            replay = True
    else:
        replay = True
    if(replay == True):
        AfficheGrille(dataPartie, player)
        print("\n     +-------------------------+")
        print("     | Combinaison impossible. |")
        print("     +-------------------------+\n")
        dataPartie = placerGoblet(dataPartie, player)[0] # si la combinaison n'est pas bonne, on recommence
        return dataPartie, errorEnter

"""
EntrerDico() rentre dans le dico ce que nous lui donnont.

elle rentre simplement la valeur. si la place n'est pas disponible elle retourne un False.

le nom du simbole dans le dico sont ses coordonnés.

"""

def EntrerDico(dataPartie, symbole, vLigne, vColonne, player):
    errorEnter = False
    if(placeOk(dataPartie, symbole, vLigne, vColonne, player)):
        if(symbole == 1 and player == 1 and dataPartie["player1"]["1"] > 0): # verifie qu'il a encore des gobelets
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "." # Place dans la grille
            dataPartie["player1"]["1"] = dataPartie["player1"]["1"] -1 # on enlève un goblet de son jeu
        
        elif(symbole == 2 and player == 1 and dataPartie["player1"]["2"] > 0): # pareil
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "x"
            dataPartie["player1"]["2"] = dataPartie["player1"]["2"] -1
        elif(symbole == 3 and player == 1 and dataPartie["player1"]["3"] > 0):# pareil
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "X"
            dataPartie["player1"]["3"] = dataPartie["player1"]["3"] -1
        elif(symbole == 1 and player == 2  and dataPartie["player2"]["1"] > 0):# pareil
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "o"
            dataPartie["player2"]["1"] = dataPartie["player2"]["1"] -1
        elif(symbole == 2 and player == 2  and dataPartie["player2"]["2"] > 0):# pareil
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "0"
            dataPartie["player2"]["2"] = dataPartie["player2"]["2"] -1
        elif(symbole == 3 and player == 2  and dataPartie["player2"]["3"] > 0):# pareil
            dataPartie["dataGrille"][str(vLigne)+str(vColonne)] = "O"
            dataPartie["player2"]["3"] = dataPartie["player2"]["3"] -1
        else:
            print("Vous avez placé tout vos gobelets de taille ", symbole)
    else:
        errorEnter = True
    return dataPartie, errorEnter