# this is module of game function

import sys

import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # move right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # move left
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # press space
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

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

def update_screen(ai_settings, screen, ship, aliens, bullets):
    '''update display and flip to the new screen'''
    screen.fill(ai_settings.bg_collor)
    # bullet
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # draw a ship after screen.fill
    ship.blitme()
    # alien.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    '''update bullets pisition and delete old bullets'''
    # update position bulleets
    bullets.update()

    # delete old bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

def update_aliens(aliens):
    '''update position all alins in fleet'''
    aliens.update()

def get_number_aliens_x(ai_settings, alien_width):
    # find number aliens in a row
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_heigt - (3 * alien_height) - ship_height)
    number_rows  = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    '''create fleet of aliens'''
    #create an alien and find number aliens in a row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    #create first a row
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
