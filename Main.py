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

playerPos = [0, 0]
cameraOffset = [-622.5, -422.5]
playerVel = [0, 0]

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

    tickTime = time.time() - tickTime

    playerVel[0] -= (playerVel[0] * 3) * tickTime
    playerVel[1] += 665 * tickTime

    playerPos[0] += playerVel[0] * tickTime
    cameraOffset[0] += playerVel[0] * tickTime
    for row in world:
            for tile in row:
                if tile[0] != "TILE_AIR":
                    if Rect(playerPos[0], playerPos[1], 45, 45).colliderect(Rect(tile[1][0] * 45, tile[1][1] * 45, 45, 45)):
                        playerPos[0] -= playerVel[0] * tickTime
                        cameraOffset[0] -= playerVel[0] * tickTime
                        playerVel[0] = 0
                        
    playerPos[1] += playerVel[1] * tickTime
    cameraOffset[1] += playerVel[1] * tickTime
    for row in world:
            for tile in row:
                if tile[0] != "TILE_AIR":
                    if Rect(playerPos[0], playerPos[1], 45, 45).colliderect(Rect(tile[1][0] * 45, tile[1][1] * 45, 45, 45)):
                        playerPos[1] -= playerVel[1] * tickTime
                        cameraOffset[1] -= playerVel[1] * tickTime
                        playerVel[1] = 0
                        
    if keys[K_d]:
        playerVel[0] += 665 * tickTime
        
    if keys[K_a]:
        playerVel[0] -= 665 * tickTime

    if keys[K_SPACE] and playerVel[1] == 0:
        playerVel[1] -= 665
        
    playerVel[1] += 665 * tickTime
        
