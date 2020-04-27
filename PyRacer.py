'''
@author Ray Johnson
PyRacer is a Python game where you avoid other cars.
Racing isn't part of the game. Sorry about that.
'''

import pygame, time, random, pickle
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)

# define window details
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('PyRacer')


# define colors
#teal_green = (0,144,144)
black = (0,0,0)
white = (255,255,255)
bright_red = (255,0,0)
red =(139,0,0)
green = (34,139,34)
bright_green = (0, 255, 0)
other_green=(0,255,128)
bright_green = (102,255,0)
blue = (0,0,255)
#turqoise = (0,255,239)
iceberg = (97, 181, 203)
sapGreen = (71,118,30)
jasmine = (254,217,133)
darkSeaGreen = (147, 181, 146)
dark_iceberg =(64,135,194)

pause = False

# impose time on game
clock = pygame.time.Clock()
carImg = pygame.image.load('racecarSm.png')
otherCarImg = pygame.image.load('otherCarSm.png')
carCrashImg = pygame.image.load('racecarSmCrashed2.png')
carIcon = pygame.image.load('racecarIcon.png')
pygame.display.set_icon(carIcon)
pygame.mixer.music.load('engine.wav')
bg = pygame.image.load('road.png').convert()

crash_sound = pygame.mixer.Sound(file='crash.wav')
otherCarCount = 0

# define width of car
(car_width, car_height) = carImg.get_rect().size
(otherCar_width, otherCar_height) = otherCarImg.get_rect().size

def button(msg, x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+ h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h) )
        if click[0] ==1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
    
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf,textRect = text_objects(msg, smallText)
    textRect.center = ( (x + (w/2)), y + (h/2))
    gameDisplay.blit(textSurf, textRect)

    
def get_high_score():
    try:
        with open('score.dat','rb') as file:
            score = pickle.load(file)
    except:
        score = 0
    return score

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render('Dodged: ' + str(count), True, black)
    gameDisplay.blit(text, (0,0))
    
def display_highest_score(score):
    font = pygame.font.SysFont(None,25)
    text = 'HighScore! ' + str(score)
    
    textviz = font.render(text, True, dark_iceberg)
    gameDisplay.blit(textviz,(display_width-len(text)*9,0))
    
#def things(thingx, thingy, thingw,thingh, color):
#    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    
def car(x, y):
    gameDisplay.blit(carImg, (x,y))
    
def otherCar(x,y):
    gameDisplay.blit(otherCarImg, (x,y))

def quit_game():
    pygame.quit()
    quit()
    
def car_crashed(x,y):
    gameDisplay.blit(carCrashImg, (x,y))
    
def text_objects(text, font,color=black):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
#245,415,100,50
    
def pause_game():
    pygame.mixer.music.pause()
    largeText = pygame.font.SysFont("comicsansms",110)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        #gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("Continue",245,415,100,50,green,bright_green,unpause_game)
        button("Quit",455,415,100,50,red,bright_red,quit_game)
        pygame.display.update()
        clock.tick(15)

def unpause_game():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',120)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
    
def crash():
    
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
    largeText = pygame.font.Font('freesansbold.ttf',120)
    TextSurf, TextRect = text_objects('You Crashed', largeText, red)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        button("Play Again", 245,415,110,50, green,bright_green,game_loop)
        button("Quit", 455,415,110,50, red,bright_red,quit_game)
        pygame.display.update()
        clock.tick(15)
        
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',120)
        TextSurf, TextRect = text_objects('PyRacer', largeText, (255,99,71))
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button("GO!",245,415,100,50,bright_green,green,game_loop)
        
        button("Quit",455,415,100,50,bright_red,red,quit_game)
        # button(msg, x,y,w,h,ic,ac):
        
        pygame.display.update()
        clock.tick(15)
        
        
def game_loop(): 
    global pause
    global otherCar_width
    global otherCar_height
    pygame.mixer.music.play(-1)
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
   # otherCars = 1
    otherCarStartX = random.randrange(0, display_width)
    otherCarStartY = -600
    otherCarSpeed = 7.8
    
    
#    thing_startx = random.randrange(0, display_width)
#    thing_starty = -600
#    thing_speed = 7.8
#    thing_width = 90
#    thing_height = 90
#    thing_count = 1
    
    dodged = 0
    gameExit = False
    high_score = get_high_score()
    #impossible_mode = False

    while not gameExit:
        gameDisplay.blit(bg, [0,0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                # left arrow
                if event.key == pygame.K_LEFT:
                    x_change = -12
                    
                    
                # right arrow
                if event.key == pygame.K_RIGHT:
                    x_change = 12
                
                # pause
                if event.key == pygame.K_p:
                    pause = True
                    pause_game()
                
                
                    
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    
        x += x_change
        #gameDisplay.fill(white)
        
        # things(thingx, thingy, thingw,thingh, color)
#        things(thing_startx, thing_starty, thing_width, thing_height, black)
        otherCar(otherCarStartX,otherCarStartY)
        otherCarStartY += otherCarSpeed
        
        
        car(x,y)
        
        things_dodged(dodged)
        
        display_highest_score(high_score)
        
        if x > (display_width - car_width) or x < 0:
            if dodged >= high_score:
                high_score = dodged
                with open('score.dat','wb') as file:
                    pickle.dump(high_score,file)
            crash()
            
        if otherCarStartY > display_height:
            otherCarStartY = 0 - otherCar_height
            otherCarStartX = random.randrange(0, display_width)
            dodged+=1
            otherCarSpeed+=.8
#            if impossible_mode == True:
#                otherCar_width = otherCar_width + (otherCar_width*1.4)
            #thing_count +=2 
#            if y < thing_starty + thing_height:
#            print('step 1')
#            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx + thing_width:
#                print('x crossover')
#                if dodged >= high_score:
#                    high_score = dodged
#                    with open('score.dat','wb') as file:
#                        pickle.dump(high_score,file)
#                car_crashed(x,y)
            
        if y < otherCarStartY + otherCar_height:
            if x > otherCarStartX and x < otherCarStartX + otherCar_width or x+car_width > otherCarStartX and x + car_width < otherCarStartX + otherCar_width:
                if dodged >= high_score:
                    high_score = dodged
                    with open('score.dat','wb') as file:
                        pickle.dump(high_score,file)
                car_crashed(x,y)
                
                crash()
           
        pygame.display.update()
        clock.tick(60)
game_intro()           
game_loop()
