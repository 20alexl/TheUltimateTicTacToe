#main.py
import game_manager as g
import level_manager as l
import helpers as h

def main(level):
    # Initialize the game with level manager
    game = g.game.game(level)
    return game.start()
    #game.board.print_board()

if __name__ == "__main__":
    level_manager = l.level.LevelManager()
    helper = h.helper.end_game()
    while True:
        winner = main(level_manager)

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
