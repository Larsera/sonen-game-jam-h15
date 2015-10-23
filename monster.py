
class Monster(self):

    def __init__(self, (hp, dmg, acp, ven), name):
        self.hp = hp
        self.damage = dmg
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
