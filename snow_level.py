def start_snowlvl():
#   imports
    import pygame
    import time
    import random
#   initialising
    FPS = 60
    display_width = 1280
    display_height = 720
    clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Snowy mountains')
    move = "="
#   colours
    black = (0,0,0)
    white = (255,255,255)
    red = (255, 0, 0)
    green = (0,255,0)
    blue = (0,0,255)
    grey = (100,100,100)
    gray = (50,50,50)
#   images
    backgroundimg = pygame.image.load('snow_background.jpg')
#   classes
    class IG_O(pygame.sprite.Sprite):
        def __init__(self,x,y,w,h):
            self.x = x
            self.y = y
            self.w = w
            self.h = h

    class cat(IG_O):
        def __init__(self,x,y,w,h,ws,js):
            #for draw()
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            #for move()
            self.walk = 0
            self.ws = ws #walkspeed
            self.running = False
            self.dir = '>' #direction
            #for leap()
            self.js = js #jumpspeed
            self.jump = 0
            self.falling = False

        def draw(self):
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            pygame.draw.rect(gameDisplay, black, self.rect)
        def move(self):
            if self.falling == False:
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    self.walk = -self.ws
                    self.dir = '<'
                    self.running = True
                elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                    self.walk = self.ws
                    self.dir = '>'
                    self.running = True
                else:
                    self.walk = 0
                    self.running = False
            if self.x > 0 and self.x + self.w < display_width:
                if self.x + self.walk > 0 and self.x + self.w + self.walk < display_width:
                    self.x += self.walk
            if self.x > 50:
                move = '<'
            if self.x + self.w < display_width - 50:
                move = '>'
        #Currently does not care what you stand on, just jumps
        def leap(self):
            if self.falling == True and self.jump < self.js:
                self.jump += 1
            elif pygame.key.get_pressed()[pygame.K_SPACE] and self.jump == 0 or pygame.key.get_pressed()[pygame.K_UP] and self.jump == 0:
                    self.jump = -self.js
                    self.falling = True
            else:
                self.jump = 0
                self.falling = False
            self.y += self.jump

    class objects(IG_O):
        def __init__(self,x,y,w,h,img,solid):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.img = img
            self.solid = solid
        def drawimg(self):
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            gameDisplay.blit(self.img, (self.x,self.y))
        def drawclr(self):
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            pygame.draw.rect(gameDisplay, gray, self.rect)

    
    Floor = objects(0,620,display_width,100,0,True)
    Platform1 = objects(700, 500, 350, 50, 0, True)
    Platform2 = objects(1200, 450, 350, 50, 0, True)
    cat = cat(25,Floor.y-100,220,100,12,17)
    background = objects(0,0,1280,720,backgroundimg,False)
    
    def shift(movedir):
        if movedir == ">":
            cat.x -= 10
            Platform1.x -= 10
            Platform2.x -= 10
        if movedir == "<":
            cat.x += 10
            Platform1.x += 10
            Platform2.x += 10
        print(movedir)
    def movedir():
            if cat.x <= 20:
                move = "<"
            elif cat.x + cat.w >= display_width-20:
                move = ">"
            else:
                move = "="
            return move

#   gameloop
    def gameloop():
        game_exit = False
        while game_exit == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
            pygame.event.pump()
        #   Shift the world
            shift(movedir())
        #   Draw things
            #gameDisplay.fill(grey)
            background.drawimg()
        #   Platforms
            Floor.drawclr()
            Platform1.drawclr()
            Platform2.drawclr()
        #   Cat things
            cat.leap()
            cat.move()
            cat.draw()
            pygame.display.update()
            clock.tick(FPS)
    gameloop()
start_snowlvl()
    