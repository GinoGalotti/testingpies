# Your Task
# You’re part of the team that explores Mars by sending remotely controlled vehicles to the surface of the planet. Develop an API that translates the commands sent from earth to instructions that are understood by the rover.

# Requirements
# You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
# The rover receives a character array of commands.
# Implement commands that move the rover forward/backward (f,b).
# Implement commands that turn the rover left/right (l,r).
# Implement wrapping from one edge of the grid to another. (planets are spheres after all)
# Implement obstacle detection before each move to a new square. If a given sequence of commands encounters an obstacle

# You are given a starting point (x,y), and a direction (N,S,E.W).
# The rover receives a collection of commands, implammant a command that will move the rover (f,b). And methods that will turn the rover

from enum import Enum


class Direction(Enum):
    N = 0
    E = 1
    S = 2
    W = 3


class Move(Enum):
    FORWARD = "f"
    BACK = "b"


class Turn(Enum):
    LEFT = "l"
    RIGHT = "r"

# Create exception when initing the wrong parameters of direction/position/landscape
# TODO: Create another class to accept a line of commands!
class Rover:

    def __init__(self, landscape, position=(0, 0), direction=Direction.N):
        self.position = position
        self.direction = direction
        self.landscape = landscape

    # To avoid having to check direcitons, we will have forward/backgrounds methods
    def move(self, direction):

        if (direction == Move.FORWARD):
            switcher = {
                Direction.N: (self.position[0]-1, self.position[1]),
                Direction.W: (self.position[0],   self.position[1]-1),
                Direction.S: (self.position[0]+1, self.position[1]),
                Direction.E: (self.position[0],   self.position[1]+1)
            }
        else:
            switcher = {
                Direction.N: (self.position[0]+1, self.position[1]),
                Direction.W: (self.position[0],   self.position[1]+1),
                Direction.S: (self.position[0]-1, self.position[1]),
                Direction.E: (self.position[0],   self.position[1]-1)
            }

        new_position = switcher.get(self.direction)

        if self.can_move(new_position):
            previous_position = self.position
            self.position = new_position

            if self.is_there_obstacle():
                self.position = previous_position
                return False
            else:
                return True

        return False

    def move_forward(self):
        return self.move(Move.FORWARD)

    def move_backwards(self):
        return self.move(Move.BACK)

    # As we don't have switch statements, and I don't want to use enums as integers, I'll do turn left and right
    def turn_left(self):
        switcher = {
            Direction.N: Direction.W,
            Direction.W: Direction.S,
            Direction.S: Direction.E,
            Direction.E: Direction.N
        }

        self.direction = switcher.get(self.direction)

    def turn_right(self):
        switcher = {
            Direction.N: Direction.E,
            Direction.E: Direction.S,
            Direction.S: Direction.W,
            Direction.W: Direction.N
        }

        self.direction = switcher.get(self.direction)

    # For testing purposes
    def can_move(self, position):
        if (position[0] < 0) or (position[1] < 0):
            return False

        if (position[0] >= len(self.landscape)):
            return False

        if (position[1] >= len(self.landscape[position[0]])):
            return False

        # If the obstacles can be "known" by the map
        return not(self.landscape[position[0]][position[1]])

    # On the problem, it seems that the obstacles can't be seen till the rover is already there
    def is_there_obstacle(self):
        not(self.landscape[self.position[0]][self.position[1]])

    def is_position(self, position):
        return position == self.position

    def is_direction(self, direction):
        return direction == self.direction

    def command(self, commands: str):
        actions = commands.split("-")
        
        for action in actions:
            if action == "F":
                self.move_forward()
            elif action == "B":
                self.move_backwards()
            elif action == "R":
                self.turn_right()
            elif action == "L":
                self.turn_left()
            else:
                print("Skipping invalid command")
