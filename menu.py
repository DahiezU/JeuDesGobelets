import deuxJoueurs
import configurations
import partieIA
from sys import version
"""

La fonction menu sert à lancer le jeu
et à entrer dans les différentes choses que le jeu propose

selon l'entrée que nous donnons, elle va rentrer là ou vous voulez (en fonction du jeu.)

des simples print pour afficher les modes ou les crédits

mais le jeu se lance depuis le fichier lancerJeu.py

"""


def menu():
    print("\n     +---------------------+")
    print("     |   JEU DES GOBLETS   |")
    print("     +---------------------+")
    print("\n\n - [1] Nouvelle Partie \n - [2] Options \n - [3] Credits \n - [4] Quitter")
    value = input("\n Selectionnez un numéro : ")
    if(value == "1"):
        newPartie()
    elif(value == "2"):
        configurations.optionsC()
        menu()
    elif(value == "3"):
        print("\n\n Développeur : Ulysse Dahiez \n python version : ",version," \n\n liste des librairies utilisé : \n\n - re du module match (Pour les Regex). \n - randRange du module random.\n - version du module sys. \n\n")
        input("Pressez entrer pour revenir au menu.\n ")
        menu()
    elif(value == "4"):

        print("\nJe reste là pour une nouvelle partie ;) \n")
        exit()
    else:
        print("\nMauvaise touche, essayez une touche entre 1 et 4 \n\n")
        menu()
    
"""

La fonction Partie sert à lancer une nouvelle partie.
Elle va regarder quels modes de jeu sont sélectionné dans le fichier de configuration (simplement ia ou deux joueurs) et lancer le jeu.

"""

def newPartie():
    ficL = open("config.txt", "r")
    nbPlayer = int(list(str(ficL.read()))[0])
    ficL.close()
    if(nbPlayer == 2):
        deuxJoueurs.Partie2Players()
        menu()
    if(nbPlayer == 1):
        partieIA.PartieIA()
        menu()






