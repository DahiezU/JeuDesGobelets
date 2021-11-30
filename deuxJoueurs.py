import utilitaire as util


def Partie2Players():
    dataPartie = {"player1":{"petit":2,"moyen":3,"grand":2}, "player2":{"petit":2,"moyen":3,"grand":2}, "dataGrille":{}}
    
    Symbole = ""
    errorEnter = False
    player = 1
    playerAv = 2
    while util.win(dataPartie, playerAv, True) == 0:
        pGoblet = util.placerGoblet(dataPartie, player, errorEnter)
        dataPartie = pGoblet[0]
        errorEnter = pGoblet[1]
        

        if(errorEnter):
            errorEnter = False
        else: 
            if(player == 1):
                player = 2
                playerAv = 1
            
            else:
                player = 1
                playerAv = 2
