from assignment1.gridworld import Gridworld


def run():
    gridworld = Gridworld('gw/1.txt')
    print("Hello Gridworld!")
    print(gridworld.states)
    cost = gridworld.cost((0,1))
    print(cost)

if __name__ == '__main__':
    run()
