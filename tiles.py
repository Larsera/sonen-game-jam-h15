import random
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
    def __init__(self, (au, dc, sc, ic, wc), name, monster_list):
        self.monster_dict = {}
        self.tot_monster_chance = 0
        self.actions_used = au
        self.danger_chance = dc
        self.shadow_chance = sc
        self.item_chance = ic
        self.water_chance = wc
        self.name = name
        self.create_monster_id_dict(monster_list)

    def get_monster(self, min_chance=1):
        random.seed()
        c = random.randint(min_chance, self.tot_monster_chance)
        return self.monster_dict[c]

    def create_monster_id_dict(self, monster_list):
        for c, m in monster_list:
            cnt = 1
            while cnt < c:
                self.monster_dict[self.tot_monster_chance + cnt] = m
                cnt += 1

            self.tot_monster_chance += c

# TODO: real values
def get_tile(ident, monster_list=[(0, Monster())]):
    return {0 : Tile((0, 0, 0, 0, 0, 0), "empty desert", monster_list),
            1 : Tile((0, 0, 0, 0, 0, 0), "big rock", monster_list),
            2 : Tile((0, 0, 0, 0, 0, 0), "small rock", monster_list),
            3 : Tile((0, 0, 0, 0, 0, 0), "jagged rock", monster_list),
            4 : Tile((0, 0, 0, 0, 0, 0), "oasis", monster_list),
            5 : Tile((0, 0, 0, 0, 0, 0), "abandoned camp", monster_list),
            6 : Tile((0, 0, 0, 0, 0, 0), "pyramid", monster_list)}[ident]
