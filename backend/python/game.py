import pygame
from controleur import Player

class Game:

    def __init__(self):
        self.player = Player()
        self.all_obstacle = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_obstacle()

    def spawn_obstacle(self):
        obstacle = Obstacle()
        self.all_obstacle.add(obstacle)

    def check_collision(self, sprite, group):

        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
