
class Monster(self):

    def __init__(self, name="none", hp=1, acp=1, ven=False, dmg_min=0, dmg_max=0):
        self.hp = hp
        self.damage = range(dmg_min, dmg_max)
        self.action_points = acp
        self.venomous = ven
        self.name = name
        self.alive = True


    def take_damage(self, dmg):
        self.hp -= dmg

    def is_alive(self):
        return self.alive

    def dead(self):
        if hp <= 0:
            self.alive = False
            self.action_points = 0

        return not self.alive
