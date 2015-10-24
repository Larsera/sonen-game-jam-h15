from character import Character
from monster import Monster

class combat():

    def __init__(self, char, mon):
        self.char = char
        self.mon = mon

    def combat_turn(self):
        char_action = char.get_action()
        mon_action = mon.get_action()

    def do_action(self, action, actor):
        if action == 1:
            return actor.deal_damage(self)

