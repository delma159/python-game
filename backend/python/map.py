import random

class map:


    def __init__(self,largeur, longeur, totalCase, mode):

        self.largeur = largeur
        self.longeur = longeur
        self.totalCase = totalCase
        self.mode = mode


    @property
    def get_largeur(self):
        return self.largeur


    @property
    def get_longeur(self):
        return self.longeur


    @property
    def total_case(self):
        return self.total_case


    @property
    def get_mode(self):
        return self.mode

