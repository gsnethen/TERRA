import pygame
from pygame.locals import *
pygame.init()
import random
import time
import sys
import WorldGeneration

screen = pygame.display.set_mode([1200 , 800])
font = pygame.font.SysFont("comicsansms", 15)
pygame.mouse.set_visible(False)

dev = True

world = WorldGeneration.generateWorld()

playerPos = [0, 0]
cameraOffset = [-622.5, -422.5]
playerVel = [0, 0]

if dev:
    items = {"ITEM_DIRT" : (10 ** 100), "ITEM_STONE" : (10 ** 100)}
else:
    items = {"ITEM_DIRT" : 0, "ITEM_STONE" : 0}
    
selection = "ITEM_DIRT"

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

    screen.blit(pygame.image.load("DirtSlot.png"), [0, 0])
    screen.blit(pygame.image.load("StoneSlot.png"), [0, 45])
    text = font.render(str(items["ITEM_DIRT"]), True, [0, 0, 0], [255, 255, 255])
    screen.blit(text, [0, 0])
    text = font.render(str(items["ITEM_STONE"]), True, [0, 0, 0], [255, 255, 255])
    screen.blit(text, [0, 45])
    
    pygame.draw.circle(screen, [255, 0, 0], [round(pygame.mouse.get_pos()[0] + 22.5), round(pygame.mouse.get_pos()[1] + 22.5)], 15)

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
                        if playerVel[1] > 0:
                            playerVel[1] = 0
                        else:
                            playerVel[1] = -1
                        
    if keys[K_d]:
        playerVel[0] += 665 * tickTime
        
    if keys[K_a]:
        playerVel[0] -= 665 * tickTime

    if keys[K_SPACE]:
        if playerVel[1] == 0:
            playerVel[1] -= 665

    if keys[K_1]:
        selection = "ITEM_DIRT"

    if keys[K_2]:
        selection = "ITEM_STONE"
        
    playerVel[1] += 665 * tickTime

    for row in range(len(world)):
        for tile in range(len(world[row])):
            world[row][tile][2] += 0.05 * tickTime
            if world[row][tile][2] > world[row][tile][3]:
                world[row][tile][2] = world[row][tile][3]

    mousePos = [round((pygame.mouse.get_pos()[0] + cameraOffset[0]) / 45) * 45, round((pygame.mouse.get_pos()[1] + cameraOffset[1]) / 45) * 45]

    if pygame.mouse.get_pressed()[2]:
        mousePos = [int((mousePos[0]) / 45), int((mousePos[1]) / 45)]
        for row in range(len(world)):
            for tile in range(len(world[row])):
                if mousePos == world[row][tile][1]:
                    if world[row][tile][0] == "TILE_AIR":
                        if items[selection] >= 1:
                            if selection == "ITEM_DIRT":
                                items[selection] -= 1
                                world[row][tile] = ["TILE_DIRT", world[row][tile][1], 0.5, 0.5]
                            if selection == "ITEM_STONE":
                                items[selection] -= 1
                                world[row][tile] = ["TILE_STONE", world[row][tile][1], 1, 1]
                        

    if pygame.mouse.get_pressed()[0]:
        mousePos = [int((mousePos[0]) / 45), int((mousePos[1]) / 45)]
        for row in range(len(world)):
            for tile in range(len(world[row])):
                if mousePos == world[row][tile][1]:
                    world[row][tile][2] -= tickTime
                    if world[row][tile][2] < 0:
                        if world[row][tile][0] == "TILE_AIR":
                            world[row][tile] = ["TILE_AIR", world[row][tile][1], 0, 0]
                        elif world[row][tile][0] == "TILE_DIRT":
                            world[row][tile] = ["TILE_AIR", world[row][tile][1], 0, 0]
                            items["ITEM_DIRT"] += 1
                        elif world[row][tile][0] == "TILE_STONE":
                            world[row][tile] = ["TILE_AIR", world[row][tile][1], 0, 0]
                            items["ITEM_STONE"] += 1

