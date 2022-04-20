import pygame
import random


class treeAlgos:
    def __init__(self):
        pygame.init()
        self.fps = 10
        val = 50
        self.LIST = [random.randrange(1, 99, 1) for _ in range(val)]

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


    def insertInTree(self,node,  index, x_cord, y_cord, radius):
        
        if node is None:
            return Node(index)
        if index < node.index:
            x_cord -= 50
            y_cord += 50
            node.left = self.insertInTree(node.left, index, x_cord, y_cord, radius)

        elif index > node.index:
            x_cord += 50
            y_cord += 50
            node.right = self.insertInTree(node.right, index, x_cord, y_cord, radius)

        else:
            print("Already Exsisting Node", node.index)
        pygame.draw.circle(self.WIN, self.GREEN,(x_cord, y_cord), radius)
        pygame.display.update()
        
        return node


    def drawTree(self):
        root = None
        x_cord = 450
        y_cord = 100
        radius = 15
        pygame.draw.circle(self.WIN, self.GREEN,(x_cord, y_cord), radius)
        for num in self.LIST:
            root = self.insertInTree(root, num, x_cord, y_cord, radius)
            yield True


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
        treeAlgo = self.drawTree()
        running = True
        while run:
            if running:
                try:
                    next(treeAlgo)
                except StopIteration:
                    running = False
                
            clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
        pygame.quit()

class Node:
    def __init__(self, index):
        self.index = index
        self.left = None
        self.right = None

s = treeAlgos()

s.main()