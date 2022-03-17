import pygame

HEIGHT=600
WIDTH=900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
run = True

while run:
    WIN
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False
            pygame.quit()

        