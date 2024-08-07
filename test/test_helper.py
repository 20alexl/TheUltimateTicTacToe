import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.helpers import helper as h

def main():
    myPlayer = h.Player
    myEndGame = h.end_game()

    myPlayer.initialize()
    print(myPlayer.current())
    myPlayer.switch()
    print(myPlayer.current().name)


if __name__ == "__main__":
    main()
