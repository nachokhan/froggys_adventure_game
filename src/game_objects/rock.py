import pygame
from config import TILE_SIZE


class Rock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("assets/images/rock.png")  # Carga la imagen de la roca
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

    def draw(self, screen):
        screen.blit(self.image, (self.x * TILE_SIZE, self.y * TILE_SIZE))  # Asume una variable 'TILE_SIZE'
