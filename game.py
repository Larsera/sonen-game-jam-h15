import pygame, math, sys, os
from pygame.locals import *
from world import *
from character import *
from gui import *
from sounds import *
from combat_handler import *
from tiles import get_tile
import config

RES_X = 1366
RES_Y = 768
pygame.init()
_screen = pygame.display.set_mode((RES_X, RES_Y))

class Game():
# This is the surface we are rendering to

    def init(self):
        self.screen = pygame.Surface((RES_X - config.SIDEBAR_WIDTH, RES_Y - config.DOWNBAR_HEIGHT))
        self.clock = pygame.time.Clock()

        self.turns_survd = 0

        self.TILE_GRID_WIDTH = self.screen.get_width()/config.TILE_W
        self.TILE_GRID_HEIGHT = self.screen.get_height()/config.TILE_H
        self.sounds = sound_player()
        self.world = World(self.TILE_GRID_HEIGHT, self.TILE_GRID_WIDTH, TILES, self.screen)
        self.character = Character(os.path.join('img', 'character.png'), (10, 10), self.screen)

        self.sidebar                = Sidebar(_screen, config.SIDEBAR) 
        self.button_search          = Button(self.sidebar, 5, config.BUTTON, "Search")
        self.button_drink_antidote  = Button(self.sidebar, 6, config.BUTTON, "Drink antidote")
        self.button_attack          = Button(self.sidebar, 5, config.BUTTON, "Attack")
        self.button_defend          = Button(self.sidebar, 6, config.BUTTON, "Defend")
        self.button_flee            = Button(self.sidebar, 7, config.BUTTON, "Flee")
        self.stats                  = Stats(self.sidebar, 1, config.STATS, self.character)

# downbar = Downbar(_screen,os.path.join('img', 'tileset_old.jpg'))
        self.dirbtn = DirectionButtons(_screen, 50, 630, os.path.join('img', 'tileset_old.jpg'))
    
    def handleEvents(self):
        event_list = pygame.event.get() 

        def handleMouseEvent(event): 
                clicked_pos = pygame.mouse.get_pos()
                
                if self.button_search.get_surface_mapped_rect(_screen).collidepoint(clicked_pos): 
                    print "Clicked: search"

                elif self.button_drink_antidote.get_surface_mapped_rect(_screen).collidepoint(clicked_pos): 
                    print "Clicked: drink_antidote"

                elif self.dirbtn.n_rect.collidepoint(clicked_pos):
                    x, y = self.character.position
                    self.character.move('N', get_tile(self.world.world[x][y]))

                elif self.dirbtn.s_rect.collidepoint(clicked_pos): 
                    print "Clicked: south"

                elif self.dirbtn.e_rect.collidepoint(clicked_pos): 
                    print "Clicked: east"

                elif self.dirbtn.w_rect.collidepoint(clicked_pos): 
                    print "Clicked: west"

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                handleMouseEvent(event)

            elif event.type == pygame.KEYUP:
                pygame.quit()

            elif event.type == pygame.USEREVENT:
                if event.dict[1] == "startcombat":
                    self.state = "combat"
                elif event.dict[1] == "gameover":
                    self.state = "gameover"
                elif event.dict[1] == "newturn":
                    self.newturn()

    def newturn(self):
        self.turns_survd += 1
        #self.character.update()

    def run(self):
        running = 1
        self.state = "normal" 
        while running:
            self.screen.fill((255, 204, 102))
            self.handleEvents()
            self.world.draw()
            self.sidebar.draw()
            if self.state == "normal":
                self.button_search.draw()
                self.button_drink_antidote.draw()
            elif self.state == "combat":
                self.button_attack.draw()
                self.button_defend.draw()
                self.button_flee.draw()
            #button3.draw()
            self.stats.draw()
            self.character.draw()
            self.sidebar.blit()

            # downbar.draw()
            # downbar.blit()

            self.dirbtn.draw()
            _screen.blit(self.screen, (0, 0))
            pygame.display.flip()

        pygame.quit()

game = Game()
game.init()
game.run()
