import heapq

from .agent import Agent


class AStar(Agent):
    def checkHeuristic(self, start, end):
        x = abs(end[0] - start[0])
        y = abs(end[1] - start[1])
        heuristic = 1 * (x + y)
        return heuristic

    def is_in_frontier(self, frontier, n):
        a = 0
        while not a == len(frontier):
            if frontier[a][1] == n:
                return True
            a += 1

        return False

    def get_frontier_g(self, frontier, node):
        a = 0
        while not a == len(frontier):
            if frontier[a][1] == node:
                return frontier[a][0]
            a += 1

    def search(self, gridworld):
        # TODO
        frontier = []  # open list
        explored = []  # closed list
        heapq.heappush(frontier, (0, gridworld.initial_state))
        parent = {}
        solution = []
        cost = 0
        nodes_expanded = 0

        while not len(frontier) == 0:
            node = heapq.heappop(frontier)
            successors = gridworld.successors(node[1])
            node_g = 0
            node_g += gridworld.cost(node[1])
            nodes_expanded = len(explored)
            explored.append(node[1])
            if node == gridworld.goal_state:
                continue
            for n in successors:
                if n in explored:
                    continue
                n_g = node_g + self.checkHeuristic(n, node[1])
                n_h = self.checkHeuristic(gridworld.goal_state, n)
                n_f = n_g + n_h
                if self.is_in_frontier(frontier, n):
                    if n_g > self.get_frontier_g(frontier, n):
                        continue

                parent[n] = node[1]
                heapq.heappush(frontier, (n_f, n))

        currentState = parent.get(gridworld.goal_state)
        solution.insert(0, gridworld.goal_state)
        while not currentState == gridworld.initial_state:
            cost += gridworld.cost(currentState)
            solution.insert(0, currentState)
            currentState = parent.get(currentState)

        cost += gridworld.cost(gridworld.goal_state)
        solution.insert(0, gridworld.initial_state)

        return solution, cost, nodes_expanded
