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
	self.health = 100
	self.poisoned = 0
        self.hunger = 100
        self.thirst = 100
        self.alive = True
        self.damage = 10

        self.position = position
    
    def draw(self):
        self.screen.blit(self.image, self.position)

    def update(self):
        self.position = self.position

    # def move(self, direction):
    #     # TEST

    def take_damage(self, dmg, poison):
        if poison == True:
            self.poisoned = self.poisoned + 1

        self.health -= dmg

        if self.health <= 0:
            self.alive = False

    def deal_damage(self, creature):
        creature.take_damage(self.damage)

    def is_alive(self):
        return self.alive


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


