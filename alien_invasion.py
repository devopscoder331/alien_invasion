# this is game 'Alien Invasion'

import pygame
from pygame.sprite import Group

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
    ship = Ship(ai_settings, screen)
    #create bullets Group
    bullets = Group()
    # run main cycle game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
