# !!! DIFFERENCE: pyevo -> pyevo2 !!!
from pyevo2.quad_board import QuadBoard
from pyevo2.agents import (TitForTatAgent, NotTitForTatAgent,
                           AlwaysCooperateAgent, AlwaysDefectAgent)
# !!! DIFFERENCE: import load_payoffs function instead of matrix !!!
from pyevo2.payoffs import load_payoffs


if __name__ == '__main__':
    # Define the agents to be in each quad
    quads = [
        {'name': 'Tit-for-Tat', 'class': TitForTatAgent,
         'color': 'b'},  # NW
        {'name': 'Not-Tit-for-Tat', 'class': NotTitForTatAgent,
         'color': 'm'},  # NE
        {'name': 'Always Cooperate', 'class': AlwaysCooperateAgent,
         'color': 'g'},  # SW
        {'name': 'Always Defect', 'class': AlwaysDefectAgent,
         'color': 'r'}   # SE
    ]

    # Initialize the board
    board = QuadBoard(quads)

    # !!! DIFFERENCE: payoff loading method is different
    payoffs = load_payoffs('bogus', 0.99)
