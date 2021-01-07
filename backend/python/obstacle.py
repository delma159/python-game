import pygame

class Obstacle(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.vitesse = 0
        self.image = pygame.image.load("img/obstacle.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20,800)
        self.rect.y = random.randint(0, 800)
