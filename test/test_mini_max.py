import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.game_manager import mini_max as m
from src.helpers import helper
from src.board_manager import board

def main():
    myUser = helper.Player
    myUser.initialize()
    
    myBoard = board.board(3)
    myBoard.place(4, myUser.current())
    myBoard.place(5, myUser.current())

    myMiniMax = m.mini_max(3, 3)
    place = myMiniMax.bestmove(myBoard, myUser.current())
    print(place)
    myUser.switch()
    myBoard.place(place, myUser.current())
    myBoard.print_board()


if __name__ == "__main__":
    main()
