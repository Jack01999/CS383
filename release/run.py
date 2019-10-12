from game import Game, State
from random_agent import RandomAgent
from minimax_agent import MinimaxAgent
from eval_fns import open_cells
from eval_fns import my_eval_1
from eval_fns import my_eval_2
from eval_fns import my_best
import random


if __name__ == '__main__':
    g = Game(5)

    # Example of setting a custom start state for the game
    #g.set_init_state(State(
    #     board=[[1, 0, 1], [1, 1, 1], [1, 0, 1]],
    #     min_pos=(1, 0),
    #     max_pos=(1, 2),
    #     min_to_play=True
    #))

    # You can set the random seed to make your tests repeatable
    # random.seed(43110)

    # Create the agents to play in the game

    min_player = MinimaxAgent(my_eval_1, 3)
    max_player = MinimaxAgent(my_eval_2, 3)
    min_count = 0
    max_count = 0

    for i in range(0, 1):
        final_utility, duration = g.play(min_player, max_player, verbose=True)
        if final_utility == -1:
            print("Min Player won")
            min_count += 1
        else:
            print("Max player won")
            max_count += 1

    print(min_count)
    print(max_count)


    # Run a complete game between the two players
    # g.play(min_player, max_player, verbose=True)
