import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed, screen_height, is_ai=False):
        super().__init__()
        self.image = pygame.Surface((4, 15))
        self.image.fill((243, 216, 63))
        self.rect = self.image.get_rect(center=position)
        self.speed = speed
        self.screen_height = screen_height
        self.is_ai = is_ai  # New attribute to determine if the laser is from AI

    def update(self):
        if self.is_ai:
            self.rect.y += self.speed  # AI lasers move downwards
        else:
            self.rect.y -= self.speed  # Player lasers move upwards

        # Remove laser if it goes off screen
        if self.rect.y > self.screen_height + 15 or self.rect.y < -15:
            self.kill()