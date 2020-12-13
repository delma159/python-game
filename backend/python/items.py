from map import MapPrincess, Controleur
from case_type import CaseType


Map = MapPrincess(5, 5)

class Items:

    def __init__(self):
        self.bonus = 0
        self.malus = 0
        self.type = {1: ' + ', 2: ' - '}
        self.point = 0

    @property
    def get_bonus(self):
        return self.bonus

    @property
    def get_malus(self):
        return self.malus

    def generate_items(self):
        liste = Map.listeMap
        case = CaseType()
        Map.generate_map()

        nrb = liste[-3].index(case.contenue_case[1])
        liste[-3][nrb] = self.type[1]


