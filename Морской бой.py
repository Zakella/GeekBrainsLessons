from pprint import pprint
import random


class SeaMap:
    def __init__(self):
        self.ships_map = []
        self.shoot_map = []

    def create_map(self):
        for i in range(0, 10):
            self.ships_map.append(["." for _ in range(0, 5)])

        decks = {  # палубы
            1: 4,
            # 2: 3,
            # 3: 2,
            # 4: 1
        }
        for key, value in decks.items():
            for i in range(0, value):
                row = random.randint(0, 9)
                column = random.randint(0, 4)
                self.ships_map[row][column] = "$"

    def show_map(self):
        print(self.ships_map)
        for i in self.ships_map:
            pprint(''.join(i))


game = SeaMap()
game.create_map()
game.show_map()
