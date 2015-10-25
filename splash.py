import pygame 
import text
import config
class Splashscreen():
    def __init__(self, surface):
        self.surface = surface
        self.text_list = text.intro
        self.font = pygame.font.Font(None, 32)
        self.textRect = pygame.Rect(self.surface.get_width()/2 - 400, self.surface.get_height()/2 - 100, 400, 400)

    def draw(self):
        self.surface.fill(config.COLOR_DARKEST)
        tmp = self.textRect.copy()
        for s in text.intro: 
            fnt = self.font.render(s, 1, config.COLOR_LIGHTEST)
            self.surface.blit(fnt, tmp) 
            tmp.top += 30
            
            
