import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.game_manager import mini_max as m

def main():
    myMiniMax = m.mini_max()
    myMiniMax.mini_max()


if __name__ == "__main__":
    main()
