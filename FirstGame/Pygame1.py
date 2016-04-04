import pygame, sys, time,math
from pygame.locals import*
pygame.init()
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLACK=(0,0,0)
BLUE=(0,0,255)
topx=0
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
Var1S=1000
TH1=pygame.Rect(0,0,0,0)
TH=pygame.image.load('TH.png')
TH2=pygame.transform.scale(TH, (1080, 920))
while True:
    topx=topx+Var1S
    rectangle=pygame.draw.rect(windowSurface, BLUE, (topx, 50, 50, 50))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    if rectangle.right>=WINDOWWIDTH:
        windowSurface.fill(RED)
        windowSurface.blit(TH2, TH1)
        Var1S=-Var1S
    elif rectangle.left <= 0:
        windowSurface.fill(BLACK)
        Var1S=-Var1S
        
    time.sleep(0.02)
