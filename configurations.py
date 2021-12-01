def optionsC():
    print("\n - Nombre de joueurs :\n\n    - [1] Un joueur \n    - [2] Deux joueurs \n\n - Niveau de l'IA :\n\n    - [3] Simple \n    - [4] Avancée \n\n - [5] Retour ")
    value = input("\n Selectionnez un numéro : ")
    
    if(int(value)>=1 and int(value)<=4):
        fichierL = open("C:\\Users\\Ulysse Dahiez\\Documents\\AP3\\Algorithmique\\DM_1\\config.txt", "r")
        fichierec = list(str(fichierL.read()))
        fichierL.close()
        fichier = open("C:\\Users\\Ulysse Dahiez\\Documents\\AP3\\Algorithmique\\DM_1\\config.txt", "w")
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
   