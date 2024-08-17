#game_manager/game.py

#old game class that didnt meet the requirments :/

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helpers import helper
from board_manager import board as b
from game_manager import mini_max

resume = 1
tie = 0
win = 2

#Move into main

class game:
    def __init__(self, cur_level, tog):
        self.level = cur_level
        self.depth = self.level.level
        self.user = helper.Player
        self.user.initialize()

        if tog:
            self.user.switch()
        
        self.board = b.board(self.level.stage)
        self.mini_max = mini_max.mini_max(self.depth, self.level.stage)
        self.boiler(self.level.level, self.level.stage)

        if self.level.level == 1:
            self.board.example_board(self.level.stage)
    
    def boiler(self, level, stage):
        print(f"----------------------------------------------------------------------")
        print(f"--------------------------STAGE {stage-2} ---- LEVEL {level}------------------------")
        print(f"----------------------------------------------------------------------")

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
                    self.board.place(move - 1 , self.user.current())
        else:
                print(f"Not a valid move(Not Num). Enter another move!")
                self.board.print_board()
                self.board.example_board(self.level.stage)
                move = input(f"Move: ").strip()
                self.valid_move(move)

    def start(self):
        while True:
            if self.user.current() == "X":
                place = input(f"Enter your move (1-{self.level.stage ** 2}): ").strip()
                self.valid_move(place)
                if self.mini_max.check_win(self.board.board) != resume:
                    break
            else:
                best_move = self.mini_max.bestmove(self.board, helper.Player.X.name)
                if best_move is not None:
                    if best_move == "tie":
                        return "tie"
                    self.board.place(best_move, self.user.current())
                    self.board.print_board()
                    if self.mini_max.check_win(self.board.board) != resume:
                        break
            self.user.switch()

        result = self.mini_max.check_win(self.board.board)
        if result == win:
            print(f"Player {self.user.current()} wins!!!")
            return self.user.current()
        else:
            print(f"Tie!!!")
            return "tie"
