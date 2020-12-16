
class CaseType:


    def __init__(self, type, contenue, x = 0,y = 0):
        self.x = x
        self.y = y
        self.contenue = contenue
        self.contenue = {1: " . ", 2: " / ", 3: " X ", 4: " * "}
        self.type = type
        if self.type == "vide":
            self.case = 1
        if self.type == "mur":
            self.case = 2
        if self.type == "princess":
            self.case = 3
        if self.type == "perso":
            self.case = 4





    @property
    def get_x(self):
        return self.x

    @property
    def get_y(self):
        return self.y

    @property
    def get_type(self):
        return self.type

    @property
    def get_contenue(self):
        return self.contenue



"""  @get_x.setter
    def x(self,x):
        self.x = x
        return x

    @get_y.setter
    def x(self, y):
        self.x = y
        return y
        
"""




"""
class CaseType:


    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
        self.contenue_case = {1: " . ", 2: " / ", 3: " X ", 4: " * "}
        self.type_case = 1



    @property
    def get_x(self):
        return self.x

    @property
    def get_y(self):
        return self.y

    @property
    def get_type_case(self):
        return self.type_case

  @get_x.setter
    def x(self,x):
        self.x = x
        return x

    @get_y.setter
    def x(self, y):
        self.x = y
        return y
        
"""

