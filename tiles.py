import random
import config
from monster import Monster


class Tile():

#ac = self.actions_used = how many actions points used to move to tile
#dc = self.danger_chance = danger chance modifier
#sc = self.shadow_chance = shadow chance modifier
#ic = self.item_chance = item chance modifier
#wc = self.water_chance = water chance modifier
#monster_list = list of tuples (c, m)
#c = chance
#m = monster
#min_monster_chance: higher = less chance of monster
    def __init__(self, (au, dc, sc, ic, wc), name, (monster_list, food_list, hydration_list, weapon_list, medicine_list), min_monster_chance=0, searches_left=3):
        self.monster_dict = {}
        self.hydration_dict = {}
        self.foodstuff_dict = {}
        self.weapon_dict = {}
        self.medicine_dict = {}
        self.tot_monster_chance = min_monster_chance
        self.tot_hydration_chance = 0
        self.tot_foodstuff_chance = 0
        self.tot_weapon_chance = 0
        self.tot_medicine_chance = 0
        self.actions_used = au
        self.danger_chance = dc
        self.shadow_chance = sc
        self.shadow = False
        self.item_chance = ic
        self.water_chance = wc
        self.water_amount = 0
        self.name = name
        self.searches_left = searches_left
        self.create_monster_id_dict(create_touples(monster_list, dc))
        self.create_hydration_id_dict(create_touples(hydration_list, ic))
        self.create_foodstuff_id_dict(create_touples(food_list, ic))
        self.create_medicine_id_dict(create_touples(medicine_list, ic))
        self.create_weapon_id_dict(create_touples(weapon_list, ic))

    def get_monster(self):
        random.seed()
        c = random.randint(1, self.tot_monster_chance)
        return self.monster_dict.get(c)

    def get_hydration(self):
        random.seed()
        c = random.randint(1, self.tot_hydration_chance)
        return self.hydration_dict.get(c)

    def get_foodstuff(self):
        random.seed()
        c = random.randint(1, self.tot_foodstuff_chance)
        return self.foodstuff_dict.get(c)

    def get_medicine(self):
        random.seed()
        c = random.randint(1, self.tot_medicine_chance)
        return self.medicine_dict.get(c)

    def get_weapon(self):
        random.seed()
        c = random.randint(1, self.tot_weapon_chance)
        return self.weapon_dict.get(c)

    def create_monster_id_dict(self, monster_list):
        for c, m in monster_list:
            while c >  0:
                c -= 1
                self.tot_monster_chance += 1
                self.monster_dict[self.tot_monster_chance] = m

    def create_hydration_id_dict(self, hydration_list):
        for c, h in hydration_list:
            while c > 0:
                c -= 1
                self.tot_hydration_chance += 1
                self.hydration_dict[self.tot_hydration_chance] = h

    def create_foodstuff_id_dict(self, foodstuff_list):
        for c, h in foodstuff_list:
            while c > 0:
                c -= 1
                self.tot_foodstuff_chance += 1
                self.foodstuff_dict[self.tot_foodstuff_chance] = h

    def create_medicine_id_dict(self, medicine_list):
        for c, h in medicine_list:
            while c > 0:
                c -= 1
                self.tot_medicine_chance += 1
                self.medicine_dict[self.tot_medicine_chance] = h

    def create_weapon_id_dict(self, weapon_list):
        for c, h in weapon_list:
            while c > 0:
                c -= 1
                self.tot_weapon_chance += 1
                self.weapon_dict[self.tot_weapon_chance] = h

    def found_shadow(self):
        self.shadow = True

def get_tile(ident, monster_list=config.DEFAULT_MONSTER_LIST, food_list=config.DEFAULT_FOOD_LIST, hydration_list=config.DEFAULT_HYDRATION_LIST, medicine_list=config.DEFAULT_MEDICINE_LIST, weapon_list=config.DEFAULT_WEAPON_LIST):
    return {0 : Tile((1, 3, 2, 2, 1), "empty desert", (monster_list, food_list, hydration_list, weapon_list, medicine_list)),
            1 : Tile((2, 5, 10, 3, 2), "big rock", (monster_list, food_list, hydration_list, weapon_list, medicine_list), searches_left=4),
            2 : Tile((2, 4, 5, 3, 3), "small rock", (monster_list, food_list, hydration_list, weapon_list, medicine_list), searches_left=4),
            3 : Tile((3, 2, 3, 1, 3), "jagged rock", (monster_list, food_list, hydration_list, weapon_list, medicine_list)),
            4 : Tile((1, 7, 7, 4, 10), "oasis", (config.OASIS_MONSTER_LIST, food_list, hydration_list, weapon_list, medicine_list), searches_left=5),
            5 : Tile((1, 4, 8, 7, 5), "abandoned camp", (monster_list, config.CAMP_FOOD_LIST, hydration_list, config.CAMP_WEAPON_LIST, medicine_list), searches_left=10),
            6 : Tile((1, 10, 10, 9, 4), "pyramid", (monster_list, food_list, hydration_list, weapon_list, medicine_list), searches_left=7)}.get(ident)


def create_touples(curlist, mod):
    out = []
    random.seed()
    for item in curlist:
        print item.name
        ant = random.randint(0, 10)
        if ant > item.rarity - mod:
            out.append((11 - ant, item))

    return out

