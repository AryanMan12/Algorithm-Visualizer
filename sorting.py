import pygame
import random

class sorter():
    def __init__(self, sorting_algo, val):
        if (type(val) == int): 
            self.LIST = [random.randrange(1, 450, 1) for _ in range(val)]
        else:
            self.LIST = val
        self.tList = self.LIST.copy()
        self.sorting_algo = sorting_algo

        self.HEIGHT=600
        self.WIDTH=900

        self.WHITE = (240,240,240)
        self.LIGHT_GREY = (192,192,192)
        self.MEDIUM_GREY = (128,128,128)
        self.DARK_GREY = (64,64,64)
        self.RED = (255,0,0)
        self.GREEN = (116,161,66)
        self.YELLOW=(255,255,0)


        self.WIN = pygame.display.set_mode((self.WIDTH,self.HEIGHT))

        self.LIST_COLORS = (self.LIGHT_GREY, self.MEDIUM_GREY, self.DARK_GREY)

        self.PADDING_TOP = 100
        self.PADDING_BOTTOM = 50
        self.PADDING_LEFT = 50
        self.PADDING_RIGHT = 50

        self.REGION_HEIGHT = 450
        self.REGION_WIDTH = 800
        self.REGION_COLOR = self.WHITE

        self.NUM_OF_ELEMENTS = len(self.LIST)
        self.MAX_VAL = max(self.LIST)
        self.RECTANGLE_WIDTH = (self.REGION_WIDTH/self.NUM_OF_ELEMENTS)
        self.UNIT_HEIGHT = (self.REGION_HEIGHT/self.MAX_VAL)


    def bubble_sort(self):
        for i in range(len(self.LIST)):
            for j in range(0, len(self.LIST) - i - 1):
                if self.LIST[j] > self.LIST[j + 1]:
                    self.LIST[j],self.LIST[j + 1]=self.LIST[j + 1],self.LIST[j]
                    self.rectangle({j: self.RED, j+1:self.GREEN}, True)
                    yield True
        return self.LIST

    def insertionSort(self):
        for i in range(1, len(self.LIST)):
            key = self.LIST[i]
            j = i-1
            while j >=0 and key < self.LIST[j] :
                self.LIST[j+1] = self.LIST[j]
                j -= 1
                self.rectangle({j: self.GREEN, j+1:self.RED}, True)
                yield True
            self.LIST[j+1] = key
        return self.LIST

    def selectionSort(self):
        for i in range(len(self.LIST)):
            min_= i
            for j in range(i+1, len(self.LIST)):
                if self.LIST[min_] > self.LIST[j]:
                    min_ = j
                self.rectangle({j: self.GREEN, i:self.RED,min_:self.YELLOW}, True)
                yield True
            self.LIST[i], self.LIST[min_] = self.LIST[min_], self.LIST[i]
        return self.LIST

    def merge(self, arr, l, m, r):

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
            pygame.time.delay(20)
            self.rectangle({l+i: self.GREEN, m+j: self.RED}, True)
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            pygame.time.delay(20)
            self.rectangle({l+i: self.GREEN, m+j: self.RED}, True)
            arr[k] = L[i]
            i += 1
            k += 1

    

        while j < n2:
            pygame.time.delay(20)
            self.rectangle({l+i: self.GREEN, m+j: self.RED}, True)
            arr[k] = R[j]
            j += 1
            k += 1

    
    
    def mergeSort(self, arr, l, r):
        if l < r:
            m = l+(r-l)//2
            yield from self.mergeSort(arr, l, m)
            yield from self.mergeSort(arr, m+1, r)
            self.merge(arr, l, m, r)
        yield True

    def partition(self,testlist,start,end):
        pivot=testlist[end]
        i=start-1
        for j in range (start,end):
            pygame.time.delay(20)
            self.rectangle({i: self.GREEN, pivot: self.YELLOW, j: self.RED}, True)
            if testlist[j]<=pivot:
                i=i+1
                testlist[i], testlist[j] = testlist[j], testlist[i]
                pygame.time.delay(20)
                self.rectangle({i: self.GREEN, pivot: self.YELLOW, j: self.RED}, True)     
        testlist[i+1], testlist[end] = testlist[end], testlist[i+1]
        self.rectangle({i: self.GREEN, pivot: self.YELLOW, j: self.RED}, True)
        
        return (i+1)


    def quickSort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.rectangle({pi: self.YELLOW}, True)
            yield from self.quickSort(array, low, pi-1)
            yield from self.quickSort(array, pi+1, high)
        yield True



    def rectangle(self, cols={}, clear = False):
        if clear:
            clear_rect = (self.PADDING_LEFT-10, self.PADDING_TOP-20, self.REGION_WIDTH+20, self.REGION_HEIGHT+25)
            pygame.draw.rect(self.WIN, self.WHITE, clear_rect)
        for i,num in enumerate(self.LIST):
            element_padding_HEIGHT = self.PADDING_TOP+(self.REGION_HEIGHT-(self.UNIT_HEIGHT*num))
            element_padding_width = self.PADDING_LEFT+(i*self.RECTANGLE_WIDTH)
            element_rect = pygame.Rect(element_padding_width, element_padding_HEIGHT, self.RECTANGLE_WIDTH, self.UNIT_HEIGHT*num)
            color = self.LIST_COLORS[i%3]
            if i in cols:
                color = cols[i]
            pygame.draw.rect(self.WIN, color, element_rect)    
        if clear:
            pygame.display.update()

    def draw(self):
        self.WIN.fill(self.WHITE)
        self.rectangle()
        pygame.display.update()

    def main(self):
        self.draw()
        run = True
        if (self.sorting_algo == "Insertion"):
            sorting_algorithm = self.insertionSort()
            sorting = True
        elif (self.sorting_algo == "Bubble"):
            sorting_algorithm = self.bubble_sort()
            sorting = True
        elif (self.sorting_algo == "Selection"):
            sorting_algorithm = self.selectionSort()
            sorting = True
        elif (self.sorting_algo == "Merge"):
            sorting_algorithm = self.mergeSort(arr=self.LIST, l=0, r=self.NUM_OF_ELEMENTS-1)
            sorting = True
        elif (self.sorting_algo == "Quick"):
            sorting_algorithm = self.quickSort(array= self.LIST, low=0, high=self.NUM_OF_ELEMENTS-1)
            sorting = True
        else:
            sorting_algorithm = None
            sorting = False

        clock=pygame.time.Clock()
        while run:
            if sorting:
                try:
                    next(sorting_algorithm)
                except StopIteration:
                    sorting = False
            else:
                self.draw()
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type != pygame.KEYDOWN:
                    continue

                if event.key == pygame.K_b and sorting == False:
                    sorting = True
                    sorting_algorithm = self.bubble_sort()
                if event.key == pygame.K_i and sorting == False:
                    sorting = True
                    sorting_algorithm = self.insertionSort()
                if event.key == pygame.K_s and sorting == False:
                    sorting = True
                    sorting_algorithm = self.selectionSort()
                if event.key == pygame.K_m and sorting == False:
                    sorting = True
                    sorting_algorithm = self.mergeSort(arr=self.LIST, l=0, r=self.NUM_OF_ELEMENTS-1)
                if event.key == pygame.K_q and sorting == False:
                    sorting = True
                    sorting_algorithm = self.quickSort(array= self.LIST, low=0, high=self.NUM_OF_ELEMENTS-1)
                if event.key == pygame.K_SPACE:
                    if (sorting_algorithm == None):
                        sorting_algorithm = self.bubble_sort()
                    sorting = not sorting
                if event.key == pygame.K_r:
                    sorting = False
                    self.LIST = self.tList.copy()
        
        pygame.quit()


