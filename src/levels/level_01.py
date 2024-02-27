from src.levels.level import Level
from src.game_objects.froggy import Froggy
from src.game_objects.door import Door
from src.game_objects.rock import Rock
from src.game_objects.bottle import Bottle


class Level01(Level):
    def __init__(self):
        super().__init__(1, "lalala")
        self.froggy = Froggy(1, 2)
        self.door = Door(2, 2)
        self.rocks = [Rock(1, 1), Rock(2, 1), Rock(3, 1), Rock(0, 1), Rock(0, 2), Rock(0, 3), Rock(0, 4), Rock(0, 5), Rock(0, 6), Rock(4, 1), Rock(5, 1), Rock(5, 2), Rock(5, 3), Rock(5, 3), Rock(5, 4), Rock(5, 5), Rock(5, 6), Rock(5, 7), Rock(0, 7), Rock(2, 7), Rock(3, 7), Rock(4, 7), Rock(1, 7), Rock(2, 3), Rock(3, 4), Rock(2, 5), Rock(2, 4), Rock(3, 3), Rock(3, 5), Rock(7, 3), Rock(7, 2), Rock(7, 1), Rock(8, 1), Rock(9, 1), Rock(9, 2), Rock(9, 3), Rock(7, 4), Rock(9, 4), Rock(8, 3), Rock(11, 4), Rock(11, 3), Rock(11, 2), Rock(11, 1), Rock(12, 1), Rock(12, 1), Rock(13, 1), Rock(13, 2), Rock(12, 3), Rock(13, 4), Rock(11, 5), Rock(12, 5), Rock(13, 5), Rock(9, 5), Rock(7, 5), Rock(9, 7), Rock(8, 7), Rock(7, 7), Rock(7, 8), Rock(7, 10), Rock(7, 9), Rock(7, 11), Rock(8, 11), Rock(9, 11), Rock(11, 7), Rock(11, 9), Rock(11, 8), Rock(11, 10), Rock(11, 11), Rock(12, 11), Rock(13, 10), Rock(13, 9), Rock(13, 8), Rock(12, 7), Rock(1, 9), Rock(2, 9), Rock(3, 9), Rock(1, 10), Rock(1, 11), Rock(2, 11), Rock(1, 12), Rock(1, 13), Rock(2, 13), Rock(3, 13)]
        self.bottles = [Bottle(1, 3), Bottle(1, 4), Bottle(1, 5), Bottle(1, 6), Bottle(2, 6), Bottle(3, 6), Bottle(4, 6), Bottle(4, 5), Bottle(4, 4), Bottle(4, 3), Bottle(4, 2), Bottle(3, 2)]

