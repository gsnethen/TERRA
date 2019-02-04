import pygame
from pygame.locals import *
pygame.init()
import random
import time
import sys
import WorldGeneration
import DrawImage
import TileImage

screen = pygame.display.set_mode([1200 , 800])
font = pygame.font.SysFont("comicsansms", 20)
pygame.mouse.set_visible(False)

world = WorldGeneration.generateWorld()

while True:
    for y in range(len(world)):
        for x in range(len(world[y])):
            DrawImage.blitImage(TileImage.getImage(world[y][x][0]), [x * 45, y * 45], [0, 0], screen)

    DrawImage.drawDisplay()

    pygame.event.get()
