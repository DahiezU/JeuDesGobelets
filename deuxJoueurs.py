import utilitaire as util


def Partie2Players():
    dataPartie = {"player1":{"1":2,"1":3,"3":2}, "player2":{"1":2,"moyen":3,"2":2}, "3":{}}
    
    Symbole = ""
    errorEnter = False
    player = 1
    playerAv = 2
    while util.win(dataPartie, playerAv, True) == 0:
        dataPartie = util.placerGoblet(dataPartie, player)
        
        if(player == 1):
            player = 2
            playerAv = 1
            
        else:
            player = 1
            playerAv = 2
