# this is module of game function

import sys

import pygame

def check_events(ship):
    '''respond to keypress and mouse event'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # action if key down (move right/left)
        elif event.type == pygame.KEYDOWN:
            # move right
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True\
            # move left
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        # action if key up (move right/left)
        elif event.type == pygame.KEYUP:
            # stop move right
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            # stop move left
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    '''update display and flip to the new screen'''
    screen.fill(ai_settings.bg_collor)
    # draw a ship after screen.fill
    ship.blitme()
    pygame.display.flip()
