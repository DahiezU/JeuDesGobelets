import utilitaire

def PartieIA():
    ficL = open("C:..\\config.txt", "r")
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
    dataPartie = {"player1":{"petit":2,"moyen":3,"grand":2}, "player2":{"petit":2,"moyen":3,"grand":2}, "dataGrille":{}}
    
    Symbole = ""
    errorEnter = False
    
    playerAv = True
    while utilitaire.win(dataPartie, 1, True) == 0 or playerAv == True:

        

        dataPartie = utilitaire.placerGobeletIASimple(dataPartie)
        if(utilitaire.win(dataPartie, playerAv, False)):
            playerAv = False
        else:
            placerGobletV = utilitaire.placerGoblet(dataPartie, 1, errorEnter)
            dataPartie = placerGobletV[0]
            errorEnter = placerGobletV[1]


        if(errorEnter):
            errorEnter = False
        
    return

def IAComplexe():
    return

