import pygame

# Initialize the pygame
pygame.init()

# Create the screen
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



# Background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

# Title and Icon
pygame.display.set_caption("Space Invaders")
try:
    icon = pygame.image.load('ufo.png')
except FileNotFoundError:
    icon = pygame.Surface((32, 32))
    icon.fill((255, 0, 0))
pygame.display.set_icon(icon)

# Player
try:
    playerImg = pygame.image.load('player.png')
except FileNotFoundError:
    playerImg = pygame.Surface((50, 50))
    playerImg.fill((0, 255, 0))
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
try:
    enemyImg = pygame.image.load('enemy.png')
except FileNotFoundError:
    enemyImg = pygame.Surface((50, 50))
    enemyImg.fill((255, 0, 0))
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

# Bullet
try:
    bulletImg = pygame.image.load('bullet.png')
except FileNotFoundError:
    bulletImg = pygame.Surface((5, 20))
    bulletImg.fill((255, 255, 255))
bulletX = 0
bulletY = 480
bulletY_change = 0.5
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))  # RGB - Black background
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Checking keystroke is pressed or not
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player movement
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = is_collision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score_value += 1
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_score(textX, textY)
    pygame.display.update()