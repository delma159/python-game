from map import MapPrincess
from map import Controleur
from case_type import CaseType
import random




def init():
    start_game()



def start_game():
    Map = MapPrincess()
    """    
    Map.generate_map()
    """
    game = Controleur(liste_map=Map.generate_map())
    game.deplacement()
    game.affichage_map()


if __name__ == "__main__":
    init()

