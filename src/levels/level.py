import importlib
from src.game_objects.froggy import Froggy
from src.game_objects.door import Door
from config import BOARD_SIZE


class Level:
    def __init__(self, number, name):
        self.name = name
        self.number = number
        self.froggy = Froggy(0, 0)  # Posición inicial de Froggy
        self.door = Door(19, 19)   # Posición de la puerta
        self.rocks = []            # Lista de rocas
        self.bottles = []          # Lista de botellas
        self.finished = False

    def load_level(self):
        level_module_name = f"src.levels.level_{str(self.number).zfill(2)}"
        level_module = importlib.import_module(level_module_name)
        level_class = getattr(level_module, f"Level{str(self.number).zfill(2)}")
        level_instance = level_class()

        self.froggy = level_instance.froggy
        self.door = level_instance.door
        self.rocks = level_instance.rocks
        self.bottles = level_instance.bottles

    def is_move_valid(self, x, y):
        if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
            return False  # Movimiento fuera del tablero
        if any(rock.x == x and rock.y == y for rock in self.rocks):
            return False  # Hay una roca en la posición
        if self.door.x == x and self.door.y == y and not self.door.is_open:
            return False  # La puerta está cerrada
        if any(bottle.x == x and bottle.y == y and bottle.is_taken for bottle in self.bottles):
            return False  # Hay una botella no tomada en la posición
        return True

    def check_item_at(self, x, y):
        for bottle in self.bottles:
            if bottle.x == x and bottle.y == y and not bottle.is_taken:
                bottle.take()
                self.update_door_state()

    def update_door_state(self):
        if all(bottle.is_taken for bottle in self.bottles):
            self.door.open_door()

    def is_completed(self):
        return self.door.is_open and self.froggy.x == self.door.x and self.froggy.y == self.door.y

    def check_completion(self):
        if self.is_completed():
            self.finished = True
