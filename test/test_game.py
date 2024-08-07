import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.game_manager import game as g
from src.level_manager import level as l

def main():
    myLevel = l.LevelManager()
    myGame = g.game(myLevel)
    myGame.start()


if __name__ == "__main__":
    main()
