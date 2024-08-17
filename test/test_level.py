import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.level_manager import level as l
from src.helpers import helper as h

def main():
    myLevel = l.LevelManager(3)
    end = h.end_game()
    end.credits(myLevel)
    myLevel.advance()
    end.credits(myLevel)
    myLevel.advance()
    end.credits(myLevel)
    myLevel.advance()
    end.credits(myLevel)


if __name__ == "__main__":
    main()
