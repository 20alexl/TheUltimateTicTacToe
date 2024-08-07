import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.board_manager import board as b

def main():
    myBoard = b.board(3)
    myBoard.place(1,"P")
    myBoard.place(1,"P")
    myBoard.print_board()


if __name__ == "__main__":
    main()
