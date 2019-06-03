# Game of Life
from collections import namedtuple

#Not using Numpy
class GameLife():

    Cords = namedtuple("Cords", "x, y")

    def __init__(self, board=None):
        if not board:
            print("penis")
            board = [   [ 1, 1, 0, 0, 1],
                        [ 1, 1, 0, 1, 0],
                        [ 1, 1, 0, 0, 1],
                        [ 1, 0, 1, 1, 0], 
                        [ 1, 1, 0, 1, 1],
                        [ 1, 1, 0, 1, 1]]
        self.board = board
        self.x_length = len(board)
        self.y_length = len(board[0])

        print(str(board))
        print("Len are {0} and {1}".format(self.x_length, self.y_length))

    def round(self):

        for x in range(0, self.x_length):
            for y in range(0, self.y_length):
                self.board[x][y] = self.dead_or_alive(self.Cords(x,y), self.board[x][y])
                print("testing position {0} with board {1}".format(str(self.Cords(x,y)),str(self.board)))

        return True
    
    def alive_neighbours(self, position):
        x = position.x
        y = position.y

        not_first_row = x > 0
        not_first_column = y > 0
        not_last_row = x < (self.x_length - 1)
        not_last_column = y < (self.y_length - 1)

        neightbours = 0

        if not_first_column:
            neightbours += self.board[x][y-1]
        if not_first_row:
            neightbours += self.board[x-1][y]
        if not_first_column and not_first_row:
            neightbours += self.board[x-1][y-1]
        if not_last_column:
            neightbours += self.board[x][y+1]
        if not_last_row:
            neightbours += self.board[x+1][y]
        if not_last_column and not_last_row:
            neightbours += self.board[x+1][y+1]
        if not_first_column and not_last_row:
            neightbours += self.board[x+1][y-1]
        if not_first_row and not_last_column:
            neightbours += self.board[x-1][y+1]

        return neightbours

    def dead_or_alive(self, position, is_alive):

        switcher = {
            1: 0,
            2: 1,
            3: 1,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
        }

        if is_alive:
            return switcher.get(self.alive_neighbours(position))
        else:
            if (self.alive_neighbours(position) == 3):
                return 1
            else: 
                return 0
