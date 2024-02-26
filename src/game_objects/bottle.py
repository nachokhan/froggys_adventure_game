import pygame
from config import TILE_SIZE


class Bottle:
    def __init__(self, x, y, is_taken=False):
        self.x = x
        self.y = y
        self.is_taken = is_taken
        self.image_taken = pygame.image.load("assets/images/empty_bottle.png")
        self.image_untaken = pygame.image.load("assets/images/filled_bottle.png")
        self.image_taken = pygame.transform.scale(self.image_taken, (TILE_SIZE, TILE_SIZE))
        self.image_untaken = pygame.transform.scale(self.image_untaken, (TILE_SIZE, TILE_SIZE))

    def draw(self, screen):
        if self.is_taken:
            screen.blit(self.image_taken, (self.x * TILE_SIZE, self.y * TILE_SIZE))
        else:
            screen.blit(self.image_untaken, (self.x * TILE_SIZE, self.y * TILE_SIZE))

    def take(self):
        self.is_taken = True
