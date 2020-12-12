
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

"""  @get_x.setter
    def x(self,x):
        self.x = x
        return x

    @get_y.setter
    def x(self, y):
        self.x = y
        return y
        
"""

