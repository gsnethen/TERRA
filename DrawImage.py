import pygame
from pygame.locals import *
pygame.init()

def blitImage(image, pos, offset, display):
    display.blit(image, [pos[0] - offset[0], pos[1] - offset[1]])

def fillDisplay(color, display):
    display.fill(color)

def drawDisplay():
    pygame.display.flip()
