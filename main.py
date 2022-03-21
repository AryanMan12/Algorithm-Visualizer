import math
import pygame
import random

LIST = [12,2,6,57,13,78,36,78,10,45,35,2,45,3,22,3,2,4,35,66,23,1456]

HEIGHT=600
WIDTH=900

WHITE = (240,240,240)
LIGHT_GREY = (192,192,192)
MEDIUM_GREY = (128,128,128)
DARK_GREY = (64,64,64)

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

LIST_COLORS = (LIGHT_GREY, MEDIUM_GREY, DARK_GREY)

PADDING_TOP = 100
PADDING_BOTTOM = 50
PADDING_LEFT = 50
PADDING_RIGHT = 50

REGION_HEIGHT = 450
REGION_WIDTH = 800
REGION_COLOR = WHITE

NUM_OF_ELEMENTS = len(LIST)
MAX_VAL = max(LIST)
RECTANGLE_WIDTH = math.ceil(REGION_WIDTH/NUM_OF_ELEMENTS)
UNIT_HEIGHT = REGION_HEIGHT//MAX_VAL


def rectangle():
    for i,num in enumerate(LIST):
        element_padding_height = PADDING_TOP+(REGION_HEIGHT-(UNIT_HEIGHT*num))
        element_padding_width = PADDING_LEFT+(i*RECTANGLE_WIDTH)
        element_rect = pygame.Rect(element_padding_width, element_padding_height, RECTANGLE_WIDTH, UNIT_HEIGHT*num)
        pygame.draw.rect(WIN, LIST_COLORS[i%3], element_rect)

def bubble_sort():
    for i in range(len(LIST)):
        for j in range(0, len(LIST) - i - 1):
            if LIST[j] > LIST[j + 1]:
                LIST[j],LIST[j + 1]=LIST[j + 1],LIST[j]

def draw():
    WIN.fill(WHITE)
    rectangle()
    pygame.display.update()

def main():
    run = True
    clock=pygame.time.Clock()
    
    while run:
        draw()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
    pygame.quit()


if __name__ == "__main__":
    main()       