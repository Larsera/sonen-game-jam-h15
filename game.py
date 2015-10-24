import pygame, math, sys, os
from pygame.locals import *
from world import *
from character import *
from gui import *

pygame.init()
_screen = pygame.display.set_mode((1366, 768))
# This is the surface we are rendering to
screen = pygame.Surface(_screen.get_size())
clock = pygame.time.Clock()

TILE_WIDTH = 32
TILE_HEIGHT = 32
TILE_GRID_WIDTH = screen.get_width()/TILE_WIDTH
TILE_GRID_HEIGHT = screen.get_height()/TILE_HEIGHT

class EventController():
    def handleEvents(self):
        event_list = pygame.event.get() 

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                clicked_pos = pygame.mouse.get_pos()
                # TODO: Check for event collision and handle
            if event.type == pygame.KEYUP:
                pygame.quit()

class Block(pygame.sprite.Sprite):
    def __init__(self, image, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.image = self.src_image.convert()

events = EventController()
world = World(TILE_GRID_HEIGHT, TILE_GRID_WIDTH, os.path.join('img', 'testgrid.png'), screen)
character = Character(os.path.join('img', 'character.png'), (10, 10), screen)

sidebar = Sidebar(screen, os.path.join('img', 'tileset_old.jpg')) 
button = Button(sidebar, 1, os.path.join('img', 'tileset.png'), "Attack")
button2 = Button(sidebar, 2, os.path.join('img', 'tileset_old.jpg'), "Research")
button3 = Button(sidebar, 3, os.path.join('img', 'tileset_old.jpg'), "DIE!")
stats = Button(sidebar, 3, os.path.join('img', 'tileset_old.jpg'), "DIE!")
running = 1
while running:
    screen.fill((255, 204, 102)) 
    events.handleEvents()
    character.update()
    world.draw()
    sidebar.draw()
    button.draw()
    button2.draw()
    button3.draw()
    # character.draw()
    sidebar.blit()
    _screen.blit(screen, (0,0))
    pygame.display.flip()

pygame.quit()
