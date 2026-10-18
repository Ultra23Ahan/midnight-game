import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(title="MidNight")

player = pygame.image.load("./assets/player/player.svg").convert_alpha()
ground = pygame.image.load("./assets/ground/ground.svg").convert_alpha()
ground = pygame.transform.scale(ground, (800, 200))

gx = 0
gy = 500
px = gx + 20
py = 250 # start pos is above the ground for the drop effect
gravity = 0.35759
xvel = 0
yvel = 0

jump_height = 9
jumping = False
colliding = False
friction = 0.95

clock = pygame.time.Clock()
run = True
while run:

    clock.tick(60)
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False


    screen.fill((0,0,0))

    yvel += gravity
    py += yvel
    px += xvel
    xvel *=friction
    player_rect = pygame.Rect(px, py, 55, 55)
    ground_rect = pygame.Rect(gx, gy, 800, 200)
    if player_rect.colliderect(ground_rect):
        yvel = 0
        gravity = 0
        colliding = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and px > 0:
        xvel = -3
    if keys[pygame.K_RIGHT] and px < (800-55):
        xvel = 3
    if jumping == False and colliding == True:
        if keys[pygame.K_UP]:
            yvel = -3
            jumping = True
        jumping = False

        
    #------------------actual game code--------------
    screen.blit(ground, (gx, gy))
    screen.blit(player, (px, py))
    pygame.display.flip()
    
pygame.quit()