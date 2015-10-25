import os
import pygame
from monster import get_monster

# Color palette:
COLOR_DARKEST   = (26, 14, 5)
COLOR_DARK      = (50, 31, 19)
COLOR_LIGHT     = (130, 102, 84)
COLOR_LIGHTEST  = (203, 163, 136)

# Tile
TILE_W = TILE_H = 32
DEFAULT_MONSTER_LIST = [get_monster("rattlesnake"), get_monster("small_scorpion"),
        get_monster("big_scorpion"), get_monster("road_runner"),
        get_monster("coyote"), get_monster("camel"), get_monster("skink")]

# Character:
CHANCE_DEC = 20
WATER_DEC = 10
HUNGER_DEC = 10

# Gui:
SIDEBAR_WIDTH = 256
SIDEBAR_UNIT_HEIGHT = 32
SIDEBAR_PADDING = 20
SIDEBAR_OUTLINE = 4
SIDEBAR_OUTLINE_COLOR = COLOR_LIGHTEST

DOWNBAR_HEIGHT = 150
DOWNBAR_UNIT_HEIGHT = 32
DOWNBAR_PADDING = 20

BUTTON_PADDING = 5
BUTTON_HEIGHT = 32
BUTTON_OUTLINE = 5
BUTTON_OUTLINE_COLOR = COLOR_LIGHTEST
BUTTON_TEXT_COLOR = COLOR_LIGHTEST
BUTTON_FONT_SIZE = 24

STATS_HEIGHT = 128
STATS_OUTLINE = 5
STATS_FONT_SIZE = 24

TEXT_PADDING = 23
TEXT_OUTLINE = 5

DIRBTN_OUTLINE = 5
DIRBTN_SIZE = 40
DIRBTN_PADDING = 4
DIRBTN_TEXT_COLOR = COLOR_LIGHTEST
DIRBTN_OUTLINE_COLOR = COLOR_LIGHTEST

CONSOLE_WIDTH = 800
CONSOLE_PADDING = 10
CONSOLE_FONT_SIZE = 32
CONSOLE_OUTLINE  = 5
CONSOLE_TEXT_PADDING = 23

#Game
TILE_WIDTH = 32
TILE_HEIGHT = 32

#sounds:
SOUND_HIT = "hit.wav"
SOUND_GAMEOVER = "gameover.wav"

#images
TILES = os.path.join('img', 'tilegrid.png')
SIDEBAR = os.path.join('img', 'panel_crystallized.png')
BUTTON = os.path.join('img', 'button_crystallized.png')
STATS = os.path.join('img', 'tileset_old.jpg')

#events
COMBAT = pygame.USEREVENT+1
NEWTURN = pygame.USEREVENT+2
WIN = pygame.USEREVENT+3
GAMEOVER = pygame.USEREVENT+4
ENDCOMBAT = pygame.USEREVENT+5
