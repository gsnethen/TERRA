import pygame
from pygame.locals import *
pygame.init()
import random
import time
import sys
import WorldGeneration
import DrawImage
import TileImage
import Player

screen = pygame.display.set_mode([1200 , 800])
font = pygame.font.SysFont("comicsansms", 20)
pygame.mouse.set_visible(False)

world = WorldGeneration.generateWorld()

playerPos = [1200, 800]
cameraOffset = [622.5, 422.5]

while True:
    tickTime = time.time()
    
    DrawImage.fillDisplay([0, 0, 0], screen)
    
    for y in range(len(world)):
        for x in range(len(world[y])):
            DrawImage.blitImage(TileImage.getImage(world[y][x][0]), [x * 45, y * 45], cameraOffset, screen)

    Player.drawPlayer(playerPos, cameraOffset, screen)

    DrawImage.drawDisplay()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    Player.movePlayer(playerPos, cameraOffset, 1)
