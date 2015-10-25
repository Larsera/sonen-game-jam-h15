import pygame, os, sys, random

class Cloud():

    def __init__(self, surface):
        self.surface = surface
        self.dust_image = pygame.image.load(os.path.join("img","dust_cloud.png"))
        random.seed()
        self.x = random.randint(-1024, -256)
        self.y = random.randint(-512, self.surface.get_height())
    
    def draw(self):
        self.surface.blit(self.dust_image, (self.x, self.y)) 
        self.x += 1
        if self.x > self.surface.get_width() + self.dust_image.get_width() + 10 : 
            random.seed()
            self.x = random.randint(-1024, -256)
            self.y = random.randint(-self.dust_image.get_height(), self.surface.get_height())
        
