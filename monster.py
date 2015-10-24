import random

class Monster():

    def __init__(self, name="none", hp=1, acp=1, ven=0, dmg_min=0, dmg_max=1, rarity=0):
        self.hp = hp
        self.dmg_min = dmg_min
        self.dmg_max = dmg_max
        self.action_points = acp
        self.remaining_actions = acp
        self.venomous = ven
        self.name = name
        self.alive = True
        self.rarity = rarity

    def update(self):
        self.remaining_actions = self.action_points

    def defend(self):
        return -self.deal_damage()

    def flee(self):
        random.seed()
        if random.randint(1, 10) == 7:
            return 1
        else:
            return 0

    def take_damage(self, dmg):
        if dmg < 0:
            return

        self.hp -= dmg
        self.dead()

    def is_alive(self):
        return self.alive

    def dead(self):
        if self.hp <= 0:
            self.alive = False
            self.action_points = 0

    def deal_damage(self):
        random.seed()
        return random.randint(self.dmg_min, self.dmg_max)

    def get_venom(self):
        random.seed()
        return random.randint(0, self.venomous)

def get_monster(ident):
    return {"rattlesnake" : Monster(name="Rattlesnake", hp=20, ven=7, dmg_min=1, dmg_max=5, rarity=5, acp=3),
            "small_scorpion" : Monster(name="Small Scorpion", hp=5, dmg_min=1, dmg_max=2, ven=10, rarity=7),
            "big_scorpion" : Monster(name="Big Scorpion", hp=15, dmg_min=3, dmg_max=5, rarity=3, acp=5),
            "road_runner" : Monster(name="Road Runner", hp=7, rarity=6, acp=15),
            "coyote" : Monster(name="Coyote", hp=25, dmg_min=5, dmg_max=10, rarity=10, acp=7),
            "camel" : Monster(name="Camel", hp=40, dmg_min=3, dmg_max=6, rarity=2, acp=2),
            "skink" : Monster(name="Skink", hp=10, dmg_min=1, dmg_max=2, rarity=1, acp=2)}.get(ident)


