import heapq

from .agent import Agent


class GBFS(Agent):
    def checkHeuristic(self, gridworld, node):
        goal = gridworld.goal_state
        x = abs(goal[0] - node[0])
        y = abs(goal[1] - node[1])
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
        node = gridworld.initial_state  # initial state
        heapq.heappush(frontier, (self.checkHeuristic(gridworld, node), node))  # add the initial state into the queue.[ (heuristic, state) ]
        foundPath = False
        parent = {}
        solution = []
        cost = 0
        nodes_expanded = 0

        while not node == gridworld.goal_state:
            node = heapq.heappop(frontier)
            explored.append(node[1])
            successors = gridworld.successors(node[1])

            for n in successors:
                heuristic = self.checkHeuristic(gridworld, n)
                if (not self.is_in_frontier(frontier, n)) and (n not in explored):
                    parent[n] = node[1]
                    if n == gridworld.goal_state:
                        nodes_expanded = len(explored)
                        node = gridworld.goal_state
                    else:
                        heapq.heappush(frontier, (self.checkHeuristic(gridworld, n), n))

        currentState = parent.get(gridworld.goal_state)
        solution.insert(0, gridworld.goal_state)
        while not currentState == gridworld.initial_state:
            cost += gridworld.cost(currentState)
            solution.insert(0, currentState)
            currentState = parent.get(currentState)

        cost += gridworld.cost(gridworld.goal_state)
        solution.insert(0, gridworld.initial_state)

        return solution, cost, nodes_expanded



