import random
from random import randint
import os
# r = random.random()

def ordi():
    joueur = 0
    chifoumi = ["1, 2, 3"]
 
    joueur = int(input("choisir entre 1 pierre 2 papier 3 ciseaux \n"))
    resultat = 0

    while resultat < 3:
        r =randint(1,3)
        if joueur == 1:
            print("vous avez choisi pierre")
        elif joueur == 2:
            print("vous avez choisi papier")
        else:
            print("vous avez choisi ciseaux")


        if r == 1:
            print("ordinateur choisi pierre")
        elif  r ==2:
            print("ordinateur choisi papier")
        else:
            print("ordinateur choisi ciseaux")


        if joueur == 1:
            if r == 2:
                print("ordinateur gagne")
            elif r == 1:
                print("Egalites")
            else:
                print("vous gagnez")


        if joueur == 2:
            if r == 2:
                print("Egalites")
            elif r == 1:
                print("vous gagnez")
            else:
                print("ordinateur gagne")

        if joueur == 3:
            if r == 1:
                print("ordinateur gagne")
            elif r == 2:
                print("vous gagnez")
            else:
                print("Egalites")


        joueur = int(input("choisir entre 1 pierre 2 papier 3 ciseaux \n"))
    resultat = resultat + 1

def vs():
    joueur = 0
    chifoumi = ["1, 2, 3"]

    resultat = 0

    while resultat < 5:
        r =randint(1,3)
        print("le premier joueur joue")
        joueur = int(input("choisir entre 1 pierre 2 papier 3 ciseaux \n"))
    
        os.system('cls')
        print("Au tour du deuxieme joueur")
        joueur2 = int(input("choisir entre 1 pierre 2 papier 3 ciseaux \n"))

        if joueur == 1:
            print("vous avez choisi pierre")
        elif joueur == 2:
            print("vous avez choisi papier")
        else:
            print("vous avez choisi ciseaux")


        if joueur2 == 1:
            print("joueur2 choisi pierre")
        elif joueur2 ==2:
            print("joueur2 choisi papier")
        else:
            print("joueur2 choisi ciseaux")


        if joueur == 1 and joueur2 == 1:
            print("vous etes à égalité ")
        if joueur == 1 and joueur2 == 2:
            print("joueur 2 gagne")
        if joueur == 1 and joueur2 ==3:
             print("joueur 1 gagne")


        if joueur == 2 and joueur2 == 2:
            print("Egalites")
        if joueur == 2 and joueur2 == 1 :
            print("joueur 1 gagne")
        if joueur ==2 and joueur2 == 3:
            print("joueur2 gagne")

        if joueur == 3 and joueur2 == 3:
            print("vous etes à égalités")
        if joueur == 3 and joueur2 == 1:
            print("joueur 2 gagne")
        if joueur == 3 and joueur == 2:
            print("joueur 1 gagne")



    resultat = resultat + 1

print("\n------------------------------------")
print("Le jeu du: Pierre - Feuille - Ciseaux")
print("------------------------------------\n")

print("------------------------------------")
print("1 -- JOUER AVEC L'ORDINATEUR")
print("2 -- 1 VS 1")
print("------------------------------------\n")

jeu = int(input("choisissez entre 1 OU 2, \n"))

if jeu == 1:
    ordi()

if jeu == 2:
    vs()









