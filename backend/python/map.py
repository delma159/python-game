import random
from case_type import CaseType



class MapPrincess:

    def __init__(self, mode=1):
        self.largeur = 0
        self.longeur = 0
        self.totalCase = 0
        self.mode = mode
        self.listeMap = []

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




    def generate_map(self):

        largeur = int(input("entrez ici la largeur souhaitez pour la map (valeur min=5 et max=10): "))
        longeur = int(input("entrez ici la longeur souhaitez pour la map (valeur min=5 et max=10): "))
        total_case = largeur * longeur
        Case = CaseType()


        cpt = 0
        for e in range(largeur):
            self.listeMap.append([])
            while len(self.listeMap[cpt]) != (longeur-1):
                self.listeMap[cpt].append(Case.contenue_case[1])
            cpt += 1


        self.listeMap[0][1] = Case.contenue_case[4]
        self.listeMap[-1][1] = Case.contenue_case[3]
        compteur=0
        for e in self.listeMap:
            self.listeMap[compteur].append(Case.contenue_case[2])
            random.shuffle(self.listeMap[compteur])
            compteur += 1


        return self.listeMap

Case = CaseType()


class Controleur:

    def __init__(self,liste_map):
        self.dpc_haut = "z"
        self.dpc_bas = "s"
        self.dpc_droit = "d"
        self.dpc_gauche = "q"
        self.map = liste_map

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


    def affichage_map(self):
        compteur = 0
        for e in self.map:
            print(self.map[compteur])
            compteur += 1


    def deplacement(self):
        princess = 0

        while True:
            for i in range(len(self.map[0])):
                if self.map[0][i] == Case.contenue_case[4]:
                    princess = i

            x = 0
            y = 0
            for e in range(len(self.map)):

                for i in range(len(self.map[e])):
                    if self.map[e][i] == Case.contenue_case[3]:
                        x = e
                        y = i

            self.affichage_map()
            msg = input("introduisez votre commande : ")


            if not self.move(msg,x,y):
                break


    def move(self, msg, x, y):
        a = 0
        b = 0

        if msg == "z":
            a = 1
            b = 0

        elif msg == "q":
            a = 0
            b = 1

        elif msg == "s":
            a = 1
            b = 0

        elif msg == "d":
            a = 0
            b = -1

        else:
            print("error try again")

        if self.map[x - a][y - b] == Case.contenue_case[4]:
            print("bravo tu as sauvé la princess! ")
            return False

        elif self.map[x - a][y - b] == Case.contenue_case[2]:
            print("Tu es rentré dans un obstacle tu es mort ! ")
            return False

        else:
            self.map[x - a][y - b] = Case.contenue_case[3]
            self.map[x][y] = Case.contenue_case[1]
            return True


        """while True:
            msg = input("introduisez votre commande : ")
            if msg == "z":
                if self.map[x - 1][y] == Case.contenue_case[4]:
                    print("bravo tu as sauvé la princess! ")
                    return False

                if self.map[x - 1][y] == Case.contenue_case[2]:
                    print("Tu es rentré dans un obstacle tu es mort ! ")
                    return False

                self.map[x - 1][y] = Case.contenue_case[3]
                self.map[x][y] = Case.contenue_case[1]
                x -= 1


    

            if msg == "q":
                if self.map[x][y - 1] == Case.contenue_case[4]:
                    print("bravo ! ")
                    return False
                self.map[x][y - 1] = Case.contenue_case[3]
                self.map[x][y] = Case.contenue_case[1]
                y -= 1



            if msg == "d":
                if self.map[x][y + 1] == Case.contenue_case[4]:
                    print("bravo ! ")
                    return False
                self.map[x][y + 1] = Case.contenue_case[3]
                self.map[x][y] = Case.contenue_case[1]
                y += 1



            if msg == "s":
                self.map[x + 1][y] = Case.contenue_case[3]
                self.map[x][y] = Case.contenue_case[1]
                x += 1"""






