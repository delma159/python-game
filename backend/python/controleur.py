import pygame



class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.vie = 1
        self.vitesse = 10
        self.image = pygame.image.load('img/saitama1.png')
        self.princess = pygame.image.load('img/princesse.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 580


    def move_right(self):
        self.rect.x += self.vitesse

    def move_left(self):
        self.rect.x -= self.vitesse

    def move_up(self):
        self.rect.y -= self.vitesse

    def move_down(self):
        self.rect.y += self.vitesse