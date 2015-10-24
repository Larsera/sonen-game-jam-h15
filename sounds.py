import pygame
import os
import time
from config import *

class sound_player():

    def __init__(self):
        pygame.mixer.init()
        self.sound_hit = pygame.mixer.Sound(os.path.join('sound', SOUND_HIT))
        self.sound_gameover = pygame.mixer.Sound(os.path.join('sound', SOUND_GAMEOVER))


