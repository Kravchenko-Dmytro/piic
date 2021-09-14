import random

import  pygame
#0-empty;1-walls;2-food;3-player;4-enemies
x=0; y=0
speed=10
a=500; b=500
n=10
pygame.init()
window=pygame.display.set_mode((a,b))
pygame.display.set_caption("Pac-Man")
labirynt=[[0] * b for i in range(a)]
labirynt[x][y]=3
zapovnenist=(a//speed)//10
for i in range(0,a,10):
    k=0
    while k<zapovnenist:
        r=((random.randint(0,b-11))//10)*10
        if labirynt[i][r]==0:
            labirynt[i][r]=1
            k+=1
k=0
while k!=n:
    f=True
    c=((random.randint(0,a-11))//10)*10
    d=((random.randint(0,b-11))//10)*10
    if labirynt[c][d]==0:
        labirynt[c][d]=2
        k+=1
game=True
victory=0
while game:
    pygame.time.delay(1)

    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>=speed and labirynt[x-speed][y]!=1:
        labirynt[x][y] = 0
        x -= speed
        labirynt[x][y] = 3

    if keys[pygame.K_RIGHT] and x<a-speed and labirynt[x+speed][y]!=1:
        labirynt[x][y] = 0
        x+=speed
        labirynt[x][y] = 3

    if keys[pygame.K_UP] and y>=speed and labirynt[x][y-speed]!=1:
        labirynt[x][y] = 0
        y-=speed
        labirynt[x][y] = 3

    if keys[pygame.K_DOWN] and y<b-speed and labirynt[x][y+speed]!=1:
        labirynt[x][y] = 0
        y+=speed
        labirynt[x][y] = 3

    window.fill((0,0,0))

    for i in range(a):
        for j in range(b):
            if labirynt[i][j]==1:
                pygame.draw.rect(window,(67,35,255),(i,j,speed,speed))

    for i in range(a):
        for j in range(b):
            if labirynt[i][j]==2:
                pygame.draw.rect(window,(255,255,255),(i,j,speed,speed))


    pygame.draw.rect(window,(255,255,0),(x, y, speed, speed))
    pygame.display.update()
    victory=1
    for i in range(a):
        for j in range(b):
            if labirynt[i][j]==2:
                victory=0
    if victory==1:
        game=False

if victory==1:
    intro=True
    while intro:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
        window.fill((0,0,0))
        font=pygame.font.Font(None,150)
        text=font.render("Victory!",True,(255,255,255))
        place=text.get_rect(center=(a//2,b//2))
        window.blit(text,place)
        pygame.display.update()
