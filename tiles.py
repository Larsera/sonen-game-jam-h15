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
#min_monster_chance: higher = less chance of monster
    def __init__(self, (au, dc, sc, ic, wc), name, monster_list, min_monster_chance=0):
        self.monster_dict = {}
        self.tot_monster_chance = min_monster_chance
        self.actions_used = au
        self.danger_chance = dc
        self.shadow_chance = sc
        self.item_chance = ic
        self.water_chance = wc
        self.name = name
        self.create_monster_id_dict(monster_list)

    def get_monster(self):
        random.seed()
        c = random.randint(1, self.tot_monster_chance)
        return self.monster_dict.get(c)

    def create_monster_id_dict(self, monster_list):
        for c, m in monster_list:
            cnt = 0
            while cnt < c:
                cnt += 1
                self.monster_dict[self.tot_monster_chance + cnt] = m

            self.tot_monster_chance += c

    def get_tile(self, ident, monster_list=[(1, Monster())]):
        return {0 : Tile((1, 3, 2, 2, 1), "empty desert", monster_list),
                1 : Tile((2, 5, 10, 3, 2), "big rock", monster_list),
                2 : Tile((2, 4, 5, 3, 3), "small rock", monster_list),
                3 : Tile((3, 2, 3, 1, 3), "jagged rock", monster_list),
                4 : Tile((1, 7, 7, 4, 10), "oasis", monster_list),
                5 : Tile((1, 4, 8, 7, 5), "abandoned camp", monster_list),
                6 : Tile((1, 10, 10, 9, 4), "pyramid", monster_list)}.get(ident)


