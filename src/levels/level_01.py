from src.levels.level import Level
from src.game_objects.froggy import Froggy
from src.game_objects.door import Door
from src.game_objects.rock import Rock
from src.game_objects.bottle import Bottle


class Level01(Level):
    def __init__(self):
        super().__init__(1)
        self.froggy = Froggy(0, 0)
        self.door = Door(10, 10)
        self.rocks = [Rock(5, 5), Rock(6, 5)]
        self.bottles = [Bottle(6, 6), Bottle(9, 9)]
