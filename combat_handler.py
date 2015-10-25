import pygame
from monster import Monster
import config
import text

class combat():

    def __init__(self, char, mon, console):
        self.char = char
        self.mon = mon
        self.console = console
        console.push_text(text.monster[self.mon.name])

    def do_combat_turn(self, cmd):
        if self.combat_turn(cmd):
            endcombat = pygame.event.Event(config.ENDCOMBAT)
            pygame.event.post(endcombat)
        elif not self.char.is_alive():
            gameover = pygame.event.Event(config.GAMEOVER)
            pygame.event.post(gameover)
        elif not self.mon.is_alive():
            string = "You defeated the " + self.mon.name + "!"
            self.console.push_text(string)
            win = pygame.event.Event(config.WIN)
            pygame.event.post(win)
        else:
            if self.char.remaining_actions == 0:
                while not self.mon.remaining_actions == 0:
                    self.combat_turn(0)

                newturn = pygame.event.Event(config.NEWTURN)
                pygame.event.post(newturn)
                self.mon.update()


    def combat_turn(self, cmd):
        if self.char.remaining_actions > 0 and cmd > 0:
            char_damage = self.do_action(cmd, self.char)
        else:
            char_damage = 0
        if self.mon.remaining_actions > 0:
            mon_damage = self.do_action(self.mon.get_action(), self.mon)
        else:
            mon_damage = 0

        if char_damage == 1:
            if self.char.flee():
                self.console.push_text("You flee from the fight!")
                return True
        elif char_damage < 0 and mon_damage > 1:
            string = "The " + self.mon.name + " hits you for " + str(mon_damage-2+char_damage) + " damage."
            self.console.push_text(string)
            self.char.take_damage(mon_damage-2+char_damage, self.mon.get_venom())
        elif char_damage < 0 and mon_damage < 0:
            string = "You lock eyes with the " + self.mon.name + ". Neiher of you makes a move."
            self.console.push_text(string)
        elif char_damage == 0:
            if mon_damage == 1:
                string = "You stand still, watching as the  " + self.mon.name + " saunters off."
                self.console.push_text(string)
                return True
            elif mon_damage == 0:
                string = "Both you and the " + self.mon.name + " look strangly at each other's laughable attempt to escape."
                self.console.push_text(string)
            elif mon_damage > 0:
                string = "The " + self.mon.name + " looks on as you stumble around trying to escape."
                self.console.push_text(string)
            else:
                string = "While you try to escape, the " + self.mon.name + " hits you for " + str(mon_damage-2) + " damage."
                venom = self.mon.get_venom()
                self.char.take_damage(mon_damage-2, venom)
                if venom > 0:
                    self.console.push_text("You've been poisoned!")
        elif char_damage > 1:
            if mon_damage == 1:
                if self.mon.flee():
                    string = "The " + self.mon.name + " fled!"
                    self.console.push_text(string)
                    return True
            elif mon_damage < 0:
                a = char_damage-2+mon_damage
                if a > 0:
                    a = 0
                string = "You hit the " + self.mon.name + " for " + str(a) + " damage."
                self.console.push_text(string)
                self.mon.take_damage(a)
            elif mon_damage == 0:
                string = "You hit the " + self.mon.name + " for " + str(char_damage-2) + " damage, while it tries to run away. "
                self.console.push_text(string)
                self.mon.take_damage(char_damage-2)
            else:
                string = "You hit the " + self.mon.name + " for " + str(char_damage-2) + " damage."
                self.console.push_text(string)
                self.mon.take_damage(char_damage-2)
                string = "The " + self.mon.name + " hits you for " + str(mon_damage-2) + " damage."
                self.console.push_text(string)
                venom = self.mon.get_venom()
                self.char.take_damage(mon_damage-2, venom)
                if venom > 0:
                    self.console.push_text("You've been poisoned!")

        return False

    def do_action(self, action, actor):
        if action == 1:
            return actor.deal_damage() + 2
        elif action == 2:
            return actor.defend()
        elif action == 3:
            return actor.flee()

