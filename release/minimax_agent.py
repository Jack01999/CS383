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

    def max_value(self, depth, game, state):
        if (game.is_terminal(state) and self.depth_limit == inf):
            return (None, game.utility(state))
        elif game.is_terminal(state) or depth == self.depth_limit:
            return (None, self.eval_fn(game, state))
        Utility = float("-inf")
        action = None
        for a in game.get_actions(state):
            updatedUtility = max(Utility, self.min_value(depth + 1, game, game.apply_action(state, a))[1])
            if updatedUtility != Utility:
                Utility = updatedUtility
                action = a
        return (action, Utility)

    def min_value(self, depth, game, state):
        if (game.is_terminal(state) and self.depth_limit == inf):
            return (None, game.utility(state))
        elif game.is_terminal(state) or depth == self.depth_limit:
            return (None, self.eval_fn(game, state))
        Utility = float("inf")
        action = None
        for a in game.get_actions(state):
            updatedUtility = min(Utility, self.max_value(depth + 1, game, game.apply_action(state, a))[1])
            if updatedUtility != Utility:
                Utility = updatedUtility
                action = a
        return (action, Utility)

    def select_action(self, game, state):

        print(state)
        print(game.get_actions(state))

        print(state[2])

        return
        '''
        if (state.min_to_play):
            return self.min_value(0, game, state)[0]
        return self.max_value(0, game, state)[0]
        '''
        """
        TODO: Implement the minimax algorithm
        """

        '''
            State = (state, [board, min_pos, max_pos, min_to_play])
            board = current board
            min_pos = position of Min player
            max_pos = position of Max player
            min_to_play = Min player's turn
            max_to_play = Max player's turn
    
            Action = (move, [move, delete])

            set_init_state(self, state)
            __moveable_to(self, cell, state)
            get_actions(self, state)
            apply_action(self, state, action)
            utility(self, state)
            is_terminal(self, state)
            show(self, state)
            play(self, min, max, verbose=True)
            
        '''
