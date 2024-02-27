from src.levels.level import Level
from src.game_objects.froggy import Froggy
from src.game_objects.door import Door
from src.game_objects.rock import Rock
from src.game_objects.bottle import Bottle


class Level02(Level):
    def __init__(self):
        super().__init__(2, "name")
        self.froggy = Froggy(0, 0)
        self.door = Door(9, 9)
        self.rocks = [Rock(1, 1), Rock(1, 2), Rock(2, 1)]
        self.bottles = [Bottle(5, 5), Bottle(6, 6), Bottle(7, 7)]
