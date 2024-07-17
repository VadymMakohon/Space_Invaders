import pygame
class Spaceship(pygame.sprite.Sprite):
    def __inint__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("Graphics/spaceship.png")
        self.rect = self.omage.get_rect(midbottom = (self.screen_width/2, self.screen_height))
