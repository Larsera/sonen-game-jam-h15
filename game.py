import pygame, math, sys, os
from pygame.locals import *
from world import *
from character import *
from gui import *
from sounds import *
from combat_handler import *
from tiles import get_tile
from items import get_foodstuff
import text
import config

RES_X = 1920
RES_Y = 1080
pygame.init()
_screen = pygame.display.set_mode((RES_X, RES_Y))

class Game():
# This is the surface we are rendering to

    def __init__(self):
        self.screen                 = pygame.Surface((RES_X - config.SIDEBAR_WIDTH, RES_Y - config.DOWNBAR_HEIGHT))
        self.clock                  = pygame.time.Clock()
        self.running                = True
        self.console                = Console(_screen)

        self.TILE_GRID_WIDTH        = self.screen.get_width()/config.TILE_W
        self.TILE_GRID_HEIGHT       = self.screen.get_height()/config.TILE_H
        self.sounds                 = sound_player()
        self.world                  = World(self.TILE_GRID_HEIGHT, self.TILE_GRID_WIDTH, TILES, self.screen)
        self.character              = Character(os.path.join('img', 'character.png'), (10, 10), self.screen, self.console)
        self.combat                 = None

        self.sidebar                = Sidebar(_screen, config.SIDEBAR) 
        self.button_search          = Button(self.sidebar, 5, config.BUTTON, "Search")
        self.button_drink_antidote  = Button(self.sidebar, 6, config.BUTTON, "Drink antidote")
        self.button_end_turn        = Button(self.sidebar, 7, config.BUTTON, "end turn")
        self.button_attack          = Button(self.sidebar, 5, config.BUTTON, "Attack")
        self.button_defend          = Button(self.sidebar, 6, config.BUTTON, "Defend")
        self.button_flee            = Button(self.sidebar, 7, config.BUTTON, "Flee")
        self.stats                  = Stats(self.sidebar, 1, config.STATS)


# downbar = Downbar(_screen,os.path.join('img', 'tileset_old.jpg'))
        self.dirbtn = DirectionButtons(_screen, 50,
                RES_Y - (config.DIRBTN_SIZE * 3 + config.DIRBTN_PADDING*2),
                os.path.join('img', 'tileset_old.jpg'))

    def handleEvents(self):
        event_list = pygame.event.get()

        def handleMouseEvent(event):
            clicked_pos = pygame.mouse.get_pos()
            
            if self.state == "normal":
                if self.button_search.get_surface_mapped_rect(_screen).collidepoint(clicked_pos):
                    curtile = self.world.get_cur_tile(self.character.position)
                    self.console.push_text("You search the area around you...")
                    self.character.search(curtile)

                elif self.button_drink_antidote.get_surface_mapped_rect(_screen).collidepoint(clicked_pos):
                    self.character.use_antidote()

                elif self.button_end_turn.get_surface_mapped_rect(_screen).collidepoint(clicked_pos):
                    self.console.push_text("Tired, you make the decision to rest for a while")
                    self.newturn()

                elif self.dirbtn.n_rect.collidepoint(clicked_pos):
                    self.character.move('N', self.world, self.console)

                elif self.dirbtn.s_rect.collidepoint(clicked_pos):
                    self.character.move('S', self.world, self.console)

                elif self.dirbtn.e_rect.collidepoint(clicked_pos):
                    self.character.move('E', self.world, self.console)

                elif self.dirbtn.w_rect.collidepoint(clicked_pos):
                    self.character.move('W', self.world, self.console)

            elif self.state == "combat":
                if self.button_attack.get_surface_mapped_rect(_screen).collidepoint(clicked_pos):
                    self.combat.do_combat_turn(1)

                elif self.button_defend.get_surface_mapped_rect(_screen).collidepoint(clicked_pos):
                    self.combat.do_combat_turn(2)

                elif self.button_flee.get_surface_mapped_rect(_screen).collidepoint(clicked_pos):
                    self.combat.do_combat_turn(3)


        def handleKeyEvent(event):
            if event.key == pygame.K_ESCAPE:
                self.running = False
            elif self.state == "normal":
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.character.move('N', self.world, self.console)

                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.character.move('S', self.world, self.console)

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.character.move('E', self.world, self.console)

                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.character.move('W', self.world, self.console)

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                handleMouseEvent(event)

            elif event.type == pygame.KEYUP:
                handleKeyEvent(event)

            elif event.type == config.COMBAT:
                self.state = "combat"
                curtile = self.world.get_cur_tile(self.character.position)
                self.combat = combat(self.character, curtile.get_monster(), self.console)
            elif event.type == config.ENDCOMBAT:
                self.state = "normal"
                self.combat = None
            elif event.type == config.GAMEOVER:
                self.state = "gameover"
            elif event.type == config.NEWTURN:
                self.newturn()
            elif event.type == config.WIN:
                self.state = "normal"
                self.combat = None
                self.character.find_food(get_foodstuff("raw_meat"))
            elif event.type == pygame.QUIT:
                self.running = False

    def newturn(self):
        self.character.update(self.world.get_cur_tile(self.character.position))

    def run(self):
        self.state = "normal" 
        while self.running:
            self.clock.tick()
            # print "Fps :", self.clock.get_fps()
            self.screen.fill(config.COLOR_DARK)
            _screen.fill(config.COLOR_DARK)
            self.handleEvents()
            self.world.draw()
            self.sidebar.draw()
            if self.state == "normal":
                self.button_search.draw()
                self.button_drink_antidote.draw()
                self.button_end_turn.draw()
            elif self.state == "combat":
                self.button_attack.draw()
                self.button_defend.draw()
                self.button_flee.draw()
            #button3.draw()
            self.stats.draw(self.character)
            self.character.draw()
            self.sidebar.blit()

            # downbar.draw()
            # downbar.blit()

            self.dirbtn.draw()
            self.console.draw()
            _screen.blit(self.screen, (0, 0))
            pygame.display.flip()

        pygame.quit()

game = Game()
game.run()
