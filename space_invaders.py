import pygame, sys, random
from game import Game

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50

GREY = (29, 29, 27)
YELLOW = (243, 216, 63)
BLACK = (0, 0, 0)

font = pygame.font.Font("Font/monogram.ttf", 40)
level_surface = font.render("LEVEL 01", False, YELLOW)
game_over_surface = font.render("GAME OVER", False, YELLOW)
score_text_surface = font.render("SCORE", False, YELLOW)
highscore_text_surface = font.render("HIGH-SCORE", False, YELLOW)

screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET))
pygame.display.set_caption("Python Space Invaders")

clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

def display_message(message, x, y, color):
    message_surface = font.render(message, False, color)
    screen.blit(message_surface, (x, y))

def show_end_screen():
    screen.fill(GREY)
    display_message("GAME OVER", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100, YELLOW)
    pygame.draw.rect(screen, YELLOW, (200, 400, 150, 50))
    pygame.draw.rect(screen, YELLOW, (400, 400, 150, 50))
    display_message("Play Again", 210, 410, BLACK)
    display_message("Quit", 450, 410, BLACK)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 200 <= mouse_x <= 350 and 400 <= mouse_y <= 450:
                    game.reset()
                    return
                if 400 <= mouse_x <= 550 and 400 <= mouse_y <= 450:
                    pygame.quit()
                    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SHOOT_LASER and game.run:
            game.alien_shoot_laser()
        if event.type == MYSTERYSHIP and game.run:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mystery_ship_group.update()
        game.check_for_collisions()

        # Drawing
        screen.fill(GREY)

        # UI
        pygame.draw.rect(screen, YELLOW, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
        pygame.draw.line(screen, YELLOW, (25, 730), (775, 730), 3)

        if game.run:
            display_message(f"LEVEL {str(game.level).zfill(2)}", 570, 740, YELLOW)
        else:
            screen.blit(game_over_surface, (570, 740, 50, 50))

        x = 50
        for life in range(game.lives):
            screen.blit(game.spaceship_group.sprite.image, (x, 745))
            x += 50

        display_message("SCORE", 50, 15, YELLOW)
        formatted_score = str(game.score).zfill(5)
        display_message(formatted_score, 50, 40, YELLOW)
        display_message("HIGH-SCORE", 550, 15, YELLOW)
        formatted_highscore = str(game.highscore).zfill(5)
        display_message(formatted_highscore, 625, 40, YELLOW)

        game.spaceship_group.draw(screen)
        game.spaceship_group.sprite.lasers_group.draw(screen)
        for obstacle in game.obstacles:
            obstacle.blocks_group.draw(screen)
        game.aliens_group.draw(screen)
        game.alien_lasers_group.draw(screen)
        game.mystery_ship_group.draw(screen)

        pygame.display.update()
        clock.tick(60)
    else:
        show_end_screen()