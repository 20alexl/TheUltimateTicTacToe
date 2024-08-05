#helpers/helper.py
from enum import Enum

class player(Enum):
    O = 0
    X = 1

class end_game:
    def __init__(self, lives = 3):
        self._lives = lives
        self.score = 4
    
    @property
    def lives(self):
        return self._lives

    @lives.setter
    def set_lives(self, value):
        # Ensure the value is within the allowed range
        if  1 <= value:
            self._level = value
        else:
            raise ValueError(f"Must have 1 or more lives.")

    def lost(self):
        # Lost a life
        self.score -= 1
        self._lives -= 1

    def game_over(self):
        # Lost a life
        if self._lives == 0:
            return True
        else:
            return False

    def credits(self, helper):
        print("----------------------------------------------------------------------")
        print("--------------------------------GG------------------------------------")
        print(f"----------------------STAGE {helper.stage} ---- LEVEL {helper.level}----------------------------")
        print(f"-----------------------------SCORE: {self.score}---------------------------------")
        print(f"----------------------------------------------------------------------")
