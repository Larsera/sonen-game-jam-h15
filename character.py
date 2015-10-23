import pygame

class Character():
    def __init__(self, image, position):
        self.src_image = pygame.image.load(image)
        self.position = position
        self.speed = self.direction = 0


