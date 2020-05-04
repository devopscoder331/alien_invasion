# this is game 'Alien Invasion'

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


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
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
