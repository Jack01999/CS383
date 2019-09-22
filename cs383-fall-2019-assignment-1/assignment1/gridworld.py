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
        sizeRows = len(self.states) - 1
        sizeColumns = len(self.states[0]) - 1

        if state[1] == 0:  # if the state is on the top row
            if self.isWall(state[1] + 1, state[0]) is False:  # if there is no wall below
                successor_list.append((state[0], state[1] + 1))
            if state[0] == 0:  # if the state is on the upper left corner
                if self.isWall(state[1], state[0] + 1) is False:  # if there is no wall to the right
                    successor_list.append((state[0] + 1, state[1]))
            elif state[0] == sizeColumns:  # if the state is on the upper right corner
                if self.isWall(state[1], state[0] - 1) is False:  # if there is no wall to the left
                    successor_list.append((state[0] - 1, state[1]))
            else:
                if self.isWall(state[1], state[0] + 1) is False:  # if there is no wall to the right
                    successor_list.append((state[0] + 1, state[1]))
                if self.isWall(state[1], state[0] - 1) is False:  # if there is no wall to the left
                    successor_list.append((state[0] - 1, state[1]))
        elif state[1] == sizeRows:  # if the state is on the bottom row
            if self.isWall(state[1] - 1, state[0]) is False:  # if there is no wall above
                successor_list.append((state[0], state[1] - 1))
            if state[0] == 0:  # if the state is on the lower left corner
                if self.isWall(state[1], state[0] + 1) is False:  # if there is no wall to the right
                    successor_list.append((state[0] + 1, state[1]))
            elif state[0] == sizeColumns:  # if the state is on the bottom right corner
                if self.isWall(state[1], state[0] - 1) is False:  # if there is no wall to the left
                    successor_list.append((state[0] - 1, state[1]))
            else:
                if self.isWall(state[1], state[0] + 1) is False:  # if there is no wall to the right
                    successor_list.append((state[0] + 1, state[1]))
                if self.isWall(state[1], state[0] - 1) is False:  # if there is no wall to the left
                    successor_list.append((state[0] - 1, state[1]))
        elif state[0] == 0:  # if the state is on the left column
            if self.isWall(state[1] + 1, state[0]) is False:  # if there is no wall below
                successor_list.append((state[0], state[1] + 1))
            if self.isWall(state[1] - 1, state[0]) is False:  # if there is no wall above
                successor_list.append((state[0], state[1] - 1))
            if self.isWall(state[1], state[0] + 1) is False:  # if there is no wall to the right
                successor_list.append((state[0] + 1, state[1]))
        elif state[0] == sizeColumns:  # if the state is on the right column
            if self.isWall(state[1] + 1, state[0]) is False:  # if there is no wall below
                successor_list.append((state[0], state[1] + 1))
            if self.isWall(state[1] - 1, state[0]) is False:  # if there is no wall above
                successor_list.append((state[0], state[1] - 1))
            if self.isWall(state[1], state[0] - 1) is False:  # if there is no wall to the left
                successor_list.append((state[0] - 1, state[1]))
        else:
            if self.isWall(state[1] + 1, state[0]) is False:  # if there is no wall below
                successor_list.append((state[0], state[1] + 1))
            if self.isWall(state[1] - 1, state[0]) is False:  # if there is no wall above
                successor_list.append((state[0], state[1] - 1))
            if self.isWall(state[1], state[0] - 1) is False:  # if there is no wall to the left
                successor_list.append((state[0] - 1, state[1]))
            if self.isWall(state[1], state[0] + 1) is False:  # if there is no wall to the right
                successor_list.append((state[0] + 1, state[1]))

        return successor_list

    def cost(self, state):
        # TODO
        if self.states[state[1]][state[0]] == 's' or self.states[state[1]][state[0]] == 'g':
            return 1
        if self.states[state[1]][state[0]] == '#':
            return 0

        return self.states[state[1]][state[0]]
