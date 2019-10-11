from game import Game, State
from random_agent import RandomAgent
from minimax_agent import MinimaxAgent
import random


if __name__ == '__main__':
    g = Game(3)

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
    min_player = MinimaxAgent()
    max_player = RandomAgent()
    count = 0

    for i in range(0, 1000):
        final_utility, duration = g.play(min_player, max_player, verbose=False)
        if final_utility == -1:
            count = count + 1
    print(count)


    # Run a complete game between the two players
    # g.play(min_player, max_player, verbose=True)
