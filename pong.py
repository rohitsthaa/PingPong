#import and initialization

import pygame,os,sys,random
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((800,600),FULLSCREEN)
pygame.mouse.set_visible(1)
clock=pygame.time.Clock()

#variable initialization

ball_posx=375
ball_posy=290
ball1_posx=0
ball1_posy=0
ball2_posx=780
ball2_posy=0
t=1
vel=[2,1]
player1score=0
player2score=0
restart=0

#image import

draw=os.path.join('image','draw.jpg')
draw=pygame.image.load(draw)
draw=pygame.transform.scale(draw,(800,600))
pla1=os.path.join('image','pla1.jpg')
pla1=pygame.image.load(pla1)
pla1=pygame.transform.scale(pla1,(800,600))
pla2=os.path.join('image','pla2.jpg')
pla2=pygame.image.load(pla2)
pla2=pygame.transform.scale(pla2,(800,600))
header=os.path.join('image','header1.jpg')
header=pygame.image.load(header)
header=pygame.transform.scale(header,(800,30))
##timer=os.path.join('image','timer.gif')
##timer=pygame.image.load(timer)
##timer=pygame.transform.scale(timer,(300,60))
start=os.path.join('image','h1.jpg')
start=pygame.image.load(start)
start=pygame.transform.scale(start,(800,600))
about1=os.path.join('image','h3.jpg')
about1=pygame.image.load(about1)
about1=pygame.transform.scale(about1,(800,600))
quits=os.path.join('image','quit.jpg')
quits=pygame.image.load(quits)
quits=pygame.transform.scale(quits,(200,50))
highscore=os.path.join('image','h2.jpg')
highscore=pygame.image.load(highscore)
highscore=pygame.transform.scale(highscore,(200,50))
starting=os.path.join('image','starting.jpg')
starting=pygame.image.load(starting)
starting=pygame.transform.scale(starting,(200,50))
court=os.path.join('image','COURT.gif')
court = pygame.image.load(court).convert_alpha()
court=pygame.transform.scale(court,(800,570))
car = os.path.join('image','BAR.gif')
car = pygame.image.load(car).convert_alpha()
car=pygame.transform.scale(car,(20,180))
ball = os.path.join('image','ball.gif')
ball=pygame.image.load(ball)
ball=pygame.transform.scale(ball,(40,40))
startimg=os.path.join('image','startimage.jpg')
startimg = pygame.image.load(startimg).convert_alpha()
startimg=pygame.transform.scale(startimg,(800,600))
startbutton=os.path.join('image','startb.png')
startbutton = pygame.image.load(startbutton).convert_alpha()
startbutton=pygame.transform.scale(startbutton,(130,130))


#Function declaration
def variable():
    global ball_posx,ball_posy,ball1_posx,ball1_posy,ball2_posx,ball2_posy,t,vel,player1score,player2score,restart
    ball_posx=375
    ball_posy=290
    ball1_posx=0
    ball1_posy=0
    ball2_posx=780
    ball2_posy=0
    t=1
    vel=[2,1]
    player1score=0
    player2score=0
    restart=0

def draw_ball(ball_posx,ball_posy):
    screen.blit(ball,(ball_posx,ball_posy))
    #pygame.display.update()
    #pygame.display.flip()

def draw_bar(ball1_posx,ball1_posy,ball2_posx,ball2_posy):
    screen.blit(car,(ball1_posx,ball1_posy))
    screen.blit(car,(ball2_posx,ball2_posy))
    #pygame.display.flip()

def strikesound():
    sound = os.path.join('sound','POP.mp3')
    sound = pygame.mixer.music.load(sound)
    pygame.mixer.music.play(0)

def background():
    screen.blit(court,(0,0))
    screen.blit(header,(0,570))
    #pygame.display.update()

def Text(string,(x,y), size = 12, color = (0,255,0) ):
	font = pygame.font.SysFont(None,size)
	text = font.render(string, 1, color)
	screen.blit(text,(x,y))

def menu():
    screen.blit(start,(0,0))
    title1=screen.blit(starting,(250,175))
    title2=screen.blit(highscore,(250,300))
    title3=screen.blit(quits,(250,425))
    pygame.display.update()

#Main executuion
screen.blit(startimg,(0,0))
pygame.display.update()
sound = os.path.join('sound','start.mp3')
sound = pygame.mixer.music.load(sound)
pygame.mixer.music.play(0)
pygame.time.delay(3700)
screen.blit(start,(0,0))
title1=screen.blit(starting,(250,175))
title2=screen.blit(highscore,(250,300))
title3=screen.blit(quits,(250,425))
pygame.display.update()
while True:
    variable()
    restart=0
    pygame.init()
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            pos=pygame.mouse.get_pos()
            if title1.collidepoint(pos):
                background()
                draw_bar(ball1_posx,ball1_posy,ball2_posx,ball2_posy)
                b=screen.blit(startbutton,(335,225))
                pygame.display.update()
                while restart==0:
                    for event in pygame.event.get():
                        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                            pos1=pygame.mouse.get_pos()
                            if b.collidepoint(pos1):
                                font = pygame.font.SysFont('Arial',30)
                                #text = font.render(' **** START *** ', 10, (0,255,255))
                                #screen.blit(text,(350,280))
                                #pygame.display.update()
                                background()
                                draw_bar(ball1_posx,ball1_posy,ball2_posx,ball2_posy)
                                draw_ball(ball_posx,ball_posy)
                                pygame.display.update()
                                pygame.time.delay(2000)
                                while restart==0:
##                                    for event in pygame.event.get():
##                                                if event.type == QUIT:
##                                                        sys.exit()
##                                                elif event.type == KEYDOWN:
##                                                        if event.key == K_ESCAPE:
##                                                            sys.exit()

                                    background()
                                    draw_bar(ball1_posx,ball1_posy,ball2_posx,ball2_posy)
                                    draw_ball(ball_posx,ball_posy)
                                    score1 = font.render('SCORE R:: '+ str(player1score), 50, (255,255,255))
                                    screen.blit(score1,(640,570))
                                    #pygame.display.update()
                                    score2 = font.render('SCORE L:: ' + str(player2score), 50, (255,255,255))
                                    screen.blit(score2,(10,570))
                                    pygame.display.update()

                                    #ball velocity control

                                    ball_posx+=vel[0]
                                    ball_posy+=vel[1]
                                    if ball_posx<=30 and ball_posy>=ball1_posy and ball_posy<=(ball1_posy+180):
                                        vel[0]=-vel[0]
                                        strikesound()
                                    if ball_posx>=730 and ball_posy>=ball2_posy and ball_posy<=(ball2_posy+180):
                                        vel[0]=-vel[0]
                                        strikesound()
                                    if ball_posy<=30:
                                        vel[1]=-vel[1]
                                    if ball_posy>=525:
                                        vel[1]=-vel[1]

                                    #pygame.time.delay(50)
                                    t=t+1

                                    #bar control
                                    pressed_key=pygame.key.get_pressed()
                                    if pressed_key[K_UP]:
                                        if ball2_posy>=0:
                                            ball2_posy-=6
                                    elif pressed_key[K_DOWN]:
                                        if ball2_posy<=386:
                                            ball2_posy+=6
                                    elif pressed_key[K_z]:
                                        if ball1_posy<=386:
                                            ball1_posy+=6
                                    elif pressed_key[K_q]:
                                        if ball1_posy>=0:
                                            ball1_posy-=6
                                    #elif pressed_key[K_ESCAPE]:
                                     #   sys.exit()

                                    if ball_posx>800:
                                        player2score+=1
                                        ball_posx=375
                                        ball_posy=290
                                        vel=[2,1]
                                        background()
                                        draw_bar(ball1_posx,ball1_posy,ball2_posx,ball2_posy)
                                        draw_ball(ball_posx,ball_posy)
                                        pygame.display.update()
                                        pygame.time.delay(1000)
                                    if ball_posx<0:
                                        player1score+=1
                                        ball_posx=375
                                        ball_posy=290
                                        vel=[-2,1]
                                        background()
                                        draw_bar(ball1_posx,ball1_posy,ball2_posx,ball2_posy)
                                        draw_ball(ball_posx,ball_posy)
                                        pygame.display.update()
                                        pygame.time.delay(1000)
                                    for event in pygame.event.get():
                                        #if event.type == QUIT:
                                         #   sys.exit()
                                        if event.type == KEYDOWN:
                                            if event.key == K_ESCAPE:
                                                restart=1
                                                menu()
                                    if player1score==15:
                                        screen.blit(pla1,(0,0))
                                        pygame.display.update()
                                        pygame.time.delay(3000)
                                        restart=1
                                        timepassed=0
                                        pygame.init()
                                        menu()
                                    if player2score==15:
                                        screen.blit(pla2,(0,0))
                                        pygame.display.update()
                                        pygame.time.delay(3000)
                                        restart=1
                                        menu()


            elif title2.collidepoint(pos):
                screen.blit(about1,(0,0))
                pygame.display.update()
                pygame.display.flip()
                pygame.time.delay(3500)
                menu()

            elif title3.collidepoint(pos):
               pygame.quit()
               sys.exit()
