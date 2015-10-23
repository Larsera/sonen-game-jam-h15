import pygame, random
from pygame.locals import *
from pygame import Rect

import os

TILE_W = 32
TILE_H = 32

TILESETFILE = "tmp"

class Map():
	def __init__(self, size_x, size_y, screen):
		random.seed()
		self.screen = screen
		self.size_x = size_x
		self.size_y = size_y

		self.scrolling = False

#Need tilset
		self.load_tileset(TILESETFILE)
		self.createmap()

	def scroll(self, rel):
		if not self.scrolling: return

		self.offset = (
				self.offset[0] + rel[0],
				self.offset[1] + rel[1])

	def load_tileset(self, image="tileset.bmp"):
		self.tileset = pygame.image.load(os.path.join("img", image)).convert()
		self.rect = self.tileset.get_rect()


	def createmap(self):
		self.world = [[0 for i in xrange(self.size_y)]
		for i in xrange(self.size_x)]

		# Populate desert with big rocks
		for i in xrange(self.size_x):
			for j in xrange(self.size_y):
				if random.randint(0, 10) > 9:
					self.world[i][j] = 1

		# Populate desert with small rocks
		for x in xrange(6):
			for i in range(1, self.size_x - 1):
				for j in range(1, self.size_y - 1):
					if (self.world[i+1][j] == 1 or self.world[i][j+1] == 1
						or self.world[i-1][j] == 1 or self.world[i][j-1] == 1):

						if random.randint(0, 10) > 3:
							self.world[i][j] = 2

	def draw(self):
		for y in range(self.size_x):
			for x in range(self.size_y):
				id = self.world[x, y]

				dest = Rect(x * TILE_W, y * TILE_H, TILE_W, TILE_H)
				src = Rect(id * TILE_W, 0, TILE_W, TILE_H)
				if self.scrolling:
					dest.left += self.offset[0]
					dest.top += self.offset[1]

				self.screen.blit(self.tileset, dest, src)


