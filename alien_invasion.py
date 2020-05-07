# this is game 'Alien Invasion'

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    # init game and create screen
    pygame.init()
    ai_settings = Settings()

    # screen is name 'suraface'
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")

    # create the ship, alien, bullets
    ship = Ship(ai_settings, screen)
#    alien = Alien(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # create fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # run main cycle game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
