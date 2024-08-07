import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.helpers import helper as h
from src.game_manager import game as g
from src.game_manager import mini_max as m
from src.level_manager import level as l
from src.board_manager import board as b

def main():
    myLevel = l.LevelManager()
    myGame = g.game(myLevel)
    #myMiniMax = m.mini_max()
    #myBoard = b.board(3)
    #myPlayer = h.player.O
    #myEndGame = h.end_game()

    #myEndGame.credits()


if __name__ == "__main__":
    main()
