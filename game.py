import pygame, math, sys, os
from pygame.locals import *
from world import *
from character import *
from gui import *
from sounds import *
from combat_handler import *
import config

RES_X = 1366
RES_Y = 768
pygame.init()
_screen = pygame.display.set_mode((RES_X, RES_Y))

# This is the surface we are rendering to
screen = pygame.Surface((RES_X - config.SIDEBAR_WIDTH, RES_Y - 130))
clock = pygame.time.Clock()

TILE_GRID_WIDTH = screen.get_width()/config.TILE_W
TILE_GRID_HEIGHT = screen.get_height()/config.TILE_H

class EventController():
    def handleEvents(self):
        event_list = pygame.event.get() 

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                clicked_pos = pygame.mouse.get_pos()
                # TODO: Check for event collision and handle
            elif event.type == pygame.KEYUP:
                pygame.quit()
            elif event.type == pygame.USEREVENT:
                if event.dict[1] == "startcombat":
                    


class Block(pygame.sprite.Sprite):
    def __init__(self, image, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.image = self.src_image.convert()

sounds = sound_player()
events = EventController()
world = World(TILE_GRID_HEIGHT, TILE_GRID_WIDTH, os.path.join('img', 'testgrid.png'), screen)
character = Character(os.path.join('img', 'character.png'), (10, 10), screen)

sidebar = Sidebar(_screen, config.SIDEBAR) 
button = Button(sidebar, 5, config.BUTTON, "Attack")
button2 = Button(sidebar, 6, config.BUTTON, "Research")
button3 = Button(sidebar, 7, config.BUTTON, "DIE!")
stats = Stats(sidebar, 1, config.STATS, character)

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
    stats.draw()
    # character.draw()
    sidebar.blit()
    _screen.blit(screen, (0, 0))
    pygame.display.flip()

pygame.quit()
