import pygame, sys

# Initialize the pygame
pygame.init()

# Create the screen
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700

GREY = (29, 29, 27)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Space Invanders")

clock = pygame.time.Clock()

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Drawing
    screen.fill(GREY)

    pygame.display.update()
    clock.tick(60)