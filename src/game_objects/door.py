import pygame
from config import TILE_SIZE


class Door:
    def __init__(self, x, y, is_open=False):
        self.x = x
        self.y = y
        self.is_open = is_open
        self.image_open = pygame.image.load("assets/images/open_door.png")
        self.image_closed = pygame.image.load("assets/images/closed_door.png")
        self.image_open = pygame.transform.scale(self.image_open, (TILE_SIZE, TILE_SIZE))
        self.image_closed = pygame.transform.scale(self.image_closed, (TILE_SIZE, TILE_SIZE))

    def draw(self, screen):
        if self.is_open:
            screen.blit(self.image_open, (self.x * TILE_SIZE, self.y * TILE_SIZE))
        else:
            screen.blit(self.image_closed, (self.x * TILE_SIZE, self.y * TILE_SIZE))

    def open_door(self):
        self.is_open = True
