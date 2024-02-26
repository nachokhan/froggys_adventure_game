import pygame
from config import TILE_SIZE


class Froggy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("assets/images/froggy.png")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

    def move(self, direction, level):
        new_x, new_y = self.x, self.y
        if direction == "up":
            new_y -= 1
        elif direction == "down":
            new_y += 1
        elif direction == "left":
            new_x -= 1
        elif direction == "right":
            new_x += 1

        if level.is_move_valid(new_x, new_y):
            self.x, self.y = new_x, new_y
            level.check_item_at(new_x, new_y)
            level.check_completion()

    def draw(self, screen):
        screen.blit(self.image, (self.x * TILE_SIZE, self.y * TILE_SIZE))
