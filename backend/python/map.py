import random


class map:

    def __init__(self,ligne1,ligne2,ligne3,ligne4,ligne5,ligne6,ligne7,ligne8,ligne9,ligne10,perso,caseEnd,obstacle):
        self.ligne1 = ligne1
        self.ligne2 = ligne2
        self.ligne3 = ligne3
        self.ligne4 = ligne4
        self.ligne5 = ligne5
        self.ligne6 = ligne6
        self.ligne7 = ligne7
        self.ligne8 = ligne8
        self.ligne9 = ligne9
        self.ligne10 = ligne10
        self.perso = perso
        self.caseEnd = caseEnd
        self.obstacle = obstacle

    @property
    def get_perso(self):
        return self.perso

    @property
    def get_caseEnd(self):
        return self.caseEnd

    @property
    def get_obstacle(self):
        return self.obstacle
    @property
    def generateCaseEnd(self):
        """
        num = random.random() * 10
        self.ligne1 = self.ligne1.append(self.ligne1[round(num)], "*")
        """
        random.shuffle(self.ligne1)


    @property
    def generatePerso(self):
        """
        num = random.random() * 10
        self.ligne10 = self.ligne10.replace(self.ligne10[round(num)], "X")
        """
        random.shuffle(self.ligne10)

    @property
    def generateObstacle(self):

        """
        obstacle = '/'
        num = random.random() * 10
        self.ligne2 = self.ligne2.replace(self.ligne2[round(num)], obstacle)
        num = random.random() * 10
        self.ligne3 = self.ligne3.replace(self.ligne3[round(num)], obstacle)
        num = random.random() * 10
        self.ligne4 = self.ligne4.replace(self.ligne4[round(num)], obstacle)
        num = random.random() * 10
        self.ligne5 = self.ligne5.replace(self.ligne5[round(num)], obstacle)
        num = random.random() * 10
        self.ligne6 = self.ligne6.replace(self.ligne6[round(num)], obstacle)
        num = random.random() * 10
        self.ligne7 = self.ligne7.replace(self.ligne7[round(num)], obstacle)
        num = random.random() * 10
        self.ligne8 = self.ligne8.replace(self.ligne8[round(num)], obstacle)
        num = random.random() * 10
        self.ligne9 = self.ligne9.replace(self.ligne9[round(num)], obstacle)
        """

        random.shuffle(self.ligne2)
        random.shuffle(self.ligne3)
        random.shuffle(self.ligne4)
        random.shuffle(self.ligne5)
        random.shuffle(self.ligne6)
        random.shuffle(self.ligne7)
        random.shuffle(self.ligne8)
        random.shuffle(self.ligne9)


    @property
    def generateMap(self):

        map = ' '.join(self.ligne1) + "\n" + ' '.join(self.ligne2) + "\n" + ' '.join(self.ligne3) + "\n" + ' '.join(
        self.ligne4) + "\n" + ' '.join(self.ligne5) + "\n" + ' '.join(self.ligne6) + "\n" + ' '.join(
        self.ligne7) + "\n" + ' '.join(
        self.ligne8) + "\n" + ' '.join(self.ligne9) + "\n" + ' '.join(self.ligne10)
        return print(map)

    @property
    def get_ligne1(self):
        return self.ligne1

    @property
    def get_ligne2(self):
        return self.ligne2

    @property
    def get_ligne3(self):
        return self.ligne3

    @property
    def get_ligne4(self):
        return self.ligne4

    @property
    def get_ligne5(self):
        return self.ligne5

    @property
    def get_ligne6(self):
        return self.ligne6

    @property
    def get_ligne7(self):
        return self.ligne7

    @property
    def get_ligne8(self):
        return self.ligne8

    @property
    def get_ligne9(self):
        return self.ligne9

    @property
    def get_ligne10(self):
        return self.ligne10