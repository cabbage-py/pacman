class Pacman:

    # Initialises Pacman object with 3 arguments:
    # x-coordinate, y-coordinate, direction-faced.
    def __init__(self, x, y, f):
        self.x = x
        self.y = y
        self.f = f

    # Updates face of Pacman with 1 argument:
    # -1 to turn left, 1 to turn right
    def update(self, turn):
        arr = ["NORTH", "EAST", "SOUTH", "WEST"]

        if (turn == -1 or turn == 1):
            index = arr.index(self.f)
            index = (index + turn) % 4
            self.f = arr[index]

    # Moves Pacman one space in the direction its facing
    # Ignores all invalid moves i.e. moving off the grid
    def move(self):
        if (self.f == "NORTH" and self.x != 4):
            self.y += 1

        elif (self.f == "SOUTH" and self.x != 0):
            self.y -= 1

        elif (self.f == "WEST" and self.y != 0):
            self.x -= 1

        elif (self.f == "EAST" and self.y != 4):
            self.x += 1
