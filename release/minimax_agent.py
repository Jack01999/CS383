from math import inf
from agent import Agent


class MinimaxAgent(Agent):
    depth_limit = None
    eval_fn = None
    prune = None

    def __init__(self, eval_fn=None, depth_limit=inf, prune=False):
        self.depth_limit = depth_limit
        self.eval_fn = eval_fn
        self.prune = prune

    def select_action(self, game, state):
        """
        TODO: Implement the minimax algorithm
        """
        pass
