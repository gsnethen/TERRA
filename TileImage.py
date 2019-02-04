import pygame
from pygame.locals import *
pygame.init()

def getImage(tile):
    dictionary = {"TILE_AIR" : pygame.image.load("AirImage.png"),
                  "TILE_DIRT" : pygame.image.load("DirtImage.png"),
                  "TILE_STONE" : pygame.image.load("StoneImage.png")}

    return dictionary[tile]
