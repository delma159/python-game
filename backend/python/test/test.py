import sys
sys.path.append("..")
from src.map import MapPrincess
import unittest

class test(unittest.Testcase):
    def setUp(self):
        self.Map = MapPrincess(0, 0)
    def test_map_largeur_is_ok(self):
        
        self.assertGreaterEqual(MapPrincess.largeur, 5)
        self.assertLessEqual(MapPrincess.largeur, 10)

    def test_map_longeur_is_ok(self):
        self.assertGreaterEqual(MapPrincess.longeur, 5)
        self.assertLessEqual(MapPrincess.longeur, 10)

    def test_move(self):
        Map = MapPrincess(0, 0)
        self.assert

if __name__ == '__main__':
    unittest.main()
