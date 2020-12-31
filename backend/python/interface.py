import pygame
from game import Game

pygame.init()

"""génération de la fenetre"""

pygame.display.set_caption("Princess Rescue")
screen = pygame.display.set_mode((1024, 720))
background = pygame.image.load('img/BK.png')

"""chargement du jeu"""

game = Game()

running = True

"""boucle running"""
while running:

    screen.blit(background, (0, 0))

    """chargement personnages"""
    screen.blit(game.player.image, game.player.rect)
    screen.blit(game.player.princess, (0, 0))

    pygame.display.flip()

    """condition de fin"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fin de jeu")

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                game.player.move_right()

            if event.key == pygame.K_LEFT:
                game.player.move_left()

            if event.key == pygame.K_DOWN:
                game.player.move_down()

            if event.key == pygame.K_UP:
                game.player.move_up()























































































































































