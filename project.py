#main.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

#from src import game_manager as g
from src import level_manager as l
from src import helpers as h
from board_manager import board as b
from game_manager import mini_max as m

resume = 1
tie = 0
win = 2

def boiler(level, stage):
    print(f"----------------------------------------------------------------------")
    print(f"--------------------------STAGE {stage-2} ---- LEVEL {level}------------------------")
    print(f"----------------------------------------------------------------------")

def valid_move(level, board, move, user):
    if move == "":
        return
    if move.isnumeric():
            move = int(move)
            if(move <= 0 or move > level.stage ** 2 or board.board[move - 1] != " "):
                print(f"Not a valid move(Not in list). Enter another move!")
                board.print_board()
                board.example_board()
                move = input(f"Move: ").strip()
                valid_move(level, board, move, user)
            else:
                board.place(move - 1 , user.current())
    else:
            print(f"Not a valid move(Not Num). Enter another move!")
            board.print_board()
            board.example_board()
            move = input(f"Move: ").strip()
            valid_move(level, board, move, user)

def start(board, level, tog, user, mini_max):
    while True:
        if user.current() == "X":
            place = input(f"Enter your move (1-{level.stage ** 2}): ").strip()
            valid_move(level, board, place, user)
            if mini_max.check_win(board.board) != resume:
                break
        else:
            best_move = mini_max.bestmove(board, h.helper.Player.X.name)
            if best_move is not None:
                if best_move == "tie":
                    return "tie"
                board.place(best_move, user.current())
                board.print_board()
                if mini_max.check_win(board.board) != resume:
                    break
        user.switch()

    result = mini_max.check_win(board.board)
    if result == win:
        board.print_board()
        print(f"Player {user.current()} wins!!!")
        return user.current()
    else:
        print(f"Tie!!!")
        return "tie"

def main(level, tog):
    # Initialize the game with level manager
    depth = level.level * 2
    user = h.helper.Player
    user.initialize()

    if tog:
        user.switch()
    
    board = b.board(level.stage)
    mini_max = m.mini_max(depth, level.stage)
    boiler(level.level, level.stage)

    if level.level == 1:
        board.example_board()

    return start(board, level, tog, user, mini_max)

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


