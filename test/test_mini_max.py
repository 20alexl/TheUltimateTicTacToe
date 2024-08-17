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
    myBoard.place(3, myUser.current())
    myBoard.place(6, myUser.current())
    myBoard.place(8, myUser.current())


    myMiniMax = m.mini_max(4, 3)
    place = myMiniMax.bestmove(myBoard, myUser.current())
    print(place + 1)
    myUser.switch()
    myBoard.place(place, myUser.current())
    myBoard.print_board()


if __name__ == "__main__":
    main()
