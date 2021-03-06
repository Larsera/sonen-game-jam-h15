import pygame 
import text
import config
class Splashscreen():
    def __init__(self, surface):
        self.surface = surface
        self.text_list = text.intro
        self.font = pygame.font.Font(None, 32)
        self.font_l = pygame.font.Font(None, 22)
        self.font_go = pygame.font.Font(None, 92)
        self.textRect = pygame.Rect(self.surface.get_width()/2 - 400, self.surface.get_height()/2 - 100, 400, 400)

    def draw(self):
        self.surface.fill(config.COLOR_DARKEST)
        tmp = self.textRect.copy()
        for s in text.intro: 
            fnt = self.font.render(s, 1, config.COLOR_LIGHTEST)
            self.surface.blit(fnt, tmp) 
            tmp.top += 30

        tmp.top += 100
        tmp.left = self.surface.get_width()/2 - 100
        fnt = self.font_l.render("Press a key to start", 1, config.COLOR_LIGHT)
        self.surface.blit(fnt, tmp) 
    def game_over(self):
        self.surface.fill(config.COLOR_DARKEST)
        fnt = self.font_go.render("GAME OVER", 1, config.COLOR_LIGHTEST)
        self.textRect.left = self.surface.get_width()/2 - 210
        self.surface.blit(fnt, self.textRect) 
