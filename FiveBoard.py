
# Author: Nathaniel Nguyen
# Date: 05/31/2020
# Description: Creates a 15x15 board to play tic-tac-toe and returns the current state of the game.

class FiveBoard:
    """Represents a board for a two-player game of tic-tac-toe."""

    def __init__(self):
        """Initializes board to a list of 15 lists and sets current state to UNFINISHED."""

        self._lol = [['' for num in range(0, 15, 1)] for num in range(0, 15, 1)]

        self._currentstate = ('UNFINISHED')

    def make_move(self,move_row, move_column, x_or_o):
        """Takes as an input, the desired row, columnn, and player to make a move."""

        if x_or_o == 'x' and self._lol[move_row][move_column] == '':
            self._lol[move_row][move_column] = 'x'
            return True

        elif x_or_o == 'o' and self._lol[move_row][move_column] == '':
            self._lol[move_row][move_column] = 'o'
            return True

        else:
            return False

    def get_current_state(self):
        """Determines the current state of the game."""

        transpose = [['' for num in range(0, 15, 1)] for num in range(0, 15, 1)]
        flip = [['' for num in range(0, 15, 1)] for num in range(0, 15, 1)]

        draw_count = 0
        allow = ['x', 'o']

        """Transposes and flips the board, and determines if there is a draw."""
        for row in range(0, 15, 1):
            for col in range(0, 15, 1):
                transpose[col][row] = self._lol[row][col]
                flip[row][col] = self._lol[row][14 - col]

                if self._lol[row][col] in allow:
                    draw_count += 1

                    if draw_count == 225:
                        self._currentstate = ('DRAW')

        """Determines if there are five x's or o's in a row horizontally and vertically."""
        for row in range(0, 15, 1):
            for col in range(0, 12, 1):

                x_win_h = ['x', 'x', 'x', 'x', 'x']
                o_win_h = ['o', 'o', 'o', 'o', 'o']

                if x_win_h == self._lol[row][col:col + 5]:
                    self._currentstate = ('X_WON')
                elif o_win_h == self._lol[row][col:col + 5]:
                    self._currentstate = ('O_WON')
                elif x_win_h == transpose[row][col:col + 5]:
                    self._currentstate = ('X_WON')
                elif o_win_h == transpose[row][col:col + 5]:
                    self._currentstate = ('O_WON')

        """Determines if there are five x's or o's in a row diagonally."""
        for row in range(0, 11, 1):
            for col in range(0, 11, 1):
                if self._lol[row][col] == 'x' and self._lol[row + 1][col + 1] == 'x' and self._lol[row + 2][col + 2] == 'x' \
                and self._lol[row + 3][col + 3] == 'x' and self._lol[row + 4][col + 4] == 'x':
                    self._currentstate = ('X_WON')
                elif self._lol[row][col] == 'o' and self._lol[row + 1][col + 1] == 'o' and self._lol[row + 2][col + 2] == 'o' \
                        and self._lol[row + 3][col + 3] == 'o' and self._lol[row + 4][col + 4] == 'o':
                    self._currentstate = ('O_WON')
                elif flip[row][col] == 'x' and flip[row + 1][col + 1] == 'x' and flip[row + 2][col + 2] == 'x' \
                        and flip[row + 3][col + 3] == 'x' and flip[row + 4][col + 4] == 'x':
                    self._currentstate = ('X_WON')
                elif flip[row][col] == 'o' and flip[row + 1][col + 1] == 'o' and flip[row + 2][col + 2] == 'o' \
                        and flip[row + 3][col + 3] == 'o' and flip[row + 4][col + 4] == 'o':
                    self._currentstate = ('O_WON')

        return self._currentstate