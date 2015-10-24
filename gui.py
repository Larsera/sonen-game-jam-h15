import os, sys, pygame
import config

# class Gui():
#     gui_event_handler = 0
     
#     def __init__ (self, surface):
#         self.surface = surface

#     def set_background(self, background):
#         self.background = background

class Sidebar():
     
    def __init__(self, surface, image):
        self.color = (255, 128, 64)
        self.parent_surface = surface
        src_image = pygame.image.load(image)
        self.image = src_image.convert()

        self.left = surface.get_width() - config.SIDEBAR_WIDTH
        self.top = 0
        self.width = config.SIDEBAR_WIDTH
        self.height = surface.get_height()

        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.surface = pygame.Surface((self.left, self.height))
        self.place = (self.left, self.top)
        self.rect = (0, self.top, self.width, self.height)

    def draw(self):
        # sidebar_rect = self.background.get_rect()
        self.surface.blit(self.image, (0,0))
        pygame.draw.rect(self.surface, self.color, self.rect, config.SIDEBAR_OUTLINE)
    def get_surface(self):
        return self.surface

    def blit(self):
        self.parent_surface.blit(self.surface, self.place)

class Button():

    def __init__(self, element, position, image, text):
        self.surface = element.get_surface()
        self.rect = pygame.Rect(config.SIDEBAR_PADDING, position * config.SIDEBAR_UNIT_HEIGHT + (position*config.SIDEBAR_PADDING), config.SIDEBAR_WIDTH - (2*config.SIDEBAR_PADDING), config.BUTTON_HEIGHT) 

        src_image = pygame.image.load(image)
        self.image = src_image.convert()
        self.image = pygame.transform.scale(self.image, (config.SIDEBAR_WIDTH - (2*config.SIDEBAR_PADDING), config.BUTTON_HEIGHT))

        self.font = pygame.font.Font(None, 32)
        self.text = self.font.render(text, 1,(255,255,255))

    def draw(self):
        pygame.draw.rect(self.surface, (255,255,255), self.rect, config.BUTTON_OUTLINE)
        self.surface.blit(self.image, self.rect)
        self.surface.blit(self.text, self.rect)


class Stats():

    def __init__(self, element, position, image, character):
        self.surface = element.get_surface()
        self.rect = (config.SIDEBAR_PADDING, position * config.SIDEBAR_UNIT_HEIGHT + (position*config.SIDEBAR_PADDING), config.SIDEBAR_WIDTH - (2*config.SIDEBAR_PADDING), config.STATS_HEIGHT) 

        src_image = pygame.image.load(image)
        self.image = src_image.convert()
        self.image = pygame.transform.scale(self.image, (config.SIDEBAR_WIDTH - (2*config.SIDEBAR_PADDING), config.STATS_HEIGHT))

        self.font = pygame.font.Font(None, 32)
        self.text_health = self.font.render("Health:    " + str(character.health), 1,(255,255,255))
        self.text_thirst = self.font.render("Hydration: " + str(character.thirst), 1,(255,255,255))
        self.text_hunger = self.font.render("Hunger:    " + str(character.hunger), 1,(255,255,255))

    def draw(self):
        pygame.draw.rect(self.surface, (255,255,255), self.rect, config.STATS_OUTLINE)
        self.surface.blit(self.image, self.rect)
        tmp = pygame.Rect(self.rect)
        self.surface.blit(self.text_health, tmp)
        tmp.top += config.TEXT_PADDING
        self.surface.blit(self.text_thirst, tmp)
        tmp.top += config.TEXT_PADDING
        self.surface.blit(self.text_hunger, tmp)

class DirectionButtons():
    def __init__(self, surface, x, y, image):
        self.surface = surface
        src_image = pygame.image.load(image)
        self.image = src_image.convert()
        z = config.DIRBTN_SIZE
        p = config.DIRBTN_PADDING
        self.n_rect = pygame.Rect(x + z + p, y, z, z)
        self.w_rect = pygame.Rect(x, y + z + p, z, z)
        self.s_rect = pygame.Rect(x + z + p, y + (z * 2) + p, z, z)
        self.e_rect = pygame.Rect(x + (z * 2) + (2 * p), y + z + p, z, z)

    def draw(self):
        pygame.draw.rect(self.surface, (255,255,255), self.n_rect, config.DIRBTN_OUTLINE)
        pygame.draw.rect(self.surface, (255,255,255), self.w_rect, config.DIRBTN_OUTLINE)
        pygame.draw.rect(self.surface, (255,255,255), self.s_rect, config.DIRBTN_OUTLINE)
        pygame.draw.rect(self.surface, (255,255,255), self.e_rect, config.DIRBTN_OUTLINE)
        

class Downbar():
    def __init__(self, surface, image):
        self.color = (255, 128, 64)
        self.parent_surface = surface
        src_image = pygame.image.load(image)
        self.image = src_image.convert()

        self.left = 0
        self.top = self.parent_surface.get_height() - config.DOWNBAR_HEIGHT 
        self.width = self.parent_surface.get_width()
        self.height = config.DOWNBAR_HEIGHT

        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.surface = pygame.Surface((self.width, self.height))
        self.place = (self.left, self.top)
        self.rect = (0, 0, self.width, self.height)
        print "Left: ", self.left, "Top: ", self.top, "Width: ", self.width, "Height: ", self.height

    def draw(self):
        self.surface.blit(self.image, (0,0))
        pygame.draw.rect(self.surface, self.color, self.rect, config.BUTTON_PADDING)
    def get_surface(self):
        return self.surface

    def blit(self):
        self.parent_surface.blit(self.surface, self.place)

