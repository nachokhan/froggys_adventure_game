import pygame
from src.game_window import GameWindow


def main():
    pygame.init()
    game_window = GameWindow()
    game_window.run_game()


if __name__ == "__main__":
    main()
