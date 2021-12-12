
"""
Ce fichier ne comporte qu'une seule fonction
elle est lancé depuis le fichier menu 

elle fonctionne de base comme la fonction menu, sauf que la configuration du mode de jeu est 
enregistré dans un fichier .txt se trouvant dans le même fichier que tout le jeu 

la fonction ouvre le fichier en mode lecture et en mode ecriture, écrit si une configartion
 est changé au momment des entrées et sauvegarde les modifications dans le fichier.


"""

def optionsC():
    print("\n - Nombre de joueurs :\n\n    - [1] Un joueur \n    - [2] Deux joueurs \n\n - Niveau de l'IA :\n\n    - [3] Simple \n    - [4] Avancée \n\n - [5] Retour ")
    value = input("\n Selectionnez un numéro : ")
    
    if(int(value)>=1 and int(value)<=4):
        fichierL = open("config.txt", "r")
        fichierec = list(str(fichierL.read()))
        fichierL.close()
        fichier = open("config.txt", "w")
        if(value == "1"):
            fichierec[0] = "1"
            fichier.write("".join(fichierec))
        elif(value == "2"):
            fichierec[0] = "2"
            fichier.write("".join(fichierec))
        elif(value == "3"):
            fichierec[1] = "3"
            fichier.write("".join(fichierec))
        elif(value == "4"):
            fichierec[1] = "4"
            fichier.write("".join(fichierec))
        fichierec.clear()
        fichier.close()
        optionsC()
    elif(value == "5"):
        return
    else:
        print("\n Mauvaise touche, essayez une touche entre 1 et 5 \n\n")
        optionsC()
   