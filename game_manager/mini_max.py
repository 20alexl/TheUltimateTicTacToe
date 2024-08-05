#game_manager/mini_max.py
from helpers import helper

resume = 1
tie = 0
win = 2

score_tie = 0
score_human = -10
score_comp = 10

class mini_max():
    def __init__(self,depth, table, stage):
        self.n = stage
        self.level = depth
        self.board = table
        self.mini = float('inf')
        self.maxi = float('-inf')
        self.mini_index = None
        self.maxi_index = None

    def mini_max(self, table, depth, is_maximizing, user):
        self.board = table
        result = self.check_win(self.board)

        if result == win:
            return score_comp if user == helper.player.O else score_human
        if result == tie:
            return score_tie

        if is_maximizing:
            best_score = -float('inf')
            for i in range(self.n ** 2):
                if i >= self.level:
                    return best_score
                if self.board[i] == " ":
                    self.board[i] = user.name
                    score = self.mini_max(self.board, depth + 1, False, helper.player.X if user == helper.player.O else helper.player.O)
                    self.board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(self.n ** 2):
                if i >= self.level:
                    return best_score
                if self.board[i] == " ":
                    self.board[i] = user.name
                    score = self.mini_max(self.board, depth + 1, True, helper.player.X if user == helper.player.O else helper.player.O)
                    self.board[i] = " "
                    best_score = min(score, best_score)
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