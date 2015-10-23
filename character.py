import random
import pygame
from pygame.locals import *
from pygame import Rect

CHANCE_DEC = 20

class Character():

    def __init__(self, image, position, screen):
        self.screen = screen
        src_image = pygame.image.load(image)
        self.image = src_image.convert()

        self.position = position
    
    def draw(self):
        self.screen.blit(self.image, position)

    def update(self):
        self.position = self.position

    def move(self, direction):
        self.position = (0,0)

    def search(self, tile):
        random.seed()
        chance = random.randint(0, 100)

        if chance + tile.shadow_chance >= 50:
            found_shadow()
            chance -= CHANCE_DEC

        if chance + tile.water_chance >= 75:
            found_water()
            chance -= CHANCE_DEC

        if chance + tile.item_chance >= 90:
            found_item()
            chance -= CHANCE_DEC

        if chance + tile.danger_chance >= 60:
            found_danger()
            chance -= CHANCE_DEC

    # def update():


