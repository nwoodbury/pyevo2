# !! Don't forget to switch to pyevo2
from pyevo2.population import Population
from pyevo2.agents import (TitForTatAgent, NotTitForTatAgent,
                           AlwaysCooperateAgent, AlwaysDefectAgent)
from pyevo2.payoffs import load_payoffs
from pyevo2.replication_game import ReplicationGame


if __name__ == '__main__':
    agents = {
        'Tit-for-Tat': {
            'class': TitForTatAgent,
            'color': 'b',
            'number': 225
        },
        'Not-Tit-For-Tat': {
            'class': NotTitForTatAgent,
            'color': 'm',
            'number': 225
        },
        'Always Cooperate': {
            'class': AlwaysCooperateAgent,
            'color': 'g',
            'number': 225
        },
        'Always Defect': {
            'class': AlwaysDefectAgent,
            'color': 'r',
            'number': 225
        }
    }
    pop = Population(agents)

    # !! changed
    payoffs = load_payoffs('bogus', 0.99)

    game = ReplicationGame(pop, payoffs, 'replication_bogus_01')
    game.run(20, fps=1)
