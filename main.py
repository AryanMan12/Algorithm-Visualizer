import pygame

HEIGHT=600
WIDTH=900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

REGION_HEIGHT = 450
REGION_WIDTH = 800
REGION_COLOR = (255, 255, 255)

LIST = [12,2,6,57,13,78,36,78,10]

def rectangle():
    pass

def draw():
    region = pygame.Rect(50, 100, REGION_WIDTH, REGION_HEIGHT)
    pygame.draw.rect(WIN, REGION_COLOR, region)
    pygame.display.update()

def main():
    run = True
    clock=pygame.time.Clock()

    draw()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
    pygame.quit()


if __name__ == "__main__":
    main()       