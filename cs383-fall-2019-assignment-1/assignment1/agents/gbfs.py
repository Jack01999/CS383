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

        while not node == gridworld.goal_state:
            node = heapq.heappop(frontier)
            explored.append(node[1])
            successors = gridworld.successors(node[1])


            for n in successors:
                print(n)
                heuristic = self.checkHeuristic(gridworld, n)
                if (not self.is_in_frontier(frontier, n)) and (n not in explored):


