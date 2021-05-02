import sys
import unittest

sys.path.append("..")
from map import MapPrincess
from map import Controleur
from user import User
from case_type import CaseType
from items import Items
from game import Game


class test(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self.Map = MapPrincess(5, 5)
        self.User = User("adel", 3)
        self.contenue = CaseType(4, 0, 0)
        self.Items = Items()
        self.Controleur = Controleur([])
        self.game = Game()

    def test_case_contenue_is_instance_of_map(self):
        test = MapPrincess(0, 0, 1)
        self.assertIsInstance(test, MapPrincess)

    def test_map_largeur_is_ok(self):
        self.assertGreaterEqual(self.Map.largeur, 5)
        self.assertLessEqual(self.Map.largeur, 10)

    def test_map_longeur_is_ok(self):
        self.assertGreaterEqual(self.Map.longeur, 5)
        self.assertLessEqual(self.Map.longeur, 10)

    def test_user(self):
        self.assertGreater(self.User.point, 0)

    def test_liste_map_vide(self):
        self.assertFalse(self.Map.listeMap)

    def test_totalCase_zero(self):
        self.assertEqual(self.Map.totalCase, 0)

    def test_input_deplacement(self):
        self.assertEqual(self.Controleur.dpc_haut, "z")
        self.assertEqual(self.Controleur.dpc_gauche, "q")
        self.assertEqual(self.Controleur.dpc_droit, "d")
        self.assertEqual(self.Controleur.dpc_bas, "s")

    def test_case_contenue_is_instance_of_caseType(self):
        test = CaseType(self.contenue, 0, 0)
        self.assertIsInstance(test, CaseType)

    def test_items_bonus_malus_point_ok(self):
        self.assertEqual(self.Items.bonus, 0)
        self.assertEqual(self.Items.malus, 0)
        self.assertEqual(self.Items.point, 0)


if __name__ == '__main__':
    unittest.main()
