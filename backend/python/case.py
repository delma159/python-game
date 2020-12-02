

class Case:

    def __init__(self,x,y,contenue_case,type_case):
        self.x = x
        self.y = y
        self.contenue_case = contenue_case
        self.type_case = type_case



    @property
    def get_x(self):
        return self.x

    @property
    def get_y(self):
        return self.y
