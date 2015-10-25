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
    def __init__(self, (au, dc, sc, ic, wc), name, monster_list, min_monster_chance=0, searches_left=3):
        self.monster_dict = {}
        self.tot_monster_chance = min_monster_chance
        self.actions_used = au
        self.danger_chance = dc
        self.shadow_chance = sc
        self.shadow = False
        self.item_chance = ic
        self.water_chance = wc
        self.water_amount = 0
        self.name = name
        self.searches_left = searches_left
        self.create_monster_id_dict(create_monster_touples(monster_list, dc))

    def get_monster(self):
        random.seed()
        c = random.randint(1, self.tot_monster_chance)
        print self.monster_dict.get(c).name
        return self.monster_dict.get(c)

    def create_monster_id_dict(self, monster_list):
        for c, m in monster_list:
            while c >  0:
                c -= 1
                self.tot_monster_chance += 1
                self.monster_dict[self.tot_monster_chance] = m

    def found_shadow(self):
        self.shadow = True


def get_tile(ident, monster_list=config.DEFAULT_MONSTER_LIST):
    return {0 : Tile((1, 3, 2, 2, 1), "empty desert", monster_list),
            1 : Tile((2, 5, 10, 3, 2), "big rock", monster_list, searches_left=4),
            2 : Tile((2, 4, 5, 3, 3), "small rock", monster_list, searches_left=4),
            3 : Tile((3, 2, 3, 1, 3), "jagged rock", monster_list),
            4 : Tile((1, 7, 7, 4, 10), "oasis", monster_list, searches_left=5),
            5 : Tile((1, 4, 8, 7, 5), "abandoned camp", monster_list, searches_left=10),
            6 : Tile((1, 10, 10, 9, 4), "pyramid", monster_list, searches_left=7)}.get(ident)


def create_monster_touples(monster_list, d):
    ml = []
    random.seed()
    for mon in monster_list:
        ant = random.randint(0, 10)
        if ant > mon.rarity - d:
            ml.append((11 - ant, mon))

    return ml

