import random
import pygame
import config
import combat_handler
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
        self.screen.blit(self.image, (x, y))

    def update(self, curtile):
        self.remaining_actions = self.actions

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

    def dec_rem_act(self, amount):
        a = self.remaining_actions - amount
        if a == 0:
            pygame.event.post(pygame.USEREVENT, {1 : "newturn"})
        elif a > 0:
            self.remaining_actions = a
        else:
            return False

        return True


    def defend(self):
        self.dec_rem_act(1)
        return -self.deal_damage()

    def flee(self):
        self.dec_rem_act(1)
        random.seed()
        if random.randint(1, 10) == 7:
            return 1
        else:
            return 0

    def move(self, direction, curtile):
        if self.dec_rem_act(curtile.actions_used):
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
            self.draw()
            return True

        else:
            return False
            

    def take_damage(self, dmg, poison):
        if poison > 0:
            self.poisoned += poison

        if dmg < 0:
            return

        self.health -= dmg

        if self.health <= 0:
            self.alive = False

    def deal_damage(self):
        self.dec_rem_act(1)
        random.seed()
        return random.randint(self.min_damage, self.max_damage)

    def is_alive(self):
        return self.alive

    def get_actions(self):
        return self.remaining_actions

    def search(self, tile):
        random.seed()
        chance = random.randint(0, 100)

        if chance >= 100 - tile.shadow_chance*10:
            tile.found_shadow()
            chance -= config.CHANCE_DEC

        if chance >= 100 - tile.water_chance*10:
            found_water()
            chance -= config.CHANCE_DEC

        if chance >= 100 - tile.item_chance*10:
            found_item()
            chance -= config.CHANCE_DEC

        if chance >= 100 - tile.danger_chance:
            self.found_danger(tile)
            chance -= config.CHANCE_DEC

    def find_food(self, foodstuff):
        self.food.append(foodstuff)

    def find_drink(self, hydration):
        self.drink.append(hydration)

    def find_medicine(self, medication):
        self.medicine.append(medication)

    def found_danger(self, tile):
        pygame.event.post(pygame.USEREVENT, {1 :"combat"})
        combat(self, tile.get_monster)

