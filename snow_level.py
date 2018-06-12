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
    class cat(pygame.sprite.Sprite):
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
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

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
            for platform in Platforms:
                if platform.y <= self.y + self.h <= platform.y + platform.h and platform.x <= self.x <= platform.x + platform.w:
                    print("You landed at:", self.x, self.y)
                    self.jump = 0
                elif pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP]:
                    print("You jumped at:", self.x, self.y)
                    self.jump -= self.js
                    self.falling = True
                else:
                    self.jump += 1 #1
                    print("You are falling at:", self.x, self.y)
                self.y += self.jump

    class objects(pygame.sprite.Sprite):
        def __init__(self,x,y,w,h,clr,img,solid):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.clr = clr
            self.img = img
            self.solid = solid
        def drawimg(self):
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            gameDisplay.blit(self.img, (self.x,self.y))
        def drawclr(self):
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            pygame.draw.rect(gameDisplay, self.clr, self.rect)

    Floor = objects(0, display_height-100, display_width, 100, gray, 0, True)
    Platform1 = objects(700, 500, 350, 50, gray, 0, True)
    Platform2 = objects(1200, 450, 350, 50, gray, 0, True)
    cat = cat(25, Floor.y-100, 220, 100, 10, 20) 
    background = objects(0, 0, display_width, display_height, grey, backgroundimg, False)
    
    Platforms = [Floor, Platform1, Platform2]

    def shift(movedir):
        if movedir == ">":
            cat.x -= 10
            Platform1.x -= 10
            Platform2.x -= 10
        if movedir == "<":
            cat.x += 10
            Platform1.x += 10
            Platform2.x += 10
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
            background.drawclr()
            cat.draw()
        #   Platforms
            Floor.drawclr()
            Platform1.drawclr()
            Platform2.drawclr()
        #   Cat things
            cat.leap()
            cat.move()
            pygame.display.update()
            clock.tick(FPS)
    gameloop()
start_snowlvl()
    