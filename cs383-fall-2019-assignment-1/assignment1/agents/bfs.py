import queue

from .agent import Agent


class BFS(Agent):
    def search(self, gridworld):
        # TODO

        frontier = queue.Queue()
        frontier.put(gridworld.initial_state)
        explored = []

        while not frontier.empty():
            node = frontier.get()
            explored += node
            for n in node:
                if (n in frontier is False) and (n in explored is False):
                    if n == gridworld.goal_state:
                        return explored
                    else:
                        frontier += n

        print(frontier.get())

        return False
