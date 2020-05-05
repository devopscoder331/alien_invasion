# this is module of game function

import sys

import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # move right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # move left
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # press space
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
    # stop move right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    # stop move left
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    '''respond to keypress and mouse event'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # action if key down (move right/left)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # action if key up (move right/left)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    '''update display and flip to the new screen'''
    screen.fill(ai_settings.bg_collor)
    # bullet
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # draw a ship after screen.fill
    ship.blitme()
    pygame.display.flip()
