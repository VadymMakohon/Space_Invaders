import pygame
import random

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        self.type = type

        # Load images for different power-ups
        if self.type == 'double_laser':
            self.image = pygame.image.load('Graphics/double_laser.png').convert_alpha()
        elif self.type == 'shield':
            self.image = pygame.image.load('Graphics/shield.png').convert_alpha()
        elif self.type == 'speed_boost':
            self.image = pygame.image.load('Graphics/speed_boost.png').convert_alpha()

        self.rect = self.image.get_rect(midtop=(x, y))
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.screen_height + self.offset:
            self.kill()