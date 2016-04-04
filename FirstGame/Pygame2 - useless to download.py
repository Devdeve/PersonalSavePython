import pygame, sys, time,math
from pygame.locals import*
pygame.init()
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLACK=(0,0,0)
BLUE=(0,0,255)
topx1=10
topy1=100
topy=50
topx=400
WINDOWWIDTH=1080
WINDOWHEIGHT=920
windowSurface=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0,32)
windowSurface.fill(BLACK)
rectangle=pygame.draw.rect(windowSurface, BLUE, (topx, 50, 50, 50))
#rectangle=pygame.draw.rect(windowSurface, RED,(150,50,100,50))
pygame.display.update()
basicFont=pygame.font.SysFont(None,48)
text=basicFont.render("xXx_420_N0sc0p3z_xXx", True, WHITE, BLACK)
textRect=text.get_rect()
textRect.centerx=windowSurface.get_rect().centerx
textRect.centery=windowSurface.get_rect().centery
windowSurface.blit(text, textRect)
pygame.display.update()
Var1S=5
Var2S=5
TopV1=10
SideV1=5
SideV2=10
TopV2=10
TH1=pygame.Rect(0,0,0,0)
TH=pygame.image.load('TH.png')
TH2=pygame.transform.scale(TH, (1080, 920))
while True:
    windowSurface.fill(BLACK)
    time.sleep(0.0001)

    rectangle=pygame.draw.rect(windowSurface, BLUE, (topx1, topy1, 100, 100))
    rectangle1=pygame.draw.rect(windowSurface, GREEN, (topx, topy, 100, 100))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
#    print(rectangle1.top)        
    if rectangle.right>=WINDOWWIDTH:
###        windowSurface.fill(RED)
         SideV2=-SideV2
    if rectangle.top<= 0:
        TopV2=-TopV2
    if rectangle.bottom>=WINDOWHEIGHT:
        TopV2=-TopV2
    if rectangle.left <= 0:
###        windowSurface.fill(BLACK)
        SideV2=-SideV2
    if rectangle1.top<=0:
        TopV1=-TopV1
#        print(TopV1)
    if rectangle1.bottom>=WINDOWHEIGHT:
        TopV1=-TopV1
    if rectangle1.right>=WINDOWWIDTH:
        SideV1=-SideV1
    elif rectangle1.left<=0:
        SideV1=-SideV1
    if rectangle1.colliderect(rectangle):
        TopV1=-TopV1
        TopV2=-TopV2
        SideV1=-SideV1
        SideV2=-SideV2
    if event.type==KEYDOWN:
        windowSurface.fill(RED)
        pygame.display.update()
        time.sleep(0.0001)
        windowSurface.fill(BLUE)
        pygame.display.update()
        time.sleep(0.0001)
        windowSurface.fill(GREEN)
        pygame.display.update()
        time.sleep(0.0001)

    topy=topy+TopV1
    topy1=topy1+TopV2
    topx1=topx1+SideV2
    topx=topx+SideV1
    pygame.display.update()
    time.sleep(0.02)
