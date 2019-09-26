import heapq
from queue import PriorityQueue

from assignment1 import gridworld
from .agent import Agent


class UCS(Agent):

    def search(self, gridworld):
        # TODO
        '''
        frontier.add (INITIAL_STATE, 0) // priority queue
        explored = {}

        while !is_empty(frontier):
            node = get_next_node(frontier)
            if is_goal(n):
                return solution
            explored += {node}
            for n in expand(node):
                if (n not in frontier) and (n not in explored):
                    froniter += {n}
                else if (n in frontier) and frontier.get(n) > n.cost:
                    frontier.update(n, n.cost)
        return failure
        '''

        node = gridworld.initial_state
        frontier = []
        heapq.heappush(frontier, (0, node))
        explored = []
        solution = []
        cost = 0
        nodes_expanded = 0

        while not len(frontier) == 0:
            node = heapq.heappop(frontier)
            if node[1] == gridworld.goal_state:
                solution.append(node[1])
                return solution, cost, nodes_expanded
            explored.append(node[1])
            solution.append(node[1])
            nodes_expanded += 1
            cost += gridworld.cost(node[1])
            for n in gridworld.successors(node[1]):
                if (not self.is_in_frontier(frontier, n)) and (n not in explored):
                    heapq.heappush(frontier, (gridworld.cost(n), n))
                elif (self.is_in_frontier(frontier, n)) and self.get_cost(frontier, n) > gridworld.cost(n):
                    print(frontier)
                    self.update_cost(frontier, n, gridworld.cost(node))
                    print(frontier)

        return solution, cost, nodes_expanded

    def is_in_frontier(self, frontier, n):
        a = 0
        while not a == len(frontier):
            if frontier[a][1] == n:
                return True
            a += 1

        return False

    def get_cost(self, frontier, node):
        a = 0
        while not a == len(frontier):
            if frontier[a][1] == node:
                return frontier[a][0]
            a += 1

    def update_cost(self, frontier, node, newCost):
        a = 0
        while not a == len(frontier):
            if frontier[a][1] == node:
                frontier[a] = (newCost, node)
            a += 1

