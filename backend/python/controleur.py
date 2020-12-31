import pygame



class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.vie = 1
        self.vitesse = 5
        self.image = pygame.image.load('img/saitama1.png')
        self.princess = pygame.image.load('img/princesse.png')
        self.rect = self.image.get_rect()
        self.rect.x = 425
        self.rect.y = 950


       def move_right(self):
        if not self.game.check_collision(self, self.game.all_obstacle):
            self.rect.x += self.vitesse
            print("tu es mort")


    def move_left(self):
        if not self.game.check_collision(self, self.game.all_obstacle):
            self.rect.x -= self.vitesse
            print("tu es mort")

    def move_up(self):
        if not self.game.check_collision(self, self.game.all_obstacle):
            self.rect.y -= self.vitesse
            print("tu es mort")


    def move_down(self):
        if not self.game.check_collision(self, self.game.all_obstacle):
            self.rect.y += self.vitesse
            print("tu es mort")
