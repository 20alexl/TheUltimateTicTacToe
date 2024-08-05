#game_manager/game.py
from helpers import helper
from board_manager import board as b
from level_manager import level
from game_manager import mini_max

resume = 1
tie = 0
win = 2

class game:
    def __init__(self, cur_level):
        self.level = cur_level
        self.depth = self.level.level * 2
        self.user = helper.player.X
        self.board = b.board(self.level.stage)
        self.mini_max = mini_max.mini_max(self.depth, self.board.board, self.board._size)
        self.boiler(self.level.level, self.level.stage)
        if self.level.level == 1:
            self.board.example_board(self.level.stage)
    
    def boiler(self, level, stage):
        print(f"----------------------------------------------------------------------")
        print(f"--------------------------STAGE {stage-2} ---- LEVEL {level}------------------------")
        print(f"----------------------------------------------------------------------")

    def switch(self):
        self.user = helper.player.O if self.user == helper.player.X else helper.player.X

    def valid_move(self, move):
        if move == "":
            return
        if move.isnumeric():
                move = int(move)
                if(move <= 0 or move > self.level.stage ** 2 or self.board.board[move - 1] != " "):
                    print(f"Not a valid move(Not in list). Enter another move!")
                    self.board.print_board()
                    self.board.example_board(self.level.stage)
                    move = input(f"Move: ").strip()
                    self.valid_move(move)
                else:
                    self.board.board[move - 1] = self.user.name
        else:
                print(f"Not a valid move(Not Num). Enter another move!")
                self.board.print_board()
                self.board.example_board(self.level.stage)
                move = input(f"Move: ").strip()
                self.valid_move(move)

    def start(self):
        while True:
            if self.user == helper.player.X:
                place = input(f"Enter your move (1-{self.level.stage ** 2}): ").strip()
                self.valid_move(place)
                self.board.print_board()
                if self.mini_max.check_win(self.board.board) != resume:
                    break
                self.switch()
            else:
                best_score = -float('inf')
                best_move = None
                for i in range(self.level.stage ** 2):
                    if self.depth > self.level.level:
                        if self.board.board[i] == " ":
                            self.board.board[i] = self.user.name
                            score = self.mini_max.mini_max(self.board.board, 0, True, helper.player.O)
                            self.board.board[i] = " "
                            if score > best_score:
                                best_score = score
                                best_move = i
                if best_move is not None:
                    self.board.board[best_move] = self.user.name
                    self.board.print_board()
                    if self.mini_max.check_win(self.board.board) != resume:
                        break
                self.switch()

        result = self.mini_max.check_win(self.board.board)
        if result == win:
            print(f"Player {self.user.name} wins!!!")
            return self.user.name
        else:
            print(f"Tie!!!")
            return "tie"
