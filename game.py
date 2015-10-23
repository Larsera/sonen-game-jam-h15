import pygame, math, sys
from pygame.locals import *

screen = pygame.display.set_mode((1366, 768))
clock = pygame.time.Clock()

class WorldMap():
    def __init__(self, image):
        self.src_image = pygame.image.load(image)
        self.image = self.src_image.convert()

class EventController():
    def handleEvents(self):
        event_list = pygame.event.get() 

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                clicked_pos = pygame.mouse.get_pos()

                # TODO: Check for event collision and handle

class Block(pygame.sprite.Sprite):
    def __init__(self, image, width, height):
        pygame.sprrite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.image = self.src_image.convert()

# TODO: Game loop
