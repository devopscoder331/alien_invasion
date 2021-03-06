# this is module store class of alien

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        '''init one alien and set position'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load image of alien and get rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # each new alien create left top position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # save position alien
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''alien move right'''
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x

    def check_edges(self):
        '''Return True if aleins in edges'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
