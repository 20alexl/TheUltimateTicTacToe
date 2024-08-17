import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.board_manager import board as b

def main():
    myBoard = b.board(3)
    myBoard.place(1,"X")
    myBoard.place(2,"O")
    myBoard.print_board()
    myBoard.example_board()


if __name__ == "__main__":
    main()
