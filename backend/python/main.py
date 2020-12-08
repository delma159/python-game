from map import map
from backend.python.case_type import case_type
from controleur import controleur
import random


# from time import sleep


def init():
    start_game()


# class map
largeur = int(input("entrez ici la largeur souhaitez pour la map (valeur min=5 et max=10): "))
longeur = int(input("entrez ici la longeur souhaitez pour la map (valeur min=5 et max=10): "))
total_case = largeur * longeur

# class case_type
x = 0
y = 0
contenue_case = {1: " . ", 2: " / ", 3: " X ", 4: " * "}

map = map(largeur, longeur, total_case, {1: 'normal'})
case = case_type(x, y, contenue_case, type_case=0)

# class controleur

haut = "z"
bas = "s"
droite = "d"
gauche = "q"
deplacement = controleur(haut, bas, droite, gauche)


def start_game():
    liste_ligne1 = []
    liste_ligne2 = []
    liste_ligne3 = []
    liste_ligne4 = []
    liste_ligne5 = []
    liste_ligne6 = []
    liste_ligne7 = []
    liste_ligne8 = []
    liste_ligne9 = []
    liste_ligne10 = []

    liste_map = [liste_ligne1, liste_ligne2, liste_ligne3, liste_ligne4, liste_ligne5, liste_ligne6, liste_ligne7,
                 liste_ligne8, liste_ligne9, liste_ligne10]

    for e in range(longeur):
        liste_map[e].append(contenue_case[1])

    for i in range(largeur):
        liste_map[i] *= largeur

    supr = True
    while supr:
        try:
            liste_map.remove([])
            supr = True

        except ValueError:
            supr = False

    liste_map[0][1] = contenue_case[4]
    liste_map[-1][1] = contenue_case[3]

    cpt = 0
    for e in liste_map:
        liste_map[cpt][0] = contenue_case[2]
        random.shuffle(liste_map[cpt])
        print(liste_map[cpt])
        cpt += 1



    x = -1
    y = 0
    for e in liste_map:
        x += 1
    for e in liste_map[x]:
        if liste_map[x][y] == contenue_case[3]:
            msg = input("introduisez votre commande : ")
            if msg == "z":
                liste_map[x - 1][y] = contenue_case[3]
                liste_map[x][y] = contenue_case[1]
                cpt = 0
                for e in liste_map:
                    print(liste_map[cpt])
                    cpt += 1
            if msg == "q":
                liste_map[x + 1 ][y] = contenue_case[3]
                liste_map[x][y] = contenue_case[1]


        y += 1









if __name__ == "__main__":
    init()
#dodie est un chien de la casse