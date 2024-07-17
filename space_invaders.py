import pygame

# Initialize the pygame
pygame.init()

# Create the screen
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Space Invanders")

clock = pygame.time.Clock()

# #Game Loop
# while True: 