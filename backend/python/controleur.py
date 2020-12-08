
class controleur:

    def __init__(self,dpc_haut,dpc_bas,dpc_droit,dpc_gauche):
        self.dpc_haut = dpc_haut
        self.dpc_bas = dpc_bas
        self.dpc_droit = dpc_droit
        self.dpc_gauche = dpc_gauche


    @property
    def get_dpc_haut(self):
        return self.dpc_haut


    @property
    def get_dpc_bas(self):
        return self.dpc_bas


    @property
    def total_dpc_droit(self):
        return self.dpc_droit


    @property
    def get_dpc_gauche(self):
        return self.dpc_gauche