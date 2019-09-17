class Gridworld:
    states = None
    initial_state = None
    goal_state = None

    def __init__(self, filename):
        with open(filename) as file:
            self.states = [list(line) for line in file.read().splitlines()]
            for y, line in enumerate(self.states):
                for x, value in enumerate(line):
                    if value.isnumeric():
                        line[x] = int(value)
                    if value == 's':
                        self.initial_state = (x, y)
                    if value == 'g':
                        self.goal_state = (x, y)

    def isWall(self, x, y):
        if self.states[x][y] == '#':
            return True
        else:
            return False

    def successors(self, state):
        # TODO
        successor_list = []
        size = len(self.states) - 1

        #
        #   CORNER CASES
        #
        if state[0] == 0 and state[1] == 0:  # if the current state is in the upper left corner
            if self.isWall(state[0], state[1] + 1) is False:  # No wall to the right
                successor_list.append((state[0], state[1] + 1))
            if self.isWall(state[0] + 1, state[1]) is False:  # No wall below
                successor_list.append((state[0] + 1, state[1]))
        elif state[0] == 0 and state[1] == size:  # if the current state is in the upper right corner
            if self.isWall(state[0], state[1] - 1) is False:  # No wall to the left
                successor_list.append((state[0], state[1] - 1))
            if self.isWall(state[0] + 1, state[1]) is False:  # No wall below
                successor_list.append((state[0] + 1, state[1]))
        elif state[0] == size and state[1] == 0:  # if the current state is in the bottom left corner
            if self.isWall(state[0] - 1, state[1]) is False:  # No wall above
                successor_list.append((state[0] - 1, state[1]))
            if self.isWall(state[0], state[1] + 1) is False:  # No wall to the right
                successor_list.append((state[0], state[1] + 1))
        elif state[0] == size and state[1] == size:  # if the current state is in the bottom right corner
            if self.isWall(state[0] - 1, state[1]) is False:  # No wall above
                successor_list.append((state[0] - 1, state[1]))
            if self.isWall(state[0], state[1] - 1) is False:  # No wall to the left
                successor_list.append((state[0], state[1] - 1))
        #
        #    SIDE CASES
        #
        elif state[0] == 0:  # if the current state is on the top row
            if self.isWall(state[0], state[1] - 1) is False:  # No wall to the left
                successor_list.append((state[0], state[1] - 1))
            if self.isWall(state[0], state[1] + 1) is False:  # No wall to the right
                successor_list.append((state[0], state[1] + 1))
            if self.isWall(state[0] + 1, state[1]) is False:  # No wall below
                successor_list.append((state[0] + 1, state[1]))
        elif state[0] == size:  # if the current state is on the bottom row
            if self.isWall(state[0], state[1] - 1) is False:  # No wall to the left
                successor_list.append((state[0], state[1] - 1))
            if self.isWall(state[0], state[1] + 1) is False:  # No wall to the right
                successor_list.append((state[0], state[1] + 1))
            if self.isWall(state[0] - 1, state[1]) is False:  # No wall above
                successor_list.append((state[0] - 1, state[1]))
        elif state[1] == 0:  # if the current state is on the left column
            if self.isWall(state[0] - 1, state[1]) is False:  # No wall above
                successor_list.append((state[0] - 1, state[1]))
            if self.isWall(state[0] + 1, state[1]) is False:  # No wall below
                successor_list.append((state[0] + 1, state[1]))
            if self.isWall(state[0], state[1] + 1) is False:  # No wall to the right
                successor_list.append((state[0], state[1] + 1))
        elif state[1] == size:  # if the current state is on the right column
            if self.isWall(state[0] - 1, state[1]) is False:  # No wall above
                successor_list.append((state[0] - 1, state[1]))
            if self.isWall(state[0] + 1, state[1]) is False:  # No wall below
                successor_list.append((state[0] + 1, state[1]))
            if self.isWall(state[0], state[1] - 1) is False:  # No wall to the left
                successor_list.append((state[0], state[1] - 1))
        #
        #   EVERYTHING ELSE (MIDDLE PIECES)
        #
        else:
            if self.isWall(state[0] - 1, state[1]) is False:  # No wall above
                successor_list.append((state[0] - 1, state[1]))
            if self.isWall(state[0] + 1, state[1]) is False:  # No wall below
                successor_list.append((state[0] + 1, state[1]))
            if self.isWall(state[0], state[1] - 1) is False:  # No wall to the left
                successor_list.append((state[0], state[1] - 1))
            if self.isWall(state[0], state[1] + 1) is False:  # No wall to the right
                successor_list.append((state[0], state[1] + 1))

        return successor_list

    def cost(self, state):
        # TODO
        if self.states[state[0]][state[1]] == 's' or self.states[state[0]][state[1]] == 'g':
            return 1
        if self.states[state[0]][state[1]] == '#':
            return 0

        return self.states[state[0]][state[1]]
