from map import map
from os import system, name

# from time import sleep

map = map(['*', '.', '.', '.', ".", '.', '.', '.', '.', '.'], ['/', '/', '.', '.', ".", '.', '.', '.', '.', '.'],
          ['/', '/', '.', '.', ".", '.', '.', '.', '.', '.'], ['/', '/', '.', '.', ".", '.', '.', '.', '.', '.'],
          ['/', '/', '.', '.', ".", '.', '.', '.', '.', '.'], ['/', '/', '.', '.', ".", '.', '.', '.', '.', '.'],
          ['/', '/', '.', '.', ".", '.', '.', '.', '.', '.'], ['/', '.', '.', '.', ".", '.', '.', '.', '.', '.'],
          ['/', '/', '.', '.', ".", '.', '.', '.', '.', '.'], ['X', '.', '.', '.', ".", '.', '.', '.', '.', '.'], "X",
          "*", "/")


def init():
    map.generateCaseEnd
    map.generatePerso
    map.generateObstacle
    map.generateMap
    check()


# vérifie si le perso est sur la case de fin ou obstacle , plus msg de fin
def check():
    if map.get_perso == map.get_caseEnd:
        print("Vous avez gagné bien joué à vous")
    if map.get_perso == map.get_obstacle:
        print("vous etes mort d'un obstacle")

        msg = input("voullez vous rejouer ? OUI ou NON")
        if msg == "OUI":
            check()
        if msg == "NON":
            return print("Aurevoir")
        else:
            return msg
    else:
        commande()


def clear():
    if name == "nt":
        _ = system('cls')


def victoire():
    print("vous avez gagné bravo !")


def commande():
    print(
        "Vous etes le X et vous devez sauver la princesse '*' " + "\n" + "Attention au obstacle = /" + "\n" + "monter = z",
        "à droit = d", "à gauche = q", " ! VOUS NE POUVEZ PAS DESCNEDRE ! ")
    deplacement = input('entrez votre deplacement :')

    compteur = 0

    for e in map.get_ligne10:
        if e == "X":
            # si usr avance
            if deplacement == "z":
                map.get_ligne10[compteur] == "."
                if map.get_ligne9[compteur] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne9[compteur] = "X"
                    map.get_ligne10[compteur] = "."
                    map.generateMap
                    compteur = 0
                    check()
            # si usr se déplace à gauched
            if deplacement == "q":
                map.get_ligne10[compteur] == "."
                if map.get_ligne10[compteur - 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne10[compteur - 1] = "X"
                    map.get_ligne10[compteur] = "."
                    map.generateMap

            # si usr se déplace à droite
            if deplacement == "d":
                map.get_ligne10[compteur] = "."
                if map.get_ligne10[compteur + 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""

                else:
                    map.get_ligne10[compteur] = "."
                    map.get_ligne10[compteur + 1] = "X"
                    map.generateMap
                    check()
        else:
            compteur += 1

    # on passe a la ligne suivante
    compteur = 0
    for e in map.get_ligne9:
        if e == "X":
            # si usr avance
            if deplacement == "z":
                map.get_ligne9[compteur] == "."
                if map.get_ligne8[compteur] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne8[compteur] = "X"
                    map.get_ligne9[compteur] = "."
                    map.generateMap
                    compteur = 0
                    check()
            # si usr se déplace à gauche
            if deplacement == "q":
                map.get_ligne9[compteur] == "."
                if map.get_ligne9[compteur - 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne9[compteur - 1] = "X"
                    map.get_ligne9[compteur] = "."
                    map.generateMap
                    check()

            # si usr se déplace à droite
            if deplacement == "d":
                map.get_ligne9[compteur] = "."
                if map.get_ligne9[compteur + 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""

                else:
                    map.get_ligne9[compteur + 1] = "."
                    map.get_ligne9[compteur + 1] = "X"
                    map.generateMap
                    check()
        else:
            compteur += 1
    # on passe a la ligne suivante
    compteur = 0
    for e in map.get_ligne8:
        if e == "X":
            # si usr avance
            if deplacement == "z":
                map.get_ligne8[compteur] == "."
                if map.get_ligne7[compteur] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne7[compteur] = "X"
                    map.get_ligne8[compteur] = "."
                    map.generateMap
                    compteur = 0
                    check()
            # si usr se déplace à gauche
            if deplacement == "q":
                map.get_ligne8[compteur] == "."
                if map.get_ligne8[compteur - 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne8[compteur - 1] = "X"
                    map.get_ligne8[compteur] = "."
                    map.generateMap
                    check()

            # si usr se déplace à droite
            if deplacement == "d":
                map.get_ligne8[compteur] = "."
                if map.get_ligne8[compteur + 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""

                else:
                    map.get_ligne8[compteur + 1] = "."
                    map.get_ligne8[compteur + 1] = "X"
                    map.generateMap
                    check()
        else:
            compteur += 1

    # on passe a la ligne suivante
    compteur = 0
    for e in map.get_ligne7:
        if e == "X":
            # si usr avance
            if deplacement == "z":
                map.get_ligne7[compteur] == "."
                if map.get_ligne6[compteur] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne6[compteur] = "X"
                    map.get_ligne7[compteur] = "."
                    map.generateMap
                    compteur = 0
                    check()
            # si usr se déplace à gauche
            if deplacement == "q":
                map.get_ligne7[compteur] == "."
                if map.get_ligne7[compteur - 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne7[compteur - 1] = "X"
                    map.get_ligne7[compteur] = "."
                    map.generateMap
                    check()

            # si usr se déplace à droite
            if deplacement == "d":
                map.get_ligne7[compteur] = "."
                if map.get_ligne7[compteur + 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""

                else:
                    map.get_ligne7[compteur + 1] = "."
                    map.get_ligne7[compteur + 1] = "X"
                    map.generateMap
                    check()
        else:
            compteur += 1

    # on passe a la ligne suivante
    compteur = 0
    for e in map.get_ligne6:
        if e == "X":
            # si usr avance
            if deplacement == "z":
                map.get_ligne6[compteur] == "."
                if map.get_ligne5[compteur] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne5[compteur] = "X"
                    map.get_ligne6[compteur] = "."
                    map.generateMap
                    compteur = 0
                    check()
            # si usr se déplace à gauche
            if deplacement == "q":
                map.get_ligne6[compteur] == "."
                if map.get_ligne6[compteur - 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne6[compteur - 1] = "X"
                    map.get_ligne6[compteur] = "."
                    map.generateMap
                    check()

            # si usr se déplace à droite
            if deplacement == "d":
                map.get_ligne6[compteur] = "."
                if map.get_ligne6[compteur + 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""

                else:
                    map.get_ligne6[compteur + 1] = "."
                    map.get_ligne6[compteur + 1] = "X"
                    map.generateMap
                    check()
        else:
            compteur += 1

    # on passe a la ligne suivante
    compteur = 0
    for e in map.get_ligne5:
        if e == "X":
            # si usr avance
            if deplacement == "z":
                map.get_ligne5[compteur] == "."
                if map.get_ligne4[compteur] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne4[compteur] = "X"
                    map.get_ligne5[compteur] = "."
                    map.generateMap
                    compteur = 0
                    check()
            # si usr se déplace à gauche
            if deplacement == "q":
                map.get_ligne5[compteur] == "."
                if map.get_ligne5[compteur - 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne5[compteur - 1] = "X"
                    map.get_ligne5[compteur] = "."
                    map.generateMap
                    check()

            # si usr se déplace à droite
            if deplacement == "d":
                map.get_ligne5[compteur] = "."
                if map.get_ligne5[compteur + 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""

                else:
                    map.get_ligne5[compteur + 1] = "."
                    map.get_ligne5[compteur + 1] = "X"
                    map.generateMap
                    check()
        else:
            compteur += 1

    # on passe a la ligne suivante
    compteur = 0
    for e in map.get_ligne4:
        if e == "X":
            # si usr avance
            if deplacement == "z":
                map.get_ligne4[compteur] == "."
                if map.get_ligne3[compteur] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne3[compteur] = "X"
                    map.get_ligne4[compteur] = "."
                    map.generateMap
                    compteur = 0
                    check()
            # si usr se déplace à gauche
            if deplacement == "q":
                map.get_ligne4[compteur] == "."
                if map.get_ligne4[compteur - 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne4[compteur - 1] = "X"
                    map.get_ligne4[compteur] = "."
                    map.generateMap
                    check()

            # si usr se déplace à droite
            if deplacement == "d":
                map.get_ligne4[compteur] = "."
                if map.get_ligne4[compteur + 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""

                else:
                    map.get_ligne4[compteur + 1] = "."
                    map.get_ligne4[compteur + 1] = "X"
                    map.generateMap
                    check()
        else:
            compteur += 1

    # on passe a la ligne suivante
    compteur = 0
    for e in map.get_ligne3:
        if e == "X":
            # si usr avance
            if deplacement == "z":
                map.get_ligne3[compteur] == "."
                if map.get_ligne2[compteur] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne2[compteur] = "X"
                    map.get_ligne3[compteur] = "."
                    map.generateMap
                    compteur = 0
                    check()
            # si usr se déplace à gauche
            if deplacement == "q":
                map.get_ligne3[compteur] == "."
                if map.get_ligne3[compteur - 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne3[compteur - 1] = "X"
                    map.get_ligne3[compteur] = "."
                    map.generateMap
                    check()

            # si usr se déplace à droite
            if deplacement == "d":
                map.get_ligne3[compteur] = "."
                if map.get_ligne3[compteur + 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""

                else:
                    map.get_ligne3[compteur + 1] = "."
                    map.get_ligne3[compteur + 1] = "X"
                    map.generateMap
                    check()
        else:
            compteur += 1

    # on passe a la ligne suivante
    compteur = 0
    for e in map.get_ligne2:
        if e == "X":
            # si usr avance
            if deplacement == "z":
                map.get_ligne2[compteur] == "."
                if map.get_ligne1[compteur] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                elif map.get_ligne1[compteur] == "*":
                    victoire()
                else:
                    map.get_ligne1[compteur] = "X"
                    map.get_ligne2[compteur] = "."
                    map.generateMap
                    compteur = 0
                    check()
            # si usr se déplace à gauche
            if deplacement == "q":
                map.get_ligne2[compteur] == "."
                if map.get_ligne2[compteur - 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                else:
                    map.get_ligne2[compteur - 1] = "X"
                    map.get_ligne2[compteur] = "."
                    map.generateMap
                    check()

            # si usr se déplace à droite
            if deplacement == "d":
                map.get_ligne2[compteur] = "."
                if map.get_ligne2[compteur + 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""

                else:
                    map.get_ligne2[compteur + 1] = "."
                    map.get_ligne2[compteur + 1] = "X"
                    map.generateMap
                    check()
        else:
            compteur += 1

    # on passe a la ligne suivante
    compteur = 0
    for e in map.get_ligne1:
        if e == "X":
            # si usr avance
            if deplacement == "z":
                print("il y a rien devant toi ;-)")
                check()
            # si usr se déplace à gauche
            if deplacement == "q":
                map.get_ligne1[compteur] == "."
                if map.get_ligne1[compteur - 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                elif map.get_ligne1[compteur - 1] == "*":
                    victoire()
                else:
                    map.get_ligne1[compteur - 1] = "X"
                    map.get_ligne1[compteur] = "."
                    map.generateMap
                    check()

            # si usr se déplace à droite
            if deplacement == "d":
                map.get_ligne1[compteur] = "."
                if map.get_ligne1[compteur + 1] == "/":
                    print("vous etes mort car vous avez touché un obstacle")
                    return ""
                elif map.get_ligne1[compteur + 1] == "*":
                    victoire()
                else:
                    map.get_ligne1[compteur + 1] = "X"
                    map.get_ligne1[compteur] = "."
                    map.generateMapd
                    check()
        if e == "*":
            print("bravo tu as sauvé la princesse")
            check()
        else:
            compteur += 1


if __name__ == "__main__" :
    init()