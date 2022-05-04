import pygame
import random


class treeAlgos:
    def __init__(self):
        pygame.init()
        self.fps = 2
        val = 15
        self.LIST = random.sample(range(1, 100), val)
        
        # self.LIST = [30, 17, 37, 11, 19, 31, 38, 10, 12, 60, 72]
        print(self.LIST)
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

        self.PADDING_TOP = 100
        self.PADDING_BOTTOM = 50
        self.PADDING_LEFT = 50
        self.PADDING_RIGHT = 50

        self.REGION_HEIGHT = 450
        self.REGION_WIDTH = 800
        self.REGION_COLOR = self.WHITE

        self.NUM_OF_ELEMENTS = len(self.LIST)
        self.MAX_VAL = max(self.LIST)
        self.radius = 15
        self.currNode = []
        self.inorderList = []
        self.root = None


    def insertInTree(self, node, index, x_cord, y_cord, radius, treeHeight, prev_node):
        
        if node is None:
            self.currNode.append((x_cord, y_cord))
            return Node(index)
        if index < node.index:
            treeHeight += 1
            prev_node = (x_cord, y_cord)
            x_cord -= (200 - (treeHeight* 35)) 
            y_cord += 35 + (treeHeight* 20)
            
            node.left = self.insertInTree(node.left, index, x_cord, y_cord, radius, treeHeight, prev_node)

        elif index > node.index:
            treeHeight += 1
            prev_node = (x_cord, y_cord)
            x_cord += (200 - (treeHeight* 35))
            y_cord += 35+ (treeHeight* 20)
            
            node.right = self.insertInTree(node.right, index, x_cord, y_cord, radius, treeHeight, prev_node)
            
        pygame.draw.line(self.WIN, self.DARK_GREY,prev_node, (x_cord, y_cord), 2)
        pygame.draw.circle(self.WIN, self.GREEN,(x_cord, y_cord), radius)
        
        pygame.display.update()
        
        return node


    def drawTree(self):
        x_cord = 450
        y_cord = 100
        self.myfont = pygame.font.SysFont("Rockwell", 16)
        pygame.draw.circle(self.WIN, self.GREEN,(x_cord, y_cord), self.radius)
        
        for i, num in enumerate(self.LIST):
            self.root = self.insertInTree(self.root, num, x_cord, y_cord, self.radius, treeHeight= 0, prev_node=(x_cord,y_cord))
            self.index_label = self.myfont.render(str(num), 1, self.DARK_GREY, self.GREEN)
            self.WIN.blit(self.index_label, (self.currNode[i][0]-8,self.currNode[i][1]-8))
            pygame.display.update()
            yield True

        for i, num in enumerate(self.LIST):
            self.index_label = self.myfont.render(str(num), 1, self.DARK_GREY, self.GREEN)
            self.WIN.blit(self.index_label, (self.currNode[i][0]-8,self.currNode[i][1]-8))
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
    
    def inorder(self, root) :
        if root is not None:
            pygame.draw.circle(self.WIN, self.RED,self.currNode[self.LIST.index(root.index)], self.radius)
            self.index_label = self.myfont.render(str(root.index), 1, self.DARK_GREY)
            self.WIN.blit(self.index_label, (self.currNode[self.LIST.index(root.index)][0]-8,self.currNode[self.LIST.index(root.index)][1]-8))
            pygame.time.delay(500)
            pygame.display.update()
            yield from self.inorder(root.left)
            clear_rect = (40, 40, 800, 40)
            pygame.draw.rect(self.WIN, self.WHITE, clear_rect)
            self.inorderList.append(root.index)
            self.inorder_label = self.myfont.render(f"Inoder Traversal: {self.inorderList}", 1, self.DARK_GREY)
            self.WIN.blit(self.inorder_label, (50, 50))
            pygame.draw.circle(self.WIN, self.YELLOW,self.currNode[self.LIST.index(root.index)], self.radius)
            self.index_label = self.myfont.render(str(root.index), 1, self.DARK_GREY)
            self.WIN.blit(self.index_label, (self.currNode[self.LIST.index(root.index)][0]-8,self.currNode[self.LIST.index(root.index)][1]-8))
            pygame.time.delay(500)
            pygame.display.update()
            yield from self.inorder(root.right)

        pygame.display.update()
        yield True

    def preorder(self, root) :
        if root is not None:
            pygame.draw.circle(self.WIN, self.RED,self.currNode[self.LIST.index(root.index)], self.radius)
            self.index_label = self.myfont.render(str(root.index), 1, self.DARK_GREY)
            self.WIN.blit(self.index_label, (self.currNode[self.LIST.index(root.index)][0]-8,self.currNode[self.LIST.index(root.index)][1]-8))
            pygame.time.delay(500)
            pygame.display.update()
            clear_rect = (40, 40, 800, 40)
            pygame.draw.rect(self.WIN, self.WHITE, clear_rect)
            self.inorderList.append(root.index)
            pygame.draw.circle(self.WIN, self.YELLOW,self.currNode[self.LIST.index(root.index)], self.radius)
            self.index_label = self.myfont.render(str(root.index), 1, self.DARK_GREY)
            self.WIN.blit(self.index_label, (self.currNode[self.LIST.index(root.index)][0]-8,self.currNode[self.LIST.index(root.index)][1]-8))
            self.inorder_label = self.myfont.render(f"Preorder Traversal: {self.inorderList}", 1, self.DARK_GREY)
            self.WIN.blit(self.inorder_label, (50, 50))
            pygame.time.delay(500)
            pygame.display.update()
            yield from self.preorder(root.left)
            yield from self.preorder(root.right)

        pygame.display.update()
        
        yield True
    def postorder(self, root) :
        if root is not None:
            pygame.draw.circle(self.WIN, self.RED,self.currNode[self.LIST.index(root.index)], self.radius)
            self.index_label = self.myfont.render(str(root.index), 1, self.DARK_GREY)
            self.WIN.blit(self.index_label, (self.currNode[self.LIST.index(root.index)][0]-8,self.currNode[self.LIST.index(root.index)][1]-8))
            pygame.time.delay(500)
            pygame.display.update()
            yield from self.postorder(root.left)
            yield from self.postorder(root.right)
            clear_rect = (40, 40, 800, 40)
            pygame.draw.rect(self.WIN, self.WHITE, clear_rect)
            self.inorderList.append(root.index)
            self.inorder_label = self.myfont.render(f"Postorder Traversal: {self.inorderList}", 1, self.DARK_GREY)
            self.WIN.blit(self.inorder_label, (50, 50))
            pygame.draw.circle(self.WIN, self.YELLOW,self.currNode[self.LIST.index(root.index)], self.radius)
            self.index_label = self.myfont.render(str(root.index), 1, self.DARK_GREY)
            self.WIN.blit(self.index_label, (self.currNode[self.LIST.index(root.index)][0]-8,self.currNode[self.LIST.index(root.index)][1]-8))
            pygame.time.delay(500)
            pygame.display.update()
        
        pygame.display.update()
        yield True

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
                
                if event.type != pygame.KEYDOWN:
                    continue

                if event.key == pygame.K_i and running == False:
                    running = True
                    treeAlgo = self.inorder(self.root)

                if event.key == pygame.K_p and running == False:
                    running = True
                    treeAlgo = self.preorder(self.root)

                if event.key == pygame.K_o and running == False:
                    running = True
                    treeAlgo = self.postorder(self.root)

                if event.key == pygame.K_r and running == False:
                    running = True
                    self.inorderList = []
                    self.draw()
                    treeAlgo = self.drawTree()


        pygame.quit()

    
    

class Node:
    def __init__(self, index):
        self.index = index
        self.left = None
        self.right = None
