import pygame

WIN = pygame.display.set_mode((300, 300))
run = True

while run:
    WIN
    for event in pygame.event.Event:
        if event == pygame.QUIT:
            run = False
            quit()
    