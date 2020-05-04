import sys

import pygame

def run_game():
    # init game and create screen
    pygame.init()
    # scree is name 'suraface'
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)

    # run main cycle game
    while True:
        # track event of keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # display last screen
        screen.fill(bg_color)
        pygame.display.flip()

run_game()
