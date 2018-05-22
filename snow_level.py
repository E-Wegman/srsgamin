def start_snowlvl():
#   imports
    import pygame
    import time
    import random
#   initialising
    FPS = 60
    display_width = 1280
    display_height = 800
    clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Snowy mountains')
#   colours
    black = (0,0,0)
    white = (255,255,255)
    red = (255, 0, 0)
    green = (0,255,0)
    blue = (0,0,255)
    grey = (100,100,100)
    gray = (50,50,50)
#   classes
    class cat(pygame.sprite.Sprite):
        def __init__(self,x,y,w,h):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            self.running = False
            self.timer = 0
            self.dir = '>'
        def draw(self):
            pygame.draw.rect(gameDisplay, black, self.rect)
    cat = cat(25,25,220,100)
#   gameloop
    def gameloop():
        game_exit = False
        while game_exit == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
            pygame.event.pump()
            gameDisplay.fill(white)
            cat.draw()
            pygame.display.update()
            clock.tick(FPS)
    gameloop()
start_snowlvl()
    