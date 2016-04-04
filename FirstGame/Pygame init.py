import pygame, sys, time,math
from pygame.locals import*
screen = pygame.display.get_surface()
TH=pygame.image.load("TH.png")
background_surface = pygame.image.load("TH.png")
pygame.init()
WHITE=(255,255,255)
GREEN=(0,255,0)
BLACK=(0,0,0)
BLUE=(0,0,255)
WINDOWWIDTH=400
WINDOWHEIGHT=300
windowSurface=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0,32)
windowSurface.fill(BLACK)
pygame.display.update()
screen.blit("TH.png",(0,0))
pygame.diplay.flip
basicFont=pygame.font.SysFont(None,48)
text=basicFont.render("xXx_420_N0sc0p3z_xXx", True, WHITE, BLACK)
textRect=text.get_rect()
textRect.centerx=windowSurface.get_rect().centerx
textRect.centery=windowSurface.get_rect().centery
windowSurface.blit(text, textRect)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
