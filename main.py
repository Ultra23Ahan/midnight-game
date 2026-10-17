import pygame

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(title="MidNight")

run = True
while run:
    pygame.time.delay(0)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    pygame.display.update()