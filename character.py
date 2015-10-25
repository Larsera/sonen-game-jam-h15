import random
import pygame
import config
import text
import items
from combat_handler import combat

class Character():

    def __init__(self, image, position, screen, console):
        self.screen = screen
        src_image = pygame.image.load(image)
        # self.image = src_image.convert()
        self.image = src_image
        self.position = position
        self.health = 100
        self.poisoned = 0
        self.hunger = 100
        self.thirst = 100
        self.alive = True
        self.max_damage = 10
        self.min_damage = 5
        self.actions = 5
        self.weapon = None
        self.remaining_actions = self.actions
        self.food = []
        self.drink = []
        self.medicine = []
        self.antidote = 0
        self.turn_survd = 1
        self.console = console

        self.position = position

    def draw(self):
        x, y = self.position
        x *= config.TILE_W
        y *= config.TILE_H
        self.screen.blit(self.image, (x, y))

    def update(self, curtile):
        self.turn_survd += 1

        self.hunger -= config.HUNGER_DEC
        if curtile.shadow:
            self.thirst -= config.WATER_DEC-5
        else:
            self.thirst -= config.WATER_DEC

        if self.thirst < 0:
            self.thirst = 0

        if self.hunger < 0:
            self.hunger = 0

        if self.poisoned > 0:
            self.console.push_text("You feel your life drain away as the poison slowly courser through your veins.")
            if self.poisoned < 5:
                self.take_damage(self.poisoned, 0)
                self.poisoned = 0
            else:
                self.take_damage(config.POISON_DAMAGE, 0)
                self.poisoned -= config.POISON_DAMAGE

        if self.hunger >= 70:
            self.remaining_actions = self.actions
        elif self.hunger >= 50:
            self.remaining_actions = self.actions-1
        elif self.hunger >= 30:
            self.remaining_actions = self.actions-2
        elif self.hunger >= 15:
            self.remaining_actions = self.actions-3
        else:
            self.remaining_actions = self.actions-4

        if curtile.water_amount == -1:
            self.console.push_text("You drink from the oasis untill you feel refreshed.")
            self.thirst = 100
        elif curtile.water_amount > 0:
            self.console.push_text("You drink from the water source, trying to make it last as long as possible.")
            nw = 100 - self.thirst
            nw = nw/10
            while curtile.water_amount > 0 and nw > 0:
                self.thirst += 10
                curtile.water_amount -= 1
                nw -= 1

        for i in self.food:
            if self.hunger + i.amount <= 100:
                self.hunger += i.amount
                self.food.remove(i)
                string = "You eat " + i.name + ".";
                self.console.push_text(string)

        for i in self.drink:
            if self.thirst + i.hydration <= 100:
                self.thirst += i.hydration
                self.drink.remove(i)
                string = "You drink " + i.name + "."
                self.console.push_text(string)

        if self.thirst == 0:
            self.take_damage(20, 0)

        if not self.is_alive():
            gameover = pygame.event.Event(config.GAMEOVER)
            pygame.event.post(gameover)

    def dec_rem_act(self, amount):
        a = self.remaining_actions - amount
        if a == 0:
            newturn = pygame.event.Event(config.NEWTURN)
            pygame.event.post(newturn)
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
        if random.randint(1, 3) == 1:
            return 1
        else:
            return 0

    def move(self, direction, world, console):
        out = False
        x, y = self.position
        src = world.world[x][y]
        if direction == 'N':
            y -= 1
            if y < 0:
                y += 1
            else:
                curtile = world.get_cur_tile((x,y))
                if self.dec_rem_act(curtile.actions_used):
                    out = True
                else:
                    y += 1
        elif direction == 'S':
            y += 1
            if y > world.size_x - 1:
                y -= 1
            else:
                curtile = world.get_cur_tile((x,y))
                if self.dec_rem_act(curtile.actions_used):
                    out = True
                else:
                    y -= 1
        elif direction == 'W':
            x -= 1
            if x < 0:
                x += 1
            else:
                curtile = world.get_cur_tile((x,y))
                if self.dec_rem_act(curtile.actions_used):
                    out = True
                else:
                    x += 1
        elif direction == 'E':
            x += 1
            if x > world.size_y - 1:
                x -= 1
            else:
                curtile = world.get_cur_tile((x,y))
                if self.dec_rem_act(curtile.actions_used):
                    out = True
                else:
                    x -= 1

        if out:
            if world.world[x][y] != src:
                console.push_text(text.biome[world.world[x][y]])

            i = random.randint(0, 10)
            if i == 10:
                console.push_text(text.flavor[random.randint(0, 7)])
            elif i == 7:
                self.found_danger(curtile)


        self.position = x, y
        self.draw()

        return out
            

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
        if tile.searches_left == 0: 
            self.console.push_text("There is nothing left to find here")
            return
        else:
            self.dec_rem_act(1)
            tile.searches_left -= 1
        random.seed()

        chance = random.randint(0, 100)


        if not tile.shadow and chance >= 100 - tile.shadow_chance*10:
            tile.found_shadow()
            self.console.push_text("You found shade!")
            chance -= config.CHANCE_DEC

        if tile.water_amount != -1 and chance >= 100 - tile.water_chance*10:
            self.found_water(tile)
            self.console.push_text("You found a source of water!")
            chance -= config.CHANCE_DEC

        if chance >= 100 - tile.item_chance*10:
            self.found_item(tile)
            chance -= config.CHANCE_DEC

        if chance >= 100 - tile.danger_chance*10:
            self.found_danger(tile)
            chance -= config.CHANCE_DEC

    def find_food(self, foodstuff):
        string = "You found some " + foodstuff.name + "."
        self.console.push_text(string)
        self.food.append(foodstuff)

    def find_drink(self, hydration):
        string = "You found some " + hydration.name + "."
        self.console.push_text(string)
        self.drink.append(hydration)

    def find_medicine(self, medication):
        if medication.antidote:
            self.antidote += 1
        else:
            self.medicine.append(medication)

    def find_weapon(self, weapon):
        if self.weapon == None or self.weapon.dmg < weapon.dmg:
            self.console.push_text(text.item[weapon.name])
            self.weapon = weapon
        else:
            self.console.push_text("You found a potential weapon, but the one you have is better.")


    def found_danger(self, tile):
        combatevent = pygame.event.Event(config.COMBAT)
        pygame.event.post(combatevent)

    def found_water(self, tile):
        random.seed()
        if tile.water_chance < 10:
            tile.water_amount = random.randint(1, tile.water_chance)
        else:
            tile.water_amount -= 1

#TODO: if time rewrite
    def found_item(self, tile):
        random.seed()
        result = random.randint(1, 4)
        if result == 1:
            food = tile.get_foodstuff()
            string = "You found a " + food.name + "."
            self.console.push_text(string)
            self.find_food(food)
        elif result == 2:
            hydration = tile.get_hydration()
            string = "You found a " + hydration.name + "."
            self.console.push_text(string)
            self.find_drink(hydration)
        elif result == 3:
            medicine = tile.get_medicine()
            string = "You found some " + medicine.name + "."
            self.console.push_text(string)
            self.find_medicine(medicine)
        elif result == 4:
            weapon = tile.get_weapon()
            self.find_weapon(weapon)

    def use_antidote(self):
        if self.antidote > 0:
            self.antidote -= 1
            if self.poisoned > 0:
                self.console.push_text("After drinking some antidote your body starts to feel a little better.")
                if self.poisoned < config.ANTIDOTE_EFFECT:
                    self.poisoned = 0
                else:
                    self.poisoned -= config.ANTIDOTE_EFFECT
            else:
                self.console.push_text("The only effect of drinking some antidote is that your stomach feels sligthly off.")

