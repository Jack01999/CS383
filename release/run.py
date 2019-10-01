from game import Game, State
from random_agent import RandomAgent
import random


if __name__ == '__main__':
    g = Game(3)

    # Example of setting a custom start state for the game
    # g.set_init_state(State(
    #     board=[[0, 0, 1], [1, 1, 1], [1, 0, 1]],
    #     min_pos=(1, 0),
    #     max_pos=(1, 1),
    #     min_to_play=True
    # ))

    # You can set the random seed to make your tests repeatable
    # random.seed(43110)
    print("its working")
    # Create the agents to play in the game
    min_player = RandomAgent()
    max_player = RandomAgent()

    # Run a complete game between the two players
    g.play(min_player, max_player, verbose=True)