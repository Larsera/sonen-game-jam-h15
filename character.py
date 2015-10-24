import random
import pygame
import config
from pygame.locals import *
from pygame import Rect

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
        self.max_damage = 10
        self.min_damage = 5
        self.actions = 5
        self.weapom = None
        self.remaining_actions = self.actions
        self.food = []
        self.drink = []
        self.medicine = []

        self.position = position

    def draw(self):
        x, y = self.position
        x *= config.TILE_W
        y *= config.TILE_H
        self.screen.blit(self.image, x, y)

    def update(self):
        self.position = self.position

        for i in self.food:
            if self.hunger + i.amount <= 100:
                self.hunger += i.amount
                self.food.remove(i)

        for i in self.drink:
            if self.thirst + i.hdr <= 100:
                self.thirst += i.hdr
                self.drink.remove(i)

        if self.hunger <= 0: self.alive = False
        if self.thirst <= 0: self.alive = False
        if self.health <= 0: self.alive = False

    def defend(self):
        return -self.deal_damage()

    def flee(self):
        random.seed()
        if random.randint(1, 10) == 7:
            return 1
        else:
            return 0

    def move(self, direction):
        x, y = self.position
        if direction == 'N':
            x -= 1
        elif direction == 'S':
            x += 1
        elif direction == 'w':
            y -= 1
        elif direction == 'E':
            y += 1

        self.position = x, y
            

    def take_damage(self, dmg, poison):
        if poison > 0:
            self.poisoned += poison

        if dmg < 0:
            return

        self.health -= dmg

        if self.health <= 0:
            self.alive = False

    def deal_damage(self):
        random.seed()
        return random.randint(self.min_damage, self.max_damage)

    def is_alive(self):
        return self.alive

    def get_actions(self):
        return self.remaining_actions

    def search(self, tile):
        random.seed()
        chance = random.randint(0, 100)

        if chance + tile.shadow_chance >= 50:
            found_shadow()
            chance -= config.CHANCE_DEC

        if chance + tile.water_chance >= 75:
            found_water()
            chance -= config.CHANCE_DEC

        if chance + tile.item_chance >= 90:
            found_item()
            chance -= config.CHANCE_DEC

        if chance + tile.danger_chance >= 60:
            found_danger()
            chance -= config.CHANCE_DEC

    def find_food(self, foodstuff):
        self.food.append(foodstuff)

    def find_drink(self, hydration):
        self.drink.append(hydration)

    def find_medicine(self, medication):
        self.medicine.append(medication)

    #def found_danger(self):
        
