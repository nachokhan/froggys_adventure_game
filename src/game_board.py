from src.levels.level import Level


class GameBoard:
    def __init__(self):
        self.level_n = 1
        self.load_level(self.level_n)

    def load_level(self, number):
        self.level = Level(number, "nivel")
        self.level_n = number
        self.level.load_level()

    def draw(self, screen):
        self.level.door.draw(screen)
        for rock in self.level.rocks:
            rock.draw(screen)
        for bottle in self.level.bottles:
            bottle.draw(screen)
        self.level.froggy.draw(screen)
