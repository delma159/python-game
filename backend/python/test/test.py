import sys
sys.path.append("..")
from src.map import MapPrincess
from user import User
import unittest

class test(unittest.Testcase):
    def setUp(self):
        self.Map = MapPrincess(0, 0)

    def test_map_largeur_is_ok(self):
        self.assertGreaterEqual(self.MapPrincess.largeur, 5)
        self.assertLessEqual(self.MapPrincess.largeur, 10)

    def test_map_longeur_is_ok(self):
        self.assertGreaterEqual(self.MapPrincess.longeur, 5)
        self.assertLessEqual(self.MapPrincess.longeur, 10)

    def test_deplacement(self):
        self.assertTrue(self.deplacement)

    def test_user(self):
        self.assertGreater(self.User.point, 0)

    def test_liste_map_vide(self):
        listeMap = []
        self.assertFalse(self.MapPrincess.listeMap)

if __name__ == '__main__':
    
