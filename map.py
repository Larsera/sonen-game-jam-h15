import pygame

class Map():
	def __init__(self, size_x, size_y):
		self.world = [[0 for i in xrange(size_y)] for i in xrange(size_x)]
