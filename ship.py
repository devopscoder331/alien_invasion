# this is module store class of ship

import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        ''' init ship and set it starting position'''
        self.screen = screen
        self.ai_settings = ai_settings
        # load image ship and get its rect
        self.image = pygame.image.load('images/ship_new.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # start each ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # store center of value horizontal position
        self.center = float(self.rect.centerx)
        # flag of move
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
    def blitme(self):
        ''' draw ship at the current location'''
        self.screen.blit(self.image, self.rect)
