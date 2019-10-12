from collections import namedtuple

State = namedtuple('State', ['board', 'min_pos', 'max_pos', 'min_to_play'])

"""
Evaluation functions for use with Minimax search.
We have supplied you with one example function to get started.
An evaluation function should return an estimate of the utility of a state.
Thus, it should be high when max is winning and low when min is winning, and
it should be bounded by the terminal utilities +1 and -1.
Any evaluation function should return the utility when given a terminal state.
Keep these criteria in mind when writing your evaluation functions.
"""


def open_cells(game, state):
    """
    Estimates utility from the number of open cells next to the current player.
    More open cells is preferable to fewer.
    """
    if game.is_terminal(state):
        return game.utility(state)
    else:
        # the number of open cells next to the current player
        open_cells = {cell for (cell, _) in game.get_actions(state)}

        # there are at best 8 open cells, so score is near 1 when things are
        # "good" for the current player, and near 0 when things are "bad"
        score = len(open_cells) / 8
        return -score if state.min_to_play else score


def my_eval_1(game, state):
    """
    Write your own evaluation function here.
    Your functions must take two arguments, a game and a state.

    Hint: Think about why open_cells is not a very good evaluation function!
    How might you improve it?
    """

    if game.is_terminal(state):
        return game.utility(state)
    else:
        # the number of open cells next to the current player
        open_cells = {cell for (cell, _) in game.get_actions(state)}
        opponent_state = State(
            board=state.board,
            min_pos=state.min_pos,
            max_pos=state.max_pos,
            min_to_play=not state.min_to_play
        )
        # the number of open cells next to the opponent
        opponent_open_cells = {cell for (cell, _) in game.get_actions(opponent_state)}
        score = len(open_cells - opponent_open_cells) / 8
        return -score if state.min_to_play else score

def my_eval_2(game, state):
    """
    Write your second evaluation function here.
    """
    counter = 1
    o_counter = 1
    if game.is_terminal(state):
        return game.utility(state)
    else:
        opponent_state = State(
            board=state.board,
            min_pos=state.min_pos,
            max_pos=state.max_pos,
            min_to_play=not state.min_to_play
        )
        player_counter = 0
        opponent_counter = 0
        for actions in game.get_actions(state):
            counter += 1
            newState = game.apply_action(state, actions)
            open_cells = {cell for (cell, _) in game.get_actions(newState)}
            player_counter += len(open_cells)

        for actions in game.get_actions(opponent_state):
            o_counter += 1
            newState = game.apply_action(opponent_state, actions)
            opponent_open_cells = {cell for (cell, _) in game.get_actions(opponent_state)}
            opponent_counter += len(open_cells)

        score = (player_counter / counter) - (opponent_counter / o_counter)
        return -score if state.min_to_play else score




def my_best(game, state):
    """
    Call whichever one of your two functions you think is better
    and return the result here.
    """

    counter = 1
    o_counter = 1
    if game.is_terminal(state):
        return game.utility(state)
    else:
        opponent_state = State(
            board=state.board,
            min_pos=state.min_pos,
            max_pos=state.max_pos,
            min_to_play=not state.min_to_play
        )
        player_counter = 0
        opponent_counter = 0
        for actions in game.get_actions(state):
            counter += 1
            newState = game.apply_action(state, actions)
            open_cells = {cell for (cell, _) in game.get_actions(newState)}
            player_counter += len(open_cells)

        for actions in game.get_actions(opponent_state):
            o_counter += 1
            newState = game.apply_action(opponent_state, actions)
            opponent_open_cells = {cell for (cell, _) in game.get_actions(opponent_state)}
            opponent_counter += len(open_cells)

        score = (player_counter / counter) - (opponent_counter / o_counter)
        return -score if state.min_to_play else score
