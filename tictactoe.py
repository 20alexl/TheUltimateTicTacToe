#main.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src import game_manager as g
from src import level_manager as l
from src import helpers as h

def main(level, tog):
    # Initialize the game with level manager
    game = g.game.game(level, tog)
    return game.start()

if __name__ == "__main__":
    level_manager = l.level.LevelManager()
    helper = h.helper.end_game()
    tehe = False #allow computer to go first cause why not(got very boring going first)
    while True:
        winner = main(level_manager, tehe)

        if winner == "X":
            helper.score += 1
            level_manager.advance()
        elif winner == "O":
            level_manager.advance()
            helper.lost()
        else:
            level_manager.advance()

        if helper.game_over():
            helper.credits(level_manager)
            break
        else:
            again = input(f"LIVES REMAINING:{helper.lives} Play Again? (y/n)")
            if again not in ["y","Y","yes", "YES"]:
                helper.credits(level_manager)
                break
        tehe = not tehe


