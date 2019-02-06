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

world = WorldGeneration.generateWorld()

playerPos = [0, 0]
cameraOffset = [-622.5, -422.5]
playerVel = [0, 0]

season = 1
day = 1

items = {"ITEM_DIRT" : 0, "ITEM_STONE" : 0, "ITEM_WOOD" : 0, "ITEM_LEAF" : 0, "ITEM_PLANK" : 0}
    
selection = "ITEM_DIRT"

tileImages = {"TILE_AIR" : pygame.image.load("AirImage.png"),
              "TILE_DIRT" : pygame.image.load("DirtImage.png"),
              "TILE_STONE" : pygame.image.load("StoneImage.png"),
              "TILE_WOOD" : pygame.image.load("WoodImage.png"),
              "TILE_LEAF" : pygame.image.load("LeafImage.png"),
              "TILE_PLANK" : pygame.image.load("PlankImage.png")}

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
    screen.blit(pygame.image.load("WoodSlot.png"), [0, 90])
    screen.blit(pygame.image.load("LeafSlot.png"), [0, 135])
    text = font.render(str(items["ITEM_WOOD"]), True, [0, 0, 0], [255, 255, 255])
    screen.blit(text, [0, 90])
    text = font.render(str(items["ITEM_LEAF"]), True, [0, 0, 0], [255, 255, 255])
    screen.blit(text, [0, 135])
    screen.blit(pygame.image.load("PlankSlot.png"), [0, 180])
    #screen.blit(pygame.image.load("LeafSlot.png"), [0, 135])
    text = font.render(str(items["ITEM_PLANK"]), True, [0, 0, 0], [255, 255, 255])
    screen.blit(text, [0, 180])
    #text = font.render(str(items["ITEM_LEAF"]), True, [0, 0, 0], [255, 255, 255])
    #screen.blit(text, [0, 135])
    
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

    if keys[K_3]:
        selection = "ITEM_WOOD"

    if keys[K_4]:
        selection = "ITEM_LEAF"
        
    if keys[K_5]:
        selection = "ITEM_PLANK"
        
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
                                world[row][tile] = ["TILE_DIRT", world[row][tile][1], 1, 1]
                            if selection == "ITEM_STONE":
                                items[selection] -= 1
                                world[row][tile] = ["TILE_STONE", world[row][tile][1], 2.5, 2.5]
                            if selection == "ITEM_WOOD":
                                items[selection] -= 1
                                world[row][tile] = ["TILE_WOOD", world[row][tile][1], 2, 2]
                            if selection == "ITEM_LEAF":
                                items[selection] -= 1
                                world[row][tile] = ["TILE_LEAF", world[row][tile][1], 0.25, 0.25]
                            if selection == "ITEM_PLANK":
                                items[selection] -= 1
                                world[row][tile] = ["TILE_PLANK", world[row][tile][1], 1.5, 1.5]

    if pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[0] <= 45 and pygame.mouse.get_pos()[0] >= 0 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[1] <= 225:
            if items["ITEM_WOOD"] >= 1:
                items["ITEM_WOOD"] -= 1
                items["ITEM_PLANK"] += 5
        else:
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
                            elif world[row][tile][0] == "TILE_WOOD":
                                world[row][tile] = ["TILE_AIR", world[row][tile][1], 0, 0]
                                items["ITEM_WOOD"] += 1
                            elif world[row][tile][0] == "TILE_LEAF":
                                world[row][tile] = ["TILE_AIR", world[row][tile][1], 0, 0]
                                items["ITEM_LEAF"] += 1
                            elif world[row][tile][0] == "TILE_PLANK":
                                world[row][tile] = ["TILE_AIR", world[row][tile][1], 0, 0]
                                items["ITEM_PLANK"] += 1

    day += tickTime * 0.1
    if day >= 30:
        day = 1
        season += 1
        if season == 5:
            season = 1
        if season == 1:
            tileImages = {"TILE_AIR" : pygame.image.load("AirImage.png"),
                          "TILE_DIRT" : pygame.image.load("DirtImage.png"),
                          "TILE_STONE" : pygame.image.load("StoneImage.png"),
                          "TILE_WOOD" : pygame.image.load("WoodImage.png"),
                          "TILE_LEAF" : pygame.image.load("LeafImage.png"),
                          "TILE_PLANK" : pygame.image.load("PlankImage.png")}

        if season == 2:
            tileImages = {"TILE_AIR" : pygame.image.load("AirImage.png"),
                          "TILE_DIRT" : pygame.image.load("DirtImage.png"),
                          "TILE_STONE" : pygame.image.load("StoneImage.png"),
                          "TILE_WOOD" : pygame.image.load("WoodImage.png"),
                          "TILE_LEAF" : pygame.image.load("SummerImage.png"),
                          "TILE_PLANK" : pygame.image.load("PlankImage.png")}

        if season == 3:
            tileImages = {"TILE_AIR" : pygame.image.load("AirImage.png"),
                          "TILE_DIRT" : pygame.image.load("DirtImage.png"),
                          "TILE_STONE" : pygame.image.load("StoneImage.png"),
                          "TILE_WOOD" : pygame.image.load("WoodImage.png"),
                          "TILE_LEAF" : pygame.image.load("FallImage.png"),
                          "TILE_PLANK" : pygame.image.load("PlankImage.png")}

        if season == 4:
            tileImages = {"TILE_AIR" : pygame.image.load("AirImage.png"),
                          "TILE_DIRT" : pygame.image.load("DirtImage.png"),
                          "TILE_STONE" : pygame.image.load("StoneImage.png"),
                          "TILE_WOOD" : pygame.image.load("WoodImage.png"),
                          "TILE_LEAF" : pygame.image.load("WinterImage.png"),
                          "TILE_PLANK" : pygame.image.load("PlankImage.png")}
