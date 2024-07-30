import pygame
import random
from laser import Laser

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, offset, is_ai=False, laser_group=None):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset = offset
        self.is_ai = is_ai
        self.lasers_group = laser_group if laser_group else pygame.sprite.Group()
        self.image = pygame.image.load("Graphics/spaceship.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=((self.screen_width + self.offset) / 2, self.screen_height - 10))
        self.speed = 16  # Adjust this value to increase/decrease speed
        self.laser_ready = True
        self.laser_time = 0
        self.laser_delay = 300  # milliseconds
        self.laser_sound = pygame.mixer.Sound("Sounds/laser.ogg")
        self.ai_timer = pygame.time.get_ticks()

    def get_user_input(self):
        if self.is_ai:
            self.ai_behavior()
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and self.rect.right < self.screen_width + self.offset:
                self.rect.x += self.speed
            if keys[pygame.K_LEFT] and self.rect.left > self.offset:
                self.rect.x -= self.speed
            if keys[pygame.K_SPACE] and self.laser_ready:
                self.shoot_laser()

    def ai_behavior(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.ai_timer > 300:  # Adjust this value for faster or slower shooting
            self.ai_timer = current_time
            move_choice = random.choice(['left', 'right', 'shoot'])
            if move_choice == 'left' and self.rect.left > self.offset:
                self.rect.x -= self.speed
            elif move_choice == 'right' and self.rect.right < self.screen_width + self.offset:
                self.rect.x += self.speed
            elif move_choice == 'shoot' and self.laser_ready:
                self.shoot_laser()

    def shoot_laser(self):
        self.laser_ready = False
        laser = Laser(self.rect.center, 20, self.screen_height)  # Adjust laser speed here if needed
        self.lasers_group.add(laser)
        self.laser_time = pygame.time.get_ticks()
        self.laser_sound.play()

    def update(self):
        self.get_user_input()
        if self.is_ai:
            self.avoid_lasers()  # AI collision avoidance
        self.constrain_movement()
        self.lasers_group.update()
        self.recharge_laser()

    def avoid_lasers(self):
        # AI strategy to avoid lasers
        for laser in pygame.sprite.spritecollide(self, self.lasers_group, False):
            if laser.rect.y > self.rect.top:  # Laser is approaching
                # Move away from the laser's horizontal direction
                if laser.rect.centerx < self.rect.centerx and self.rect.left > self.offset:
                    self.rect.x -= self.speed  # Move left
                elif laser.rect.centerx > self.rect.centerx and self.rect.right < self.screen_width + self.offset:
                    self.rect.x += self.speed  # Move right

                # Constrain movement to screen bounds
                self.constrain_movement()
                break  # Avoid multiple adjustments if lasers are close

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
