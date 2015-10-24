import os, sys, pygame

SIDEBAR_WIDTH = 250
# class Gui():
#     gui_event_handler = 0
     
#     def __init__ (self, surface):
#         self.surface = surface

#     def set_background(self, background):
#         self.background = background

class Sidebar():
     
    def __init__(self, surface):
        self.color = (255, 128, 64)
        self.parent_surface = surface

        self.left = surface.get_width() - SIDEBAR_WIDTH
        self.top = 0
        self.width = SIDEBAR_WIDTH
        self.height = surface.get_height()

        self.surface = pygame.Surface((self.left, self.height))
        self.place = (self.left, self.top)
        self.rect = (0, 0, self.width, self.height)

    def draw(self):
        # sidebar_rect = self.background.get_rect()
        pygame.draw.rect(self.surface, self.color, self.rect, 7)
        self.parent_surface.blit(self.surface, self.place)

class Button():

    def __init__(self, gui):
        self.gui = gui
    
    # def draw(
