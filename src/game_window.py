import pygame
from src.game_board import GameBoard
from config import WINDOW_HEIGHT, WINDOW_WIDTH


class GameWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.game_board = GameBoard()
        self.congratulations_font = pygame.font.SysFont(None, 100)  # Fuente para el cartel de felicitaciones

    def run_game(self):
        running = True
        level = self.game_board.level
        froggy = level.froggy
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:

                    if level.finished:
                        self.show_congratulations()
                        self.game_board.level_n += 1
                        self.game_board.load_level(self.game_board.level_n)
                        level = self.game_board.level
                        froggy = level.froggy
                        break

                    # Move Froggy when arrow keys are pressed
                    if event.key == pygame.K_LEFT:
                        froggy.move("left", level)
                    elif event.key == pygame.K_RIGHT:
                        froggy.move("right", level)
                    elif event.key == pygame.K_UP:
                        froggy.move("up", level)
                    elif event.key == pygame.K_DOWN:
                        froggy.move("down", level)

            self.screen.fill((0, 0, 0))
            self.game_board.draw(self.screen)
            pygame.display.flip()

        pygame.quit()

    def show_congratulations(self):
        # Mostrar el cartel de felicitaciones en el centro de la pantalla
        text = self.congratulations_font.render("Congratulations!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

        # Esperar a que se presione una tecla
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    waiting = False
