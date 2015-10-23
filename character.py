import pygame
from pygame.locals import *
from pygame import Rect

class Character():

    def __init__(self, image, position, screen):
        self.screen = screen
        self.src_image = pygame.image.load(image)
        self.image = src_image.convert()

        self.position = position
    
    def draw(self):
        self.screen.blit(self.image, position)

    def move(direction):
        self.position = (0,0)

    # def update():


