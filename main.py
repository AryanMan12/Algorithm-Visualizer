import math
import time
import pygame

LIST = [12,2,6,57,13,78,36,70,10,45,35,2,45,3,22,3,2,4,35,66,23,14,15,30]
tList = LIST.copy()

HEIGHT=600
WIDTH=900

WHITE = (240,240,240)
LIGHT_GREY = (192,192,192)
MEDIUM_GREY = (128,128,128)
DARK_GREY = (64,64,64)
RED = (255,0,0)
GREEN = (116,161,66)
BLUE=(25,25,115)


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

def selectionSort():
    for i in range(len(LIST)):
        min_= i
        for j in range(i+1, len(LIST)):
            if LIST[min_] > LIST[j]:
                min_ = j
            rectangle({j: GREEN, i:RED,min_:BLUE}, True)
            yield True
        LIST[i], LIST[min_] = LIST[min_], LIST[i]
    return LIST

def merge(arr, l, m, r):

    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0     
    j = 0     
    k = l     
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    time.sleep(0.09)
 
 
def mergeSort(arr = LIST, l = 0, r = NUM_OF_ELEMENTS-1):
    if l < r:
        m = l+(r-l)//2
        time.sleep(0.09)
        l_arr = {i:GREEN for i in range(m)}
        r_arr = {j+m:RED for j in range(r-m)}
        l_arr.update(r_arr)
        rectangle(l_arr, True)
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    cols ={}
    for j in range(low, high):
        time.sleep(0.05)
        if array[j] <= pivot:
            cols.update({j: RED})
            time.sleep(0.05) 
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
            continue
        cols.update({j:GREEN})
        cols.update({pivot:BLUE})
        rectangle(cols, True)
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i+1
def quickSort(array=LIST, low=0, high=NUM_OF_ELEMENTS-1):
  if low < high:
    pi = partition(array, low, high) 
    quickSort(array, low, pi-1)
    quickSort(array, pi+1, high)
    time.sleep(0.05)


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
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_b and sorting == False:
                sorting = True
                sorting_algorithm = bubble_sort()
            if event.key == pygame.K_i and sorting == False:
                sorting = True
                sorting_algorithm = insertionSort()
            if event.key == pygame.K_s and sorting == False:
                sorting = True
                sorting_algorithm = selectionSort()
            if event.key == pygame.K_m:
                mergeSort()
            if event.key == pygame.K_q:
                quickSort()
            if event.key == pygame.K_SPACE:
                if (sorting_algorithm == None):
                    sorting_algorithm = bubble_sort()
                sorting = not sorting
            if event.key == pygame.K_r:
                LIST = tList  
       
    pygame.quit()
            

if __name__ == "__main__":
    main()       