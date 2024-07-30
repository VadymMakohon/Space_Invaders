import pygame
from laser import Laser

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, offset):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset = offset
        self.image = pygame.image.load("Graphics/spaceship.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=((self.screen_width + self.offset) / 2, self.screen_height - 10))
        self.speed = 16   # Adjust this value to increase/decrease speed
        self.lasers_group = pygame.sprite.Group()
        self.laser_ready = True
        self.laser_time = 0
        self.laser_delay = 300  # milliseconds
        self.laser_sound = pygame.mixer.Sound("Sounds/laser.ogg")

    def get_user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right < self.screen_width + self.offset:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT] and self.rect.left > self.offset:
            self.rect.x -= self.speed
        if keys[pygame.K_SPACE] and self.laser_ready:
            self.shoot_laser()

    def shoot_laser(self):
        self.laser_ready = False
        laser = Laser(self.rect.center, 20, self.screen_height)  # Adjust laser speed here if needed
        self.lasers_group.add(laser)
        self.laser_time = pygame.time.get_ticks()
        self.laser_sound.play()

    def update(self):
        self.get_user_input()
        self.constrain_movement()
        self.lasers_group.update()
        self.recharge_laser()

    def constrain_movement(self):
        if self.rect.right > self.screen_width + self.offset:
            self.rect.right = self.screen_width + self.offset
        if self.rect.left < self.offset:
            self.rect.left = self.offset

    def recharge_laser(self):
        if not self.laser_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_delay:
                self.laser_ready = True

    def reset(self):
        self.rect = self.image.get_rect(midbottom=((self.screen_width + self.offset) / 2, self.screen_height - 10))
        self.lasers_group.empty()