import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    # init game and create screen
    pygame.init()
    ai_settings = Settings()
    # screen is name 'suraface'
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")
    # create the ship
    ship = Ship(screen)
    # run main cycle game
    while True:
        # track event of keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # draw display last screen
        screen.fill(ai_settings.bg_collor)
        # draw a ship after screen.fill
        ship.blitme()
        pygame.display.flip()

run_game()
