

class Items:

    def __init__(self,bonus,malus):

        self.bonus = bonus
        self.malus = malus


    @property
    def get_bonus(self):
        return self.bonus

    @property
    def get_malus(self):
        return self.malus