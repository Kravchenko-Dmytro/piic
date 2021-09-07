import random

import  pygame

x=0; y=0
width=10; height=10
speed=10
a=500; b=500
n=3
pygame.init()
window=pygame.display.set_mode((a,b))
pygame.display.set_caption("Pac-Man")


foodx=[]
foody=[]
while len(foodx)!=n:
    f=True
    c=((random.randint(0,a-11))//10)*10
    d=((random.randint(0,b-11))//10)*10
    if c==x and d==y:
        f=False
    for i in range(len(foodx)):
        if c==foodx[i] and d==foody[i]:
            f=False
    if (f):
        foodx.append(c)
        foody.append(d)


game=True
while game:
    pygame.time.delay(100)

    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            game=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>=10:
        x-=speed
        for i in range(len(foodx)-1):
            if x==foodx[i] and y==foody[i] :
                foodx=foodx[:i]+foodx[i+1:]
                foody = foody[:i] + foody[i + 1:]
#            if x==foodx[i] and y==foody[i] and i==len(foodx)-1:
#                print("++++++++++++++++")
#                foodx =foodx[:-1]
#                foody =foody[:-1]

    if keys[pygame.K_RIGHT] and x<a-width:
        x+=speed

        for i in range(len(foodx)-1):
            if x==foodx[i] and y==foody[i]:
                foodx=foodx[:i]+foodx[i+1:]
                foody = foody[:i] + foody[i + 1:]

    if keys[pygame.K_UP] and y>=10:
        y-=speed

        for i in range(len(foodx)-1):
            if x==foodx[i] and y==foody[i]:
                foodx=foodx[:i]+foodx[i+1:]
                foody = foody[:i] + foody[i + 1:]

    if keys[pygame.K_DOWN] and y<b-height:
        y+=speed

        for i in range(len(foodx)-1):
            if x==foodx[i] and y==foody[i]:
               foodx=foodx[:i]+foodx[i+1:]
               foody = foody[:i] + foody[i + 1:]

    window.fill((0,0,0))


    for i in range(len(foodx)):
        pygame.draw.rect(window,(255,255,255),(foodx[i],foody[i],10,10))


    pygame.draw.rect(window,(255,255,0),(x, y, width, height))
    pygame.display.update()