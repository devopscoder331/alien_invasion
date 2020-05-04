# this is module of game function

import sys

import pygame

def check_events():
    '''respond to keypress and mouse event'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    '''update display and flip to the new screen'''
    screen.fill(ai_settings.bg_collor)
    # draw a ship after screen.fill
    ship.blitme()
    pygame.display.flip()
