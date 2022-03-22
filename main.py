import math
import pygame
import random

LIST = [12,2,6,57,13,78,36,70,10,45,35,2,45,3,22,3,2,4,35,66,23,14,15,30]

HEIGHT=600
WIDTH=900

WHITE = (240,240,240)
LIGHT_GREY = (192,192,192)
MEDIUM_GREY = (128,128,128)
DARK_GREY = (64,64,64)
RED = (255,0,0)
GREEN = (116,161,66)


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
UNIT_HEIGHT = math.ceil(REGION_HEIGHT/MAX_VAL)


def bubble_sort():
    for i in range(len(LIST)):
        for j in range(0, len(LIST) - i - 1):
            if LIST[j] > LIST[j + 1]:
                LIST[j],LIST[j + 1]=LIST[j + 1],LIST[j]
                rectangle({j: RED, j+1:GREEN}, True)
                yield True
    return LIST

def insertionSort():
    for i in range(1, len(LIST)):
        key = LIST[i]
        j = i-1
        while j >=0 and key < LIST[j] :
            LIST[j+1] = LIST[j]
            j -= 1
            rectangle({j: GREEN, j+1:RED}, True)
            yield True
        LIST[j+1] = key
    return LIST

def rectangle(cols={}, clear = False):

    if clear:
        clear_rect = (PADDING_LEFT-10, PADDING_TOP-20, REGION_WIDTH+20, REGION_HEIGHT+25)
        pygame.draw.rect(WIN, WHITE, clear_rect)

    for i,num in enumerate(LIST):
        element_padding_height = PADDING_TOP+(REGION_HEIGHT-(UNIT_HEIGHT*num))
        element_padding_width = PADDING_LEFT+(i*RECTANGLE_WIDTH)
        element_rect = pygame.Rect(element_padding_width, element_padding_height, RECTANGLE_WIDTH, UNIT_HEIGHT*num)
        color = LIST_COLORS[i%3]
        if i in cols:
            color = cols[i]
        pygame.draw.rect(WIN, color, element_rect)
        
    if clear:
        pygame.display.update()

def draw():
    WIN.fill(WHITE)
    rectangle()
    pygame.display.update()

def main():
    run = True
    sorting = False
    sorting_algorithm = None
    clock=pygame.time.Clock()
    
    while run:
        if sorting:
            try:
                next(sorting_algorithm)
            except StopIteration:
                sorting = False
        else:
            draw()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm = insertionSort()

            
    pygame.quit()


if __name__ == "__main__":
    main()       