import pygame
from pygame.locals import *
pygame.init()
import random
import time
import sys
import WorldGeneration

screen = pygame.display.set_mode([1200 , 800])
font = pygame.font.SysFont("comicsansms", 20)
pygame.mouse.set_visible(False)

world = WorldGeneration.generateWorld()

playerPos = [1200, 800]
cameraOffset = [622.5, 422.5]

tileImages = {"TILE_AIR" : pygame.image.load("AirImage.png"),
              "TILE_DIRT" : pygame.image.load("DirtImage.png"),
              "TILE_STONE" : pygame.image.load("StoneImage.png")}

while True:
    tickTime = time.time()
    
    screen.fill([0, 0, 0])
    
    for row in world:
        for tile in row:
            screen.blit(tileImages[tile[0]], [(tile[1][0] * 45) - cameraOffset[0], (tile[1][1] * 45) - cameraOffset[1]])

    screen.blit(pygame.image.load("PlayerImage.png"), [playerPos[0] - cameraOffset[0], playerPos[1] - cameraOffset[1]])

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_d]:
        playerPos[0] += 135 * (time.time() - tickTime)
        cameraOffset[0] += 135 * (time.time() - tickTime)
    if keys[K_a]:
        playerPos[0] -= 135 * (time.time() - tickTime)
        cameraOffset[0] -= 135 * (time.time() - tickTime)
    if keys[K_w]:
        playerPos[1] -= 135 * (time.time() - tickTime)
        cameraOffset[1] -= 135 * (time.time() - tickTime)
    if keys[K_s]:
        playerPos[1] += 135 * (time.time() - tickTime)
        cameraOffset[1] += 135 * (time.time() - tickTime)
