from character import Character
from monster import Monster

class combat():

    def __init__(self, char, mon):
        self.char = char
        self.mon = mon

        while not self.combat_turn:
            if not self.char.is_alive() or not self.mon.is_alive():
                break

    def combat_turn(self):
        if self.char.action_points_left > 0:
            char_damage = self.do_action(self.char.get_action, self.char)
        else:
            char_damage = 0
        if self.mon.action_points_left > 0:
            mon_damage = self.do_action(self.mon.get_action, self.mon)
        else:
            mon_damage = 0

        if char_damage == 1:
            if self.char.flee():
                return True
        elif char_damage < 0 and mon_damage > 0:
            self.char.take_damage(mon_damage-2+char_damage)
        elif char_damage > 1:
            if mon_damage == 1:
                if self.mon.flee():
                    return True
            elif mon_damage < 0:
                self.mon.take_damage(char_damage-2+mon_damage)
            elif mon_damage > 1:
                self.mon.take_damage(char_damage-2)
                self.char.take_damage(mon_damage-2, self.mon.get_venom)

        return False

    def do_action(self, action, actor):
        if action == 1:
            return actor.deal_damage() + 2
        elif action == 2:
            return actor.defend()
        elif action == 3:
            return actor.flee()

