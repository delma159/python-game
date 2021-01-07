import pygame



class Player(pygame.sprite.Sprite):
    """Class represantant le joueur et la princess
    """

    def __init__(self):
        super().__init__()
        self.vie = 1
        self.vitesse = 5
        self.image = pygame.image.load('img/saitama1.png')
        self.princess = pygame.image.load('img/princesse.png')
        self.rect = self.image.get_rect()
        self.rect.x = 425
        self.rect.y = 950
        
        if self.vie == 0:
            raise ValueError

        if self.vitesse == 0:
            raise ValueError

        """Creation de function permet le deplacement a droit , verification de collison pour restreindre ces deplacements
        PRE : -
        POST : deplacement vers la droit + verification collision
        """
            

   def move_right(self):
    if not self.game.check_collision(self, self.game.all_obstacle):
        self.rect.x += self.vitesse
        
        
    """Creation de function permet le deplacement a gauche , verification de collison pour restreindre ces deplacements
    PRE : -
    POST : deplacement vers la gauche + verification collision
        """

    def move_left(self):
        if not self.game.check_collision(self, self.game.all_obstacle):
            self.rect.x -= self.vitesse
    
    """Creation de function permet le deplacement en haut , verification de collison pour restreindre ces deplacements
    PRE : -
    POST : deplacement vers le haut + verification collision
        """
    
    def move_up(self):
        if not self.game.check_collision(self, self.game.all_obstacle):
            self.rect.y -= self.vitesse
            
            
    """Creation de function permet le deplacement en bas , verification de collison pour restreindre ces deplacements
    PRE : -
    POST : deplacement vers le bas + verification collision
        """

    def move_down(self):
        if not self.game.check_collision(self, self.game.all_obstacle):
            self.rect.y += self.vitesse

            
            
     """Creation function permetant la gestion des degats et point de vie du joueur
    PRE : @param{degat} : valeur(s) degat subit par le joueur
    POST : difference entre la vie et degat
    """

    def damage(self, degat):
        if self.vie - degat > degat:
            self.vie -= degat

        else:
            self.game.game_over()
