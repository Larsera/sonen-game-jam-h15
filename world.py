#import pygame
import random
#from pygame.locals import *
#from pygame import Rect

import os

TILE_W = 32
TILE_H = 32

TILESETFILE = "tmp"

class World():
	def __init__(self, size_x, size_y, screen):
		random.seed()
		self.screen = screen
		self.size_x = size_x
		self.size_y = size_y

		self.scrolling = False

#Need tilset
#		self.load_tileset(TILESETFILE)
		self.createmap()

#	def scroll(self, rel):
#		if not self.scrolling: return

#		self.offset = (
#				self.offset[0] + rel[0],
#				self.offset[1] + rel[1])

#	def load_tileset(self, image="tileset.bmp"):
#		self.tileset = pygame.image.load(os.path.join("img", image)).convert()
#		self.rect = self.tileset.get_rect()


	def createmap(self):
		self.world = [[0 for i in xrange(self.size_x)]
		for i in xrange(self.size_y)]

		# Populate desert with big rocks
		for i in xrange(self.size_y):
			for j in xrange(self.size_x):
				if random.randint(0, 100) >= 99:
					self.world[i][j] = 1

		# Populate desert with small rocks
		for x in xrange(3):
			for i in range(1, self.size_y - 1):
				for j in range(1, self.size_x - 1):
					if (self.world[i+1][j] == 1 or self.world[i][j+1] == 1
						or self.world[i-1][j] == 1 or self.world[i][j-1] == 1
						or self.world[i+1][j] == 2 or self.world[i][j+1] == 2
						or self.world[i-1][j] == 2 or self.world[i][j-1] == 2):

						if self.world[i][j] == 0 and random.randint(0, 10) > 7:
							self.world[i][j] = 2

		# Populate desert with jagged rocks
		for i in xrange(self.size_y):
			for j in xrange(self.size_x):
				if self.world[i][j] == 2 and random.randint(0, 100) > 94:
					self.world[i][j] = 3

		# Populate desert with oases
		for i in xrange(self.size_y):
			for j in xrange(self.size_x):
				if self.world[i][j] == 0 and random.randint(0, 300) > 299:
					self.world[i][j] = 4

		# Populate desert with abandoned camps
		for i in xrange(self.size_y):
			for j in xrange(self.size_x):
				if self.world[i][j] == 0 and random.randint(0, 500) > 499:
					self.world[i][j] = 5

		# Populate desert with pyramid
		target = 1
		count = 0
		x = 0
		y = 0
		while target != 0 and < 50:
			x = random.randint(0, self.size_x)
			y = random.randint(0, self.size_y)
			target = self.world[y][x]
			count = count + 1

		self.world[y][x] = 6


	def test(self):
		for i in xrange(self.size_y):
			for j in xrange(self.size_x):
				if self.world[i][j] == 0:
					print ".",
				if self.world[i][j] == 1:
					print "O",
				if self.world[i][j] == 2:
					print "*",
				if self.world[i][j] == 3:
					print "X",
				if self.world[i][j] == 4:
					print "Y",
				if self.world[i][j] == 5:
					print "@",
				if self.world[i][j] == 6:
					print "^",
			print ""
#	def draw(self):
#		for y in range(self.size_x):
#			for x in range(self.size_y):
#				id = self.world[x, y]

#				dest = Rect(x * TILE_W, y * TILE_H, TILE_W, TILE_H)
#				src = Rect(id * TILE_W, 0, TILE_W, TILE_H)
#				if self.scrolling:
#					dest.left += self.offset[0]
#					dest.top += self.offset[1]

#				self.screen.blit(self.tileset, dest, src)


world = World(80, 40, 1)
world.createmap()
world.test()
