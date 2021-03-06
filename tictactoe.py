"""TIC TAC TOE"""

import pygame
import sys
import time

clock = pygame.time.Clock()

#color definitions
BLACK=(0,0,0)
GREEN=(0,255,0)
BRIGHT_GREEN=(0,200,0)
RED=(255,0,0)
BRIGHT_RED=(200,0,0)
WHITE=(255,255,255)
BLUE=(0,0,255)
BRIGHT_BLUE=(0,0,200)

#dipsplay details
display_width = 900
display_height = 600


#surface
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Tic-Tac-Toe")
#centres of the 9 boxes
a1=(350,200)
a2=(450,200)
a3=(550,200)
b1=(350,300)
b2=(450,300)
b3=(550,300)
c1=(350,400)
c2=(450,400)
c3=(550,400)


class Player(object):
    def __init__(self,click,box):

        self.click=click
        self.box=box


    def get_box(self,pos):

        if pos[0] in range(300,400) and pos[1] in range(150,250):
            self.box=a1
        elif pos[0] in range(400,500) and pos[1] in range(150,250):
            self.box=a2
        elif pos[0] in range(500,600) and pos[1] in range(150,250):
            self.box=a3
        elif pos[0] in range(300,400) and pos[1] in range(250,350):
            self.box=b1
        elif pos[0] in range(400,500) and pos[1] in range(250,350):
            self.box=b2
        elif pos[0] in range(500,600) and pos[1] in range(250,350):
            self.box=b3
        elif pos[0] in range(300,400) and pos[1] in range(350,450):
            self.box=c1
        elif pos[0] in range(400,500) and pos[1] in range(350,450):
            self.box=c2
        elif pos[0] in range(500,600) and pos[1] in range(350,450):
            self.box=c3
        else:
            pass


def get_box1(pos):
    if pos[0] in range(300,400) and pos[1] in range(150,250):
        box=a1
    elif pos[0] in range(400,500) and pos[1] in range(150,250):
        box=a2
    elif pos[0] in range(500,600) and pos[1] in range(150,250):
        box=a3
    elif pos[0] in range(300,400) and pos[1] in range(250,350):
        box=b1
    elif pos[0] in range(400,500) and pos[1] in range(250,350):
        box=b2
    elif pos[0] in range(500,600) and pos[1] in range(250,350):
        box=b3
    elif pos[0] in range(300,400) and pos[1] in range(350,450):
        box=c1
    elif pos[0] in range(400,500) and pos[1] in range(350,450):
        box=c2
    elif pos[0] in range(500,600) and pos[1] in range(350,450):
        box=c3
    else:
        box=None
        pass
    return box
def X(x,y): #Draws an X
    pygame.draw.line(gameDisplay,WHITE,(x-40,y-40),(x+40,y+40),2)
    pygame.draw.line(gameDisplay,WHITE,(x+40,y-40),(x-40,y+40),2)


def drawX(box): #draw an X in given box using the X() function
    if box==a1:
        X(a1[0],a1[1])
    if box==a2:
        X(a2[0],a2[1])
    if box==a3:
        X(a3[0],a3[1])
    if box==b1:
        X(b1[0],b1[1])
    if box==b2:
        X(b2[0],b2[1])
    if box==b3:
        X(b3[0],b3[1])
    if box==c1:
        X(c1[0],c1[1])
    if box==c2:
        X(c2[0],c2[1])
    if box==c3:
        X(c3[0],c3[1])
    pygame.display.update()

def drawO(box):  #Draw an O into a box
    if box==a1:
        pygame.draw.circle(gameDisplay,WHITE,a1,40,2)
    if box==a2:
        pygame.draw.circle(gameDisplay,WHITE,a2,40,2)
    if box==a3:
        pygame.draw.circle(gameDisplay,WHITE,a3,40,2)
    if box==b1:
        pygame.draw.circle(gameDisplay,WHITE,b1,40,2)
    if box==b2:
        pygame.draw.circle(gameDisplay,WHITE,b2,40,2)
    if box==b3:
        pygame.draw.circle(gameDisplay,WHITE,b3,40,2)
    if box==c1:
        pygame.draw.circle(gameDisplay,WHITE,c1,40,2)
    if box==c2:
        pygame.draw.circle(gameDisplay,WHITE,c2,40,2)
    if box==c3:
        pygame.draw.circle(gameDisplay,WHITE,c3,40,2)
    pygame.display.update()

def quitgame(): #PUT LINK TO GAME MENU HERE
    pygame.quit()

def drawgrid():

    pygame.draw.line(gameDisplay,RED,(400,150),(400,450),2)
    pygame.draw.line(gameDisplay,RED,(500,150),(500,450),2)
    pygame.draw.line(gameDisplay,RED,(300,250),(600,250),2)
    pygame.draw.line(gameDisplay,RED,(300,350),(600,350),2)
    pygame.display.update() #to apply the grid that i just drew


def checkwin(moves):
    win=False
    if (a1 in moves) and (a2 in moves) and (a3 in moves):
        win=True
    elif (b1 in moves) and (b2 in moves) and (b3 in moves):
        win=True
    elif (c1 in moves) and (c2 in moves) and (c3 in moves):
        win=True
    elif (a1 in moves) and (b1 in moves) and (c1 in moves):
        win=True
    elif (a2 in moves) and (b2 in moves) and (c2 in moves):
        win=True
    elif (a3 in moves) and (b3 in moves) and (c3 in moves):
        win=True
    elif (a1 in moves) and (b2 in moves) and (c3 in moves):
        win=True
    elif (a3 in moves) and (b2 in moves) and (c1 in moves):
        win=True
    return win

def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text,x,y,size,color):
    largeText = pygame.font.SysFont("calibri",size)
    TextSurf, TextRect = text_objects(text, largeText,color)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()





def button(msg,color,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            gameDisplay.fill(BLACK)

            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText,color)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def decidemove(totalmoves,compmoves):
    #step 1

    pass





def gameintro():
    pygame.init()
    gameDisplay.fill(BLACK)
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
        message_display('TIC-TAC-TOE',450,150,150,RED)

        #button("vs COMP",BLACK,350,250,200,60,GREEN,BRIGHT_GREEN,vsComp)
        button("PLAY",BLACK,350,350,200,60,BLUE,BRIGHT_BLUE,vsPlayer)
        button("QUIT",BLACK,790,540,100,50,RED,BRIGHT_RED,quitgame)



        pygame.display.update()

        clock.tick(60)


def vsPlayer():
    Player1=Player(0,0) #thiis should be displayed as USERNAME
    Player2=Player(0,0)
    drawgrid()
    message_display("Player 1:X   Player 2:O",100,20,20,WHITE)
    count=0
    totalmoves=[]
    player1moves=[]
    player2moves=[]
    won=False
    done=False
    while not done:
        clock.tick(60)

        for event in pygame.event.get():
            if count==0:
                count+=1
                pass

            elif event.type==pygame.QUIT:

                done=True
                quitgame()

            elif count>=10:
                if won==False:
                        gameDisplay.fill(BLACK)
                        message_display("IT'S A TIE!",450,250,100,WHITE)
                        time.sleep(1)

                done=True

            elif event.type==pygame.MOUSEBUTTONUP and get_box1(event.pos) not in totalmoves and event.pos[0] in range(300,600) and event.pos[1] in range(150,450):

                position=get_box1(event.pos)
                totalmoves.append(position)
                print (totalmoves)

                if count%2==1:
                    Player1.get_box(position)
                    drawX(Player1.box)
                    player1moves.append(Player1.box)
                    count+=1
                    if checkwin(player1moves)==True:
                        won=True
                        gameDisplay.fill(BLACK)
                        message_display('PLAYER 1 WINS!',450,250,100,WHITE)
                        time.sleep(1)
                        gameintro()

                    break
                if count%2==0:
                    Player2.get_box(position)
                    drawO(Player2.box)
                    player2moves.append(Player2.box)
                    count+=1
                    if checkwin(player2moves)==True:
                        won=True
                        gameDisplay.fill(BLACK)
                        message_display('PLAYER 2 WINS!',450,250,100,WHITE)
                        time.sleep(1)
                        gameintro()
                    break



        pygame.display.update()



    gameDisplay.fill(BLACK)
    gameintro()




def vsComp():
    comp=Player(0,0)
    Player1=Player(0,0)
    drawgrid()
    message_display("Player 1:X Computer:O",100,20,20,WHITE)
    count=0
    totalmoves=[]
    player1moves=[]
    compmoves=[]
    won=False
    done=False
    while (not done) and (not won):
        clock.tick(60)
        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                done=True
                quitgame()


            elif count>=9:
                if won==False:
                    gameDisplay.fill(BLACK)
                    message_display("IT'S A TIE!",450,250,100,WHITE)
                    time.sleep(1)
                done=True



            elif (event.type==pygame.MOUSEBUTTONUP and get_box1(event.pos) not in totalmoves and event.pos[0] in range(300,600) and event.pos[1] in range(150,450)) and count%2==0:

                position=get_box1(event.pos)
                totalmoves.append(position)
                print (totalmoves)


                Player1.get_box(position)
                drawX(Player1.box)
                player1moves.append(Player1.box)
                count+=1
                if checkwin(player1moves)==True:
                    won=True
                    gameDisplay.fill(BLACK)
                    message_display('PLAYER 1 WINS!',450,250,100,WHITE)
                    time.sleep(1)
                    gameintro()



            elif count%2==1:
                time.sleep(0.5)

                count+=1

                position=decidemove(totalmoves,compmoves)
                totalmoves.append(position)
                compmoves.append(position)
                drawO(position)
                count+=1
                if checkwin(compmoves)==True:
                        won=True
                        gameDisplay.fill(BLACK)
                        message_display('COMPUTER WINS!',450,250,100,WHITE)
                        time.sleep(1)
                        gameintro()





            pygame.display.update()


    gameDisplay.fill(BLACK)
    gameintro()




gameintro()

quit()
