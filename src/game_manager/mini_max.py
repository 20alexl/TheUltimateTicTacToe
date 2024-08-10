#game_manager/mini_max.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helpers import helper

resume = 1
tie = 0
win = 2

score_tie = 0
score_human = -10
score_comp = 10

class mini_max():
    def __init__(self,depth, stage):
        self.n = stage
        self.level = depth
        self.mini = float('inf')
        self.maxi = float('-inf')
        self.mini_index = None
        self.maxi_index = None

    def mini_max(self, table, depth, is_maximizing, user):
        result = self.check_win(table)

        if result == win:
            return score_comp - depth if user == helper.Player.O else score_human + depth
        if result == tie:
            return score_tie

        if is_maximizing:
            best_score = -1000
            for i in range(self.n ** 2):
                if depth > self.level:
                    return depth

                if table[i] == " ":
                    table[i] = user.name

                    best_score = max(best_score, self.mini_max(table, depth + 1, False,\
                    helper.Player.X if user == helper.Player.O else helper.Player.O))

                    table[i] = " "
            return best_score
        else:
            best_score = 1000
            for i in range(self.n ** 2):
                if depth > self.level:
                    return -depth

                if table[i] == " ":
                    table[i] = user.name

                    best_score = min(best_score, self.mini_max(table, depth + 1, True,\
                    helper.Player.X if user == helper.Player.O else helper.Player.O))

                    table[i] = " "
            return best_score

    def check_line(self, start, step, length):
        first = self.board[start]
        if first == " ":
            return False
        for i in range(1, length):
            if self.board[start + i * step] != first:
                return False
        return True

    def check_win(self, board):
        self.board = board
        # Check rows and columns
        for i in range(self.n):
            if self.check_line(i * self.n, 1, self.n) or self.check_line(i, self.n, self.n):
                return win
        
        # Check diagonals
        if self.check_line(0, self.n + 1, self.n) or self.check_line(self.n - 1, self.n - 1, self.n):
            return win
        
        # Check for tie
        if " " not in board:
            return tie
        
        # Game should continue
        return resume
    
    def bestmove(self, table, user):
        best_score = -1000
        best_move = None
        for i in range(self.n ** 2):
            if table.board[i] == " ":
                table.place(i, user)
                score = self.mini_max(table.board, 0, True, helper.Player.O)
                table.board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move