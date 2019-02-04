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

dirtImage = pygame.image.load("DirtImage.png")
stoneImage = pygame.image.load("StoneImage.png")

world = WorldGeneration.generateWorld()
