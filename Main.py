import pygame
from pygame.locals import *
pygame.init()
import random
import time
import sys
import WorldGeneration

screen = pygame.display.set_mode([1200 , 800], pygame.FULLSCREEN)
font = pygame.font.SysFont("comicsansms", 15)
pygame.mouse.set_visible(False)

world = WorldGeneration.generateWorld()

playerPos = [0, 0]
cameraOffset = [-622.5, -422.5]
playerVel = [0, 0]

season = 1
day = 1

items = {"ITEM_DIRT" : 0, "ITEM_STONE" : 0, "ITEM_WOOD" : 0, "ITEM_LEAF" : 0, "ITEM_PLANK" : 0, "ITEM_COPPER" : 0, "ITEM_IRON" : 0}
    
selection = "ITEM_DIRT"

upgrade = 0

tileImages = {"TILE_AIR" : pygame.image.load("AirImage.png"),
              "TILE_DIRT" : pygame.image.load("DirtImage.png"),
              "TILE_STONE" : pygame.image.load("StoneImage.png"),
              "TILE_WOOD" : pygame.image.load("WoodImage.png"),
              "TILE_LEAF" : pygame.image.load("LeafImage.png"),
              "TILE_PLANK" : pygame.image.load("PlankImage.png"),
              "TILE_COPPER" : pygame.image.load("CopperImage.png"),
              "TILE_IRON" : pygame.image.load("IronImage.png")}

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
    if upgrade == 0:
        screen.blit(pygame.image.load("EmptySlot.png"), [0, 225])
    if upgrade == 1:
        screen.blit(pygame.image.load("Level1Slot.png"), [0, 225])
    if upgrade == 2:
        screen.blit(pygame.image.load("Level2Slot.png"), [0, 225])
    if upgrade == 3:
        screen.blit(pygame.image.load("Level3Slot.png"), [0, 225])
    if upgrade == 4:
        screen.blit(pygame.image.load("Level4Slot.png"), [0, 225])
    screen.blit(pygame.image.load("CopperSlot.png"), [0, 270])
    screen.blit(pygame.image.load("IronSlot.png"), [0, 315])
    text = font.render(str(items["ITEM_COPPER"]), True, [0, 0, 0], [255, 255, 255])
    screen.blit(text, [0, 270])
    text = font.render(str(items["ITEM_IRON"]), True, [0, 0, 0], [255, 255, 255])
    screen.blit(text, [0, 315])
    
    pygame.draw.circle(screen, [255, 0, 0], [round(pygame.mouse.get_pos()[0] + 22.5), round(pygame.mouse.get_pos()[1] + 22.5)], 15)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    tickTime = time.time() - tickTime

    if not keys[K_SPACE]:
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

    if keys[K_6]:
        selection = "ITEM_COPPER"
        
    if keys[K_7]:
        selection = "ITEM_IRON"

    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()
        
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
                            if selection == "ITEM_COPPER":
                                items[selection] -= 1
                                world[row][tile] = ["TILE_COPPER", world[row][tile][1], 3.5, 3.5]
                            if selection == "ITEM_IRON":
                                items[selection] -= 1
                                world[row][tile] = ["TILE_IRON", world[row][tile][1], 5, 5]
                                
    if pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[0] <= 45 and pygame.mouse.get_pos()[0] >= 0 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[1] <= 225:
            if items["ITEM_WOOD"] >= 1:
                items["ITEM_WOOD"] -= 1
                items["ITEM_PLANK"] += 5

        elif pygame.mouse.get_pos()[0] <= 45 and pygame.mouse.get_pos()[0] >= 0 and pygame.mouse.get_pos()[1] >= 225 and pygame.mouse.get_pos()[1] <= 270:
            if items["ITEM_WOOD"] >= 2 and items["ITEM_PLANK"] >= 8 and upgrade == 0:
                items["ITEM_WOOD"] -= 2
                items["ITEM_PLANK"] -= 8
                upgrade = 1

            if items["ITEM_WOOD"] >= 4 and items["ITEM_STONE"] >= 8 and upgrade == 1:
                items["ITEM_WOOD"] -= 4
                items["ITEM_STONE"] -= 8
                upgrade = 2

            if items["ITEM_WOOD"] >= 4 and items["ITEM_COPPER"] >= 6 and upgrade == 2:
                items["ITEM_WOOD"] -= 4
                items["ITEM_COPPER"] -= 6
                upgrade = 3

            if items["ITEM_WOOD"] >= 6 and items["ITEM_IRON"] >= 6 and upgrade == 3:
                items["ITEM_WOOD"] -= 6
                items["ITEM_IRON"] -= 6
                upgrade = 4
                
        else:
            mousePos = [int((mousePos[0]) / 45), int((mousePos[1]) / 45)]
            for row in range(len(world)):
                for tile in range(len(world[row])):
                    if mousePos == world[row][tile][1]:
                        if upgrade == 0:
                            world[row][tile][2] -= tickTime * 0.2
                        if upgrade == 1:
                            world[row][tile][2] -= tickTime
                        if upgrade == 2:
                            world[row][tile][2] -= tickTime * 2.25
                        if upgrade == 3:
                            world[row][tile][2] -= tickTime * 4
                        if upgrade == 4:
                            world[row][tile][2] -= tickTime * 9.5
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
                            elif world[row][tile][0] == "TILE_COPPER":
                                world[row][tile] = ["TILE_AIR", world[row][tile][1], 0, 0]
                                items["ITEM_COPPER"] += 1
                            elif world[row][tile][0] == "TILE_IRON":
                                world[row][tile] = ["TILE_AIR", world[row][tile][1], 0, 0]
                                items["ITEM_IRON"] += 1

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
