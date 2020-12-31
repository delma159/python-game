import pygame
from game import Game

pygame.init()

"""génération de la fenetre"""

pygame.display.set_caption("Princess Rescue")
screen = pygame.display.set_mode((1080, 1080))
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

    game.all_obstacle.draw(screen)


    """verification deplacement"""
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()

    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()


    elif game.pressed.get(pygame.K_UP):
        game.player.move_up()


    """player coordonées"""
    print(game.player.rect.x)
    print(game.player.rect.y)



    """onload fenetre"""
    pygame.display.flip()

    """condition de fin"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fin de jeu")

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False






















































































































































