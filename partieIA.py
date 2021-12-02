import utilitaire

def PartieIA():
    ficL = open("C:\\Users\\Ulysse Dahiez\\Documents\\AP3\\Algorithmique\\DM_1\\config.txt", "r")
    IALevel = int(list(str(ficL.read()))[1])
    ficL.close()
    if (IALevel == 3):
        IASimple()
    elif(IALevel == 4):
        IAComplexe()
    else:
        print("\n Configurez une IA.")
        input("\nPressez entrer pour revenir au menu.\n ")
                
        return

def IASimple():
    dataPartie = {"player1":{"1":2,"2":3,"3":2}, "player2":{"1":2,"2":3,"3":2}, "dataGrille":{}}
    
    Symbole = ""
    joueur = 1
    playerAv = True
    while utilitaire.win(dataPartie, 1, True) == 0 or playerAv == True:
        
        
        if(joueur == 1):

            dataPartie = utilitaire.placerGobeletIASimple(dataPartie)
            joueur = 2
            playerAv = False
        else:
            joueur = 1
            utilitaire.AfficheGrille(dataPartie, 1)
            dataPartie = utilitaire.placerGoblet(dataPartie, 1)
        
    return

def IAComplexe():
    return

