import heapq

from .agent import Agent


class AStar(Agent):
    def checkHeuristic(self, end, node):
        x = abs(end[0] - node[0])
        y = abs(end[1] - node[1])
        heuristic = 1 * (x + y)
        return heuristic

    def is_in_frontier(self, frontier, n):
        a = 0
        while not a == len(frontier):
            if frontier[a][1] == n:
                return True
            a += 1

        return False

    def search(self, gridworld):
        # TODO
        explored = []
        frontier = []  # initialize heap queue
        node = gridworld.initial_state
        heapq.heappush(frontier, (self.checkHeuristic(gridworld.goal_state, node), node))
        parent = {}
        solution = []
        cost = 0
        nodes_expanded = 0

        while not len(frontier) == 0:
            node = heapq.heappop(frontier)  # node with the lowest heuristic
            explored.append(node[1])
            if node == gridworld.goal_state:
                break
            successors = gridworld.successors(node[1])
            for n in successors:
                if n in explored:
                    continue
                print(explored)
                g = self.checkHeuristic(n, gridworld.initial_state) + self.checkHeuristic(n, node[1])
                h = self.checkHeuristic(gridworld.goal_state, n)
                f = g + h

                if self.is_in_frontier(frontier, n):
                    if g > self.checkHeuristic(node[1], gridworld.initial_state):
                        continue

                heapq.heappush(frontier, (self.checkHeuristic(gridworld.goal_state, n), n))

        return solution, cost, nodes_expanded
