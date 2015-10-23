import pygame, math, sys, os
from pygame.locals import *
from world import *
from character import *

pygame.init()
_screen = pygame.display.set_mode((1366, 768))
screen = pygame.Surface(_screen.get_size())
clock = pygame.time.Clock()

class EventController():
    def handleEvents(self):
        event_list = pygame.event.get() 

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                clicked_pos = pygame.mouse.get_pos()
                # TODO: Check for event collision and handle

class Block(pygame.sprite.Sprite):
    def __init__(self, image, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.image = self.src_image.convert()

events = EventController()
world = World(128, 128, os.path.join('img', 'tileset.png'), screen)
character = Character(os.path.join('img', 'character.png'), (10, 10), screen)

running = 1
while running:
    screen.fill((255, 204, 102)) 
    events.handleEvents()
    character.update()
    world.draw()
    character.draw()

    _screen.blit(screen, (0,0))
    pygame.display.flip()

pygame.quit()
