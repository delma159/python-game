import sys
sys.path.append("..")
from src.map import MapPrincess
import unittest

    def test_map_largeur_is_ok(self):
        Map = MapPrincess(0, 0)
        self.assertGreaterEqual(MapPrincess.largeur, 5)
        self.assertLessEqual(MapPrincess.largeur, 10)

    def test_map_longeur_is_ok(self):
        Map = MapPrincess(0, 0)
        self.assertGreaterEqual(MapPrincess.longeur, 5)
        self.assertLessEqual(MapPrincess.longeur, 10)

    def test_move(self):
        Map = MapPrincess(0, 0)
        self.assert
