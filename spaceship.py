import pygame
class Spaceship(pygame.sprite.Sprite):
    def __inint__(self):
        super().__init__()
        self.image = pygame.image.load("Graphics/spaceship.png")
        self.rect = self.omage.get_rect(midbottom = (100, 100))
        