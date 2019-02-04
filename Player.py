import pygame
from pygame.locals import *
pygame.init()
import DrawImage

def drawPlayer(pos, offset, display):
    DrawImage.blitImage(pygame.image.load("PlayerImage.png"), pos, offset, display)

def movePlayer(pos, offset, tick):
    keys = pygame.key.get_pressed()
    if keys[K_d]:
        pos[0] += 90 * tick
        offset[0] += 90 * tick
    if keys[K_a]:
        pos[0] -= 90 * tick
        offset[0] -= 90 * tick
    if keys[K_w]:
        pos[1] += 90 * tick
        offset[1] += 90 * tick
    if keys[K_s]:
        pos[1] -= 90 * tick
        offset[1] -= 90 * tick
