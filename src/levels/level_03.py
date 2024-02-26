from src.levels.level import Level
from src.game_objects.froggy import Froggy
from src.game_objects.door import Door
from src.game_objects.rock import Rock
from src.game_objects.bottle import Bottle


class Level03(Level):
    def __init__(self):
        super().__init__(4)
        self.froggy = Froggy(0, 0)
        self.door = Door(9, 9)
        self.rocks = [
            Rock(1, 1), Rock(1, 2), Rock(1, 3), Rock(1, 4), Rock(1, 5),
            Rock(2, 1), Rock(2, 5),
            Rock(3, 1), Rock(3, 5),
            Rock(4, 1), 
            Rock(5, 1),  Rock(5, 3),  Rock(5, 5)
        ]
        self.bottles = [
            Bottle(2, 2), Bottle(2, 3), Bottle(2, 4),
            Bottle(3, 2), Bottle(3, 3), Bottle(3, 4),
            Bottle(4, 2), Bottle(4, 3), Bottle(4, 4)
        ]