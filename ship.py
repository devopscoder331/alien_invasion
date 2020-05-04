# this is module store class of ship

import pygame

class Ship():
    def __init__(self, screen):
        ''' init ship and set it starting position'''
        self.screen = screen
        # load image ship and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # start each ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        ''' draw ship at the current location'''
        self.screen.blit(self.image, self.rect)
