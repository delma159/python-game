

class User:

    def __init__(self,user,point):

        self.user = user
        self.point = point


    @property
    def get_user(self):
        return self.user

    @property
    def get_point(self):
        return self.point