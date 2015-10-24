import os, sys, pygame

# class Gui():
#     gui_event_handler = 0
     
#     def __init__ (self, surface):
#         self.surface = surface

#     def set_background(self, background):
#         self.background = background

class Sidebar():
     
    def __init__(self, surface, place_x, place_y, size_x, size_y):
        self.color = (255, 128, 64)
        self.parent_surface = surface
        self.surface = pygame.Surface((size_x,size_y))
        self.place = (place_x, place_y)
        self.rect = (0, 0, size_x, size_y)


    def draw(self):
        # sidebar_rect = self.background.get_rect()
        pygame.draw.rect(self.surface, self.color, self.rect, 5)
        self.parent_surface.blit(self.surface, self.place)

class Button():

    def __init__(self, gui):
        self.gui = gui
    
    # def draw(
