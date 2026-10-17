import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(title="MidNight")

player = pygame.image.load("./assets/player/player.svg").convert_alpha()
ground = pygame.image.load("./assets/ground/ground.svg").convert_alpha()

gx = 0
gy = 500

run = True
while run:
    #-----------init stuff----------
    pygame.time.delay(5) # 60fps
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    #------------------actual game code--------------
    screen.blit(ground, (gx, gy))
    screen.blit(player, (gx, gy))
    pygame.display.update()