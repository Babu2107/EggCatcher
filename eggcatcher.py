import random 
import pygame
from pygame import mixer
import time
import math
pygame.init()
screen=pygame.display.set_mode((500,500))
con=True
score=0
drop=3
#breaksound=mixer.Sound('crack.wav')
pygame.display.set_caption("EGG CATCHER")
icon=pygame.image.load("logo.png")
backim=pygame.image.load("farmback.png")
chicimg=pygame.image.load("chicken.png")
nestim=pygame.image.load("nest.png")
baskim=pygame.image.load("basket.png")
eggim=pygame.image.load("egg.png")
x=mixer.Sound("music.wav")
x.play(-1)
xchange=0
plax=200
play=400
j=random.randint(0,4)
ex=[10,120,230,340,450]
ey=70
pygame.display.set_icon(icon)
def player(x,y):
    screen.blit(baskim,(x,y))
def chicken():
    x=0
    y=50
    z=70
    for i in range(5):
        screen.blit(nestim,(x,z))
        screen.blit(chicimg,(x,y))
        x+=110
def egg():
        global j
        x=0
        z=70
        for i in range(5):
            global ex,ey 
            ey+=0.1
            screen.blit(eggim,(ex[j],ey))
scofont=pygame.font.Font("eggfont.ttf",32)
gamfont=pygame.font.Font("eggfont.ttf",64)

def score_counter():
    global j,ex,ey,score,plax,play
    dis=math.sqrt(math.pow((plax-ex[j]),2)+math.pow((play-ey),2))
    if(dis<45):
        score+=1
        j=random.randint(0,4)
        ey=70
    print(dis)
def score1():
    global drop
    sco=scofont.render("score : "+str(score)+"                       CHANCES "+str(drop),True,(255,255,255))

    screen.blit(sco,(0,0))
def gameover():
    gam=gamfont.render("GAME OVER ",True,(255,0,0))
    screen.blit(gam,(100,250))  
    sco=scofont.render("score : "+str(score),True,(0,0,255))
    screen.blit(sco,(180,300))
    pygame.display.update()
while con:
    screen.fill((0,128,128))
    screen.blit(backim,(0,0))
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            con =False
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_LEFT):
                xchange=-1
            if(event.key==pygame.K_RIGHT):
                xchange=1  
        if(event.type==pygame.KEYUP):
            if(event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
                xchange=0
    plax+=xchange
    if(plax<=0):
        plax=0
    if(plax>=434):
        plax=434
    if(ey>=500):
        j=random.randint(0,4)
        drop-=1

        #breaksound.play()
        ey=70   
    if(drop==0):
        gameover()
        time.sleep(5)
        break
    player(plax,play)
    score_counter()
    score1()
    egg()
    chicken()
    pygame.display.update()

    
