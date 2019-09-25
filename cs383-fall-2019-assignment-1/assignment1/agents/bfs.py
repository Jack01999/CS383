import queue

from .agent import Agent


class BFS(Agent):
    def search(self, gridworld):
        # TODO

        node = gridworld.initial_state
        frontier = queue.Queue()
        frontier.put(node)
        explored = []
        solution = []
        cost = 0
        nodes_expanded = 0
        parent = {}

        while not node == gridworld.goal_state:
            node = frontier.get()
            explored.append(node)
            for n in gridworld.successors(node):
                if (n not in frontier.queue) and (n not in explored):
                    parent[n] = node
                    if n == gridworld.goal_state:
                        nodes_expanded = len(explored)
                        node = gridworld.goal_state
                    else:
                        frontier.put(n)

        currentState = parent.get(gridworld.goal_state)
        solution.insert(0, gridworld.goal_state)
        while not currentState == gridworld.initial_state:
            cost += gridworld.cost(currentState)
            solution.insert(0, currentState)
            currentState = parent.get(currentState)

        cost += gridworld.cost(gridworld.goal_state)
        solution.insert(0, gridworld.initial_state)

        return solution, cost, nodes_expanded
