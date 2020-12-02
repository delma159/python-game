


class type:


    def __init__(self,case_dispo,obstacle,perso,princess):

        self.case_dispo = case_dispo
        self.obstacle = obstacle
        self.perso = perso
        self.princess = princess


    @property
    def get_case_dispo(self):
        return self.case_dispo


    @property
    def get_obstacle(self):
        return self.obstacle


    @property
    def total_perso(self):
        return self.perso


    @property
    def get_princess(self):
        return self.princess
