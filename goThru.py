import pygame as pgame
import random
import time

pgame.init()
clock = pgame.time.Clock()

screenH = 500
screenW = 600
white = (255,255,255)
red = (225,0,10)
blue = (10,0,250)
green = (230,5,10)
black = (0,0,0)
birdSize = 20
fps = 150
barW = 50
riseHeight = 3
slowHeight = 1

gameScreen = pgame.display.set_mode((screenW,screenH))
pgame.display.set_caption("Go Thru")

font = pgame.font.SysFont('comicsanms',25)
largeFont = pgame.font.SysFont(None,45)

def showMsg(text,col,placing = [ screenW/2,screenH/2 ],size = font):
    msg = size.render(text,True,col)
    msgBox = msg.get_rect()
    msgBox.center = placing[0],placing[1]
    gameScreen.blit(msg,msgBox)

def checkThis(bar,xCo,yCo):
    if xCo+birdSize > bar[2] and xCo <= bar[2]+barW:
        if yCo < bar[0]:
            return True
        elif yCo+birdSize+1 >= bar[1]:
            return True
    return False

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
    gameOver = False 
    birdPosX = screenW/2
    birdPosY = screenH/2
    riseBird = 0
    countSec = 0
    score = -1
    barOnScreen = []
    gameStart = False
    last = screenH/2
    
    while not gameExit:
        while gameOver == True:
            showMsg("Game Over, you!! Press 'P' to play again or 'Q' to quit",red,[screenW/2,screenH-50])
            pgame.display.update()
            
            for event in pgame.event.get():
                if event.type == pgame.QUIT:
                        gameExit = True
                        gameOver = False
                        break
                if event.type == pgame.KEYDOWN:
                    if event.key == pgame.K_q:
                        main()
                    elif event.key == pgame.K_p:
                        gameLoop()
        if gameExit:
            continue
        
        for event in pgame.event.get():
            if event.type == pgame.QUIT:
                gameExit = True
                break
            elif event.type == pgame.KEYDOWN:
                if event.key == pgame.K_SPACE:
                    riseBird = -riseHeight
                    gameStart = True
                elif event.key == pgame.K_p:
                    pause()
            elif event.type == pgame.KEYUP:
                if event.key == pgame.K_SPACE:
                    riseBird = slowHeight
            elif event.type == pgame.MOUSEBUTTONDOWN:
                riseBird = -riseHeight
                gameStart = True
            elif event.type == pgame.MOUSEBUTTONUP:
                riseBird = slowHeight
        
        countSec += 1
        birdPosY += riseBird
        if birdPosY <= 0 :
            birdPosY -= riseBird
        if birdPosY + birdSize > screenH :
            gameOver = True
            continue
        
        if gameStart == True:
            if countSec == fps:
                randNum = int(random.randrange(50,470)/10)*10
                while abs(last - randNum) > 100 or randNum + 90 >= screenH:
                    randNum = int(random.randrange(50,470)/10)*10
                barPos = []
                barPos.append(randNum)
                barPos.append(randNum+80)
                barPos.append(screenW)
                barOnScreen.append(barPos)
                last = randNum
                #print("New Bar")
                countSec = 0
                score += 1
        
        gameScreen.fill(white)

        if not gameStart:
            showMsg("Press 'Space' to begin or Click ",black,[screenW/2,screenH/2+50])

        if gameStart:
            for bar in reversed(barOnScreen):
                if bar[2] < 0 :
                    continue
                gameScreen.fill(blue,rect=[bar[2],0,barW,bar[0]])
                gameScreen.fill(blue,rect=[bar[2],bar[1],barW,screenH-bar[1]])
                bar[2] -= 2

                if checkThis(bar,birdPosX,birdPosY):
                    gameOver = True
                    break

        gameScreen.fill(red,rect = [birdPosX,birdPosY,birdSize,birdSize])
        
        if score < 0:
            showMsg("Score : 0",red ,[screenW/2,25])
        else:
            showMsg("Score : "+str(score),red ,[screenW/2,25])
        
        pgame.display.update()
        #for i in range(0,count):
        #    del barOnScreen[i]
        clock.tick(fps)
    pgame.quit()
    quit()
    
def main():
    gameScreen.fill(white)
    showMsg("Go Thru !!",green,[screenW/2,screenH/2-150])
    showMsg("Press 'P' to begin gameplay or 'E' to Exit.",green,[screenW/2,screenH/2-125])
    showMsg("During gameplay press 'P' to pause",green,[screenW/2,screenH/2-100])
    
    #Controls
    showMsg("Controls",black)
    showMsg("Press 'space' or click to rise and then release",black,[screenW/2,screenH/2+100])
    showMsg("by kishanp",red,[screenW/2,screenH-75])
    pgame.display.update()
    
    while True:
        for event in pgame.event.get():
            if event.type == pgame.QUIT:
                pgame.quit()
                quit()
            if event.type == pgame.KEYDOWN:
                if event.key == pgame.K_p:
                    gameLoop()
                elif event.key == pgame.K_e:
                    gameScreen.fill(white)
                    showMsg("Good Bye",red)
                    pgame.display.update()
                    pgame.quit()
                    quit()

if __name__ == "__main__": main()
