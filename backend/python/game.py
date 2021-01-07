import pygame
from controleur import Player
from obstacle import Obstacle

"""Creation class game pour lancer le jeu
"""

class Game:
    
    """definition du joueur, des obstacle dans un group
    PRE : -
    POST : definiton player, tous les obstacle

    """
    

    def __init__(self):
        self.player = Player()
        self.all_obstacle = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_obstacle()
        
        
    """function spawn_obstacle
    PRE : -
    POST : ajout d obstacle dans le group
    
    """    
    

    def spawn_obstacle(self):
        obstacle = Obstacle()
        self.all_obstacle.add(obstacle)

     """
    function check_collision
    PRE : -
    POST : verification si collision
    """   
        
        
    def check_collision(self, sprite, group):

        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    
    """
    function game over
    POST : - 
    PRE : return quit la fenetre du jeu
    """
    
    def game_over(self):
        return pygame.QUIT
