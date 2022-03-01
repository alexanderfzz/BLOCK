import pygame

#start
pygame.init()
running = True
screen = pygame.display.set_mode((1000, 800))

#visual identifications
pygame.display.set_caption("BLOCK")
map = pygame.image.load("map.png")
player = pygame.image.load("player.png")
enemy = pygame.image.load("enemy.png")
bread = pygame.image.load("holy bread.png")
turret = pygame.image.load("turret.png")
bullet = pygame.image.load("bullet.png")
R = pygame.image.load("R key indicator.png")
E = pygame.image.load("E key indicator.png")
pygame.display.set_icon(player)

#player
playerX = 612
playerY = 652
playerMoveX = 0
playerMoveY = 0
playerXt = 0
playeYt = 0
def ShowPlayer(x,y):
    screen.blit(player, (x,y))

#enemy
enemyAlive = False
route = 0
enemySpeedC = 0
enemySpeed = 1

#bread
breadHP = 5
def ShowBread():
    screen.blit(bread,(436,336))

#turret
turretX = 0
turretY = 0
turretAngle = 0
turretPosition = "start"
def ShowTurret(x,y):
    screen.blit(turret, (x, y))

#bullet
bulletX = turretX
bulletY = turretY
bulletMoveX = 2
bulletMoveY = 2
bulletAngle = 0
bulletSpeed = 0
bulletState = "ready"
def ShowBullet(x,y):
    screen.blit(bullet, (x + 26,y + 16))

# r key
rState = False
def ShowR(x,y):
    screen.blit(R, (x + 32,y - 32))

#e key
eState = False
p_u = False
def ShowE(x,y):
    screen.blit(E, (x, y - 32))

#game Over
gameOver = False
tfont = pygame.font.Font("freesansbold.ttf", 68)
font = pygame.font.Font("freesansbold.ttf", 32)
def ShowGameOver():
    gameOverText  = tfont.render("Game Over", True, (30, 150, 30))
    score = font.render(f"score: {enemySpeed - 1}", True, (50, 150, 50))
    screen.blit(gameOverText, (200, 300))
    screen.blit(score, (200, 400))
#in game stats
def ShowScore():
    score = font.render(f"score: {enemySpeed - 1}", True, (0, 0, 0))
    screen.blit(score, (10,10))
def ShowHP():
    hp = font.render(f"HP: {breadHP}", True, (0  ,0 ,0))
    screen.blit(hp, (10, 42))