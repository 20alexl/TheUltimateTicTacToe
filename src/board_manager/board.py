#board_manager/board.py
class board:
    def __init__(self, size):
        self._size = size
        self.board = [" "] * size**2

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Ensure the value is within the allowed range
        if  value >= 3:
            self._size = value
        else:
            raise ValueError(f"Size cant be smaller than 3.")

    def print_board(self):
        temp = 0
        for row in range((self._size*2) + 1):
            for col in range((self._size*4) + 1):
                #print(row, col)
                if row % 2 == 0:
                    if col % 4 == 0:
                        print('+ ', end='')
                    else:
                        print('- ', end='')
                else:
                    if (col - 2) % 4 == 0:
                        print(f'{self.board[temp]} ', end='')
                        temp += 1
                    else:
                        if (col - 1) % 2 == 0:
                            print('  ', end='')
                        else:
                            print('| ', end='')
            print()

    def example_board(self, rows):
        print(f"Player 1 is X, Computer is O")
        print(f"Enter the number of the place you want to go")
        print(f"EXAMPLE {rows}X{rows} BOARD")
        temp = 1
        trig = False
        for row in range((self._size*2) + 1):
            for col in range((self._size*4) + 1):
                #print(row, col)
                if trig:
                    print('  ', end='')
                    trig = False
                elif row % 2 == 0:
                    if col % 4 == 0:
                        print('+ ', end='')
                    else:
                        print('- ', end='')
                else:
                    if (col - 2) % 4 == 0:
                        print(f'{temp} ', end='')
                        temp += 1
                    else:
                        if (col - 1) % 2 == 0:
                            if temp > 10:
                                print(' ', end='')
                            else:
                                print('  ', end='')
                        else:
                            print('| ', end='')
                            trig = True
            print()

    def place(self, loc, user):
        if self.board[loc] == ' ':
            self.board[loc] = user
        else:
            raise ValueError(f"Invalid place loaction")