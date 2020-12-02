from map import map
import map
import case
import items


# from time import sleep
largeur = int(input("entrez ici la largeur souhaitez pour la map (valeur min=5 et max=10): "))
longeur = int(input("entrez ici la longeur souhaitez pour la map (valeur min=5 et max=10): "))
total_case = largeur * longeur

map = map(largeur, longeur, total_case, { 1 : "solo"})



def start_game():

    boucle_infini = 1

    while boucle_infini == 0:

        if map.get_perso == map.get_princess:
            return boucle_infini +1


def generate_map():
    nbr=0
    while nbr == longeur:
        pass


def init():
    generate_map()
    start_game




if __name__ == "__main__" :
    init()
