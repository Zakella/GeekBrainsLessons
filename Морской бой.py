from pprint import pprint
import random


class SeaMap:
    rows = 5
    columns = 10
    symbol_ship = "$"
    symbol_busy = "^"
    symbol_empty_field = "."

    def __init__(self):
        self.ships_map = []
        self.shoot_map = []
        self.game_over = False

    def create_map(self):
        for i in range(0, self.columns):
            self.ships_map.append([self.symbol_empty_field for _ in range(0, self.rows)])
            self.shoot_map.append([self.symbol_empty_field for _ in range(0, self.rows)])

        decks = {  # палубы по хорошему их надо сделать строгими, но получатся случайными
            1: 4,
            2: 3,
            3: 2,
            4: 1
        }
        for key, value in decks.items():
            for i in range(0, value):
                self.create_ships(key)

    def create_ships(self, quant):
        row = random.randint(0, self.columns - 1)
        column = random.randint(0, self.rows - 1)
        if self.ships_map[row][column] == self.symbol_ship or self.ships_map[row][column] == self.symbol_busy:
            self.create_ships(quant)
        else:
            self.ships_map[row][column] = self.symbol_ship
            for i in range(0, quant):
                try:
                    self.ships_map[row][i + column] = self.symbol_ship
                except:
                    self.ships_map[row][i - column] = self.symbol_ship

    def show_map(self):
        print(self.ships_map)
        for i in self.ships_map:
            pprint(''.join(i))
        pprint(self.symbol_busy * self.columns)
        for i in self.shoot_map:
            pprint(''.join(i))

    def shoot(self, row, col):
        self.shoot_map[row][col] = "*"
        self.show_map()




sm = SeaMap()
sm.create_map()
sm.show_map()
while not sm.game_over:
    pass

