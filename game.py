import pygame, math, sys
from pygame.locals import *

screen = pygame.display.set_mode((1366, 768))
clock = pygame.time.Clock()

class WorldMap():
    def __init__(self, image):
        self.src_image = pygame.image.load(image)

background = pygame.image.load('bg.png')
