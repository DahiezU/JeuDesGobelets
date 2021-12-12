import utilitaire as util

"""
Partie2Players() deux joueurs fait jouer les deux joueurs à tour de rôle, tant que 
personne n'a gagné(ou les joueurs sont exaqueo), la partie ne s'arrete pas
si un joueur fait une mauvaise entrée, il doit refaire sont entrée.

( on a tous droit à l'erreur :) )
"""

def Partie2Players():
    dataPartie = {"player1":{"1":2,"2":3,"3":2}, "player2":{"1":2,"2":3,"3":2}, "dataGrille":{}}
    
    Symbole = ""
    errorEnter = False
    player = 1
    playerAv = 2
    while util.win(dataPartie, playerAv, True) == 0:
        util.AfficheGrille(dataPartie, player)
        resPG = util.placerGoblet(dataPartie, player)
        dataPartie = resPG[0]
        errorEnter = resPG[1]
        if(errorEnter):
            
            errorEnter = False
        else:
            if(player == 1):
                player = 2
                playerAv = 1
                
            else:
                player = 1
                playerAv = 2
