import pygame

HEIGHT=600
WIDTH=900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))


# Aaya kya ❤️de
#Emoji kaise use biya J2

def main():
    run = True
    clock=pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
    pygame.quit()
                

if __name__ == "__main__":
    main()       