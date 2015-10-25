import pygame
from monster import Monster
import config
import text

class combat():

    def __init__(self, char, mon, console):
        self.char = char
        self.mon = mon
        self.console = console
        print "MONSTER? ",
        print(type(mon))
        console.push_text(text.monster[self.mon.name])

    def do_combat_turn(self, cmd):
        if self.combat_turn(cmd):
            endcombat = pygame.event.Event(config.ENDCOMBAT)
            pygame.event.post(endcombat)
        elif not self.char.is_alive():
            gameover = pygame.event.Event(config.GAMEOVER)
            pygame.event.post(gameover)
        elif not self.mon.is_alive():
            win = pygame.event.Event(config.WIN)
            pygame.event.post(win)
        else:
            if self.char.remaining_actions == 0 and self.mon.remaining_actions == 0:
                newturn = pygame.event.Event(config.NEWTURN)
                pygame.event.post(newturn)
                self.mon.update()


    def combat_turn(self, cmd):
        if self.char.action_points_left > 0:
            char_damage = self.do_action(cmd, self.char)
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
                self.char.take_damage(mon_damage-2, self.mon.get_venom())

        return False

    def do_action(self, action, actor):
        if action == 1:
            return actor.deal_damage() + 2
        elif action == 2:
            return actor.defend()
        elif action == 3:
            return actor.flee()

