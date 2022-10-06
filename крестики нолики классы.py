class TicTacToeBoard:
    def __init__(self):
        self.board = []
        self.game_over = False
        self.next_move = True

    def run(self):
        self.make_move()
        self.check_field()
        self.get_field()


    def new_game(self):
        for i in range(0, 3):
            self.board.append(["-" for _ in range(0, 3)])

    def get_field(self):
        print("********************")
        for i in self.board:
            print(i)

    def check_field(self):
        print(self.board)

        draw = True
        for i in self.board:
            draw = "-" not in i

        if draw:
            print("Силы были равны, ничья!")
            self.game_over = True
            return

        win_сorteges = [[(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                        [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                        [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
                        ]

        for combo in win_сorteges:
            self.check_combination(combo)

    def check_combination(self, *args):
        h_list = []
        for i in args[0]:
            h_list.append(self.board[i[0]][i[1]])

        h_list = list(set(h_list))
        if len(h_list) == 1:
            if "x" in h_list:
                print("Поздравляем! Игрок №1 победил!")
                self.game_over = True
            elif "0" in h_list:
                print("Поздравляем! Игрок №2 победил!")
                self.game_over = True

    def make_move(self):
        if self.next_move:
            player1_move = input('Игрок № 1 введите номер колонки, затем номер строки для хода: ')
            symb = "x"
            move = player1_move.split()
        else:
            player2_move = input('Игрок № 2 введите номер колонки, затем номер строки для хода: ')
            symb = "0"
            move = player2_move.split()

        for _ in self.board:
            if self.board[int(move[1]) - 1][int(move[0]) - 1] == "-":
                self.board[int(move[1]) - 1][int(move[0]) - 1] = symb
                self.next_move = not self.next_move
                break
            else:
                print("Место уже занято , сделайте ход еще раз!")
                break



board = TicTacToeBoard()
board.new_game()
board.get_field()
while not board.game_over:
   board.run()
