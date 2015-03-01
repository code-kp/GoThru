import pygame as pgame
import random
import time

clock = pgame.time.Clock()

screenH = 500
screenW = 600
white = (255,255,255)
red = (225,0,10)
blue = (10,0,250)
birdSize = 20
fps = 30

riseBird = 5
slowBird = 5

gameScreen = pgame.display.set_mode((screenW,screenH))
pgame.display.set_caption("Save the bird")

font = pgame.font.SysFont(None,25)
largeFont = pgame.font.SysFont(None,45)

def showMsg(msg,color,placing = [screenW/2,screenH/2],size = font):
    toBeShown = size.render(msg,True,color)
    msgRect = toBeShown.get_rect()
    msgRect.center = placing[0],placing[1]
    gameScreen.blit(toBeShown,msgRect)

def pause():
    paused = True
    showMsg("Paused",black,size = largeFont)
    showMsg("'C' to continue or 'Q' to quit",black,[screenW/2,screenH/2+25])
    pgame.display.update()
    while paused:
        for event in pgame.event.get():
            if event.type == pgame.QUIT:
                pgame.quit()
                quit()
            elif event.type == pgame.KEYDOWN:
                if event.key == pgame.K_c:
                    paused = False
                    break
                elif event.key == pgame.K_q:
                    main()
           

def gameLoop():
    
    gameExit = False

    birdPosX = screenW/2
    birdPosY = screenH/2
    riseBirdY = 0
    riseBirdX = 0
    countSec = 0
    barOnScreen = []
    gameStart = False
    last = screenH/2
    
    while not gameExit:
        for event in pgame.event.get():
            if event.type == pgame.QUIT:
                gameExit = True
                break
            elif event.type == pgame.KEYDOWN:
                if event.key == pgame.K_UP:
                    riseBirdY = -riseBird
                    gameStart = True
                elif event.key == pgame.K_RIGHT:
                    riseBirdX = riseBird
                    gameStart = True
                elif event.key == pgame.K_p:
                    pause()
            elif event.type == pgame.KEYUP:
                if event.key == pgame.K_UP or event.key == pgame.K_RIGHT or event.key == pgame.K_LEFT:
                    riseBirdY = slowBird
                    riseBirdX = 0
                     
        countSec += 1
        birdPosX += riseBirdX
        birdPosY += riseBirdY

        if birdPosX+birdSize >= screenW :
            birdPosX -= riseBirdX
        if birdPosY <= 0 :
            birdPosY -= riseBirdY

        if gameStart == True:
            if countSec == fps:
                randNum = int(random.randrange(50,470)/10)*10
                while not abs(last - randNum) < 100:
                    randNum = int(random.randrange(50,470)/10)*10
                barPos = []
                barPos.append(randNum)
                barPos.append(randNum+80)
                barPos.append(screenW)
                barOnScreen.append(barPos)
                last = randNum
                print("New Bar")
                countSec = 0
        
        gameScreen.fill(white)
        gameScreen.fill(red,rect = [birdPosX,birdPosY,birdSize,birdSize])
        pgame.display.update()
        
        count = 0
        if count <= 3:
            for bar in barOnScreen:
                gameScreen.fill(blue,rect=[bar[2],0,50,bar[0]])
                gameScreen.fill(blue,rect=[bar[2],bar[1],50,screenH-bar[1]])
                bar[2] -= 10
        else:
            count = 1
            while count<3:
                bar = barOnScreen[-count]
                gameScreen.fill(blue,rect=[bar[2],0,50,bar[0]])
                gameScreen.fill(blue,rect=[bar[2],bar[1],50,screenH-bar[1]])
                bar[2] -= 10
                count += 1
        pgame.display.update()
        count += 1
        #for i in range(0,count):
        #    del barOnScreen[i]
        clock.tick(fps)
    pgame.quit()
    quit()
    

gameLoop()
    

