from map import MapPrincess, Controleur
from items import Items


def init():
    start_game()



def start_game():

    Map = MapPrincess(0,0)
    item = Items()
    game = Controleur(liste_map=Map.generate_map())

    item.generate_items()
    game.deplacement()
    game.affichage_map()


if __name__ == "__main__":
    init()
