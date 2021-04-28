import sys
sys.path.append("..")
from map import MapPrincess
from user import User
import unittest

class test(unittest.TestCase):

    def setUp(self):
        self.Map = MapPrincess(5, 5)
        self.User = User("adel", 3)


    def test_map_largeur_is_ok(self):
        self.assertGreaterEqual(self.Map.largeur, 5)
        self.assertLessEqual(self.Map.largeur, 10)

    def test_map_longeur_is_ok(self):
        self.assertGreaterEqual(self.Map.longeur, 5)
        self.assertLessEqual(self.Map.longeur, 10)
    """
    def test_deplacement(self):
        self.assertTrue(self.)"""

    def test_user(self):
        self.assertGreater(self.User.point, 0)

    def test_liste_map_vide(self):
        self.assertFalse(self.Map.listeMap)




if __name__ == '__main__':
    unittest.main()
