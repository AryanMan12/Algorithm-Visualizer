import random
import pygame
import math

class GraphAlgos:
    def __init__(self):
        pygame.init()
        self.fps = 2
        
        self.Graph = {"a": {"a": 0, "b": 2, "c": 1, "d": 4, "e": math.inf, "f": math.inf, "g": math.inf},
                    "b": {"a": 2, "b": 0, "c": 2, "d": 4, "e": 3, "f": math.inf, "g": math.inf},
                    "c": {"a": 1, "b": 2, "c": 0, "d": 2, "e": 5, "f": 7, "g": math.inf},
                    "d": {"a": 4, "b": math.inf, "c": 2, "d": 0, "e": math.inf, "f": 4, "g": math.inf},
                    "e": {"a": math.inf, "b": 3, "c": 5, "d": math.inf, "e": 0, "f": math.inf, "g": 1},
                    "f": {"a": math.inf, "b": math.inf, "c": 7, "d": 4, "e": math.inf, "f": 0, "g": 3},
                    "g": {"a": math.inf, "b": math.inf, "c": math.inf, "d": math.inf, "e": 1, "f": 3, "g": 0}}

        self.keyList = list(self.Graph)

        self.HEIGHT=600
        self.WIDTH=900


        self.WHITE = (240,240,240)
        self.LIGHT_GREY = (192,192,192)
        self.MEDIUM_GREY = (128,128,128)
        self.DARK_GREY = (64,64,64)
        self.RED = (255,0,0)
        self.GREEN = (116,161,66)
        self.YELLOW=(255,255,0)
        self.radius = 20


        self.WIN = pygame.display.set_mode((self.WIDTH,self.HEIGHT))

        self.NUM_OF_NODES = len(self.Graph)
        self.NODES_CoOrdinates = []
        self.xSampleSize = 600//(self.NUM_OF_NODES/3)
        self.ySampleSize = 300//(self.NUM_OF_NODES/3)
        while True:
            self.x_cod = [random.randrange(150, 750, self.xSampleSize) for _ in range(self.NUM_OF_NODES)]
            self.y_cod = [random.randrange(150, 450, self.ySampleSize) for _ in range(self.NUM_OF_NODES)]
            self.cods = [(x,y) for x, y in zip(self.x_cod, self.y_cod)]
            if len(self.cods) == len(list(set(self.cods))):
                break

        self.PADDING_TOP = 100
        self.PADDING_BOTTOM = 50
        self.PADDING_LEFT = 50
        self.PADDING_RIGHT = 50

        self.REGION_HEIGHT = 450
        self.REGION_WIDTH = 800
        self.REGION_COLOR = self.WHITE
        

        
    def drawGraph(self):
        self.myfont = pygame.font.SysFont("Rockwell", 16)
        for i in range(self.NUM_OF_NODES):
            pygame.draw.circle(self.WIN, self.GREEN,self.cods[i], self.radius)
            self.index_label = self.myfont.render(str(self.keyList[i]), 1, self.DARK_GREY, self.GREEN)
            self.WIN.blit(self.index_label, (self.cods[i][0]-6,self.cods[i][1]-9))
            pygame.display.update()
            pygame.time.wait(500)
            yield True
        
        for i, node in enumerate(self.Graph):
            for j, n in enumerate(self.Graph[node]):
                if type(self.Graph.get(node).get(n)) == int:
                    pygame.draw.line(self.WIN, self.DARK_GREY,self.cods[i], self.cods[j], 2)
                    pygame.display.update()
                    pygame.time.wait(500)
                yield True

        for i in range(self.NUM_OF_NODES):
            pygame.draw.circle(self.WIN, self.GREEN,self.cods[i], self.radius)
            self.index_label = self.myfont.render(str(self.keyList[i]), 1, self.DARK_GREY, self.GREEN)
            self.WIN.blit(self.index_label, (self.cods[i][0]-6,self.cods[i][1]-9))
            pygame.display.update()
        

    def draw(self):
        self.WIN.fill(self.WHITE)
        self.myfont = pygame.font.SysFont("Rockwell", 20)

        self.fps_add = self.myfont.render(" + ", 1, self.WHITE, self.DARK_GREY)
        self.fps_label = self.myfont.render(f"{self.fps}", 1, self.DARK_GREY)
        self.fps_sub = self.myfont.render("  -  ", 1, self.WHITE, self.DARK_GREY)

        self.WIN.blit(self.fps_add, (800, 560))
        self.WIN.blit(self.fps_label, (750, 560))
        self.WIN.blit(self.fps_sub, (700, 560))
    
        pygame.display.update()

    
    def main(self):
        self.draw()
        run = True
        clock = pygame.time.Clock()
        graphAlgo = self.drawGraph()
        running = True
        while run:
            if running:
                try:
                    next(graphAlgo)
                except StopIteration:
                    running = False
                
            clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                
                if event.type != pygame.KEYDOWN:
                    continue


        pygame.quit()

s = GraphAlgos()

s.main()