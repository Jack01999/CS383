import heapq
from queue import PriorityQueue

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

        frontier = []
        heapq.heappush(frontier, (0, gridworld.initial_state))
        explored = []
        solution = []
        cost = 0
        nodes_expanded = 0

        while not len(frontier) == 0:
            node = heapq.heappop(frontier)
            print(node)
            if node == gridworld.goal_state:
                return solution
            explored.append(node)
            for n in gridworld.successors(node[1]):
                if (n not in frontier) and (n not in explored):
                    frontier.append(n)
                elif (n in frontier) and frontier.get(n) > gridworld.cost(n):
                    frontier.update(n, gridworld.cost(node))

        return




