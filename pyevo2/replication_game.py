import os
import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


class ReplicationGame:
    """
    Defines a game running replication dynamics.

    Parameters
    ----------
    population : Population
        Defines the population of agents.
    payoffs : pandas.DataFrame
        Defines the payoffs for agents playing against each other.
    savedir : str
        The location, relative to <root>/out/, where the sim results will be
        saved.
    """

    def __init__(self, population, payoffs, savedir):
        self.population = population
        self.payoffs = payoffs
        self.savedir = savedir

    def update(self):
        """
        Updates a single round of the game.
        """
        # Collect agents into a single list, resetting old population
        agent_lst = []
        for name, lst in self.population.agents.iteritems():
            agent_lst += lst
            self.population.agents[name] = []

        # Compete agent, adding it back into the population with its new strat
        for agent in agent_lst:
            self.compete_agent(agent, agent_lst)

    def compete_agent(self, agent, agent_lst):
        """
        Competes an agent with another random agent from the population. This
        agent then replicates the strategy of the winner of the two.
        """
        enemy_i = random.randint(0, len(agent_lst) - 1)
        enemy = agent_lst[enemy_i]

        # enemy indexed first (selects column with enemy name), then
        # agent (selects row with agent name), as per the payoffs def.
        agent_payoff = self.payoffs[enemy.name][agent.name]
        enemy_payoff = self.payoffs[agent.name][enemy.name]

        if agent_payoff >= enemy_payoff:
            best_agent = agent.name
        else:
            best_agent = enemy.name

        new_agent = self.population.init_agent(best_agent)
        self.population.agents[best_agent].append(new_agent)

    def run(self, t, interval=1, fps=2):
        """
        Runs the game, creating animations. Overrides the base function in
        `Game`.
        """
        fig = plt.figure(figsize=(12, 12))
        ax = plt.gca()

        loc = 'out/%s' % self.savedir
        if not os.path.exists(loc):
            os.makedirs(loc)

        xs = np.arange(len(self.population.agents))
        plt.ylim((0, 900))
        width = 0.5
        labels = [name for name in self.population.agents.keys()]
        colors = [self.population.agent_defs[name]['color'] for name
                  in labels]

        ys = [len(self.population.agents[name]) for name in labels]
        bar = ax.bar(xs + width, ys, width, color=colors)
        ax.set_xticks(xs + 3 / 2.0 * width)
        ax.set_xticklabels(labels)
        plt.ylabel('Number of Agents')

        time_text = ax.text(0.02, 0.95, 'Initialization',
                            transform=ax.transAxes)

        plt.savefig('%s/initial.png' % loc)

        def update_fig(i):
            self.update()
            ys = [len(self.population.agents[name]) for name in labels]
            for rect, h in zip(bar, ys):
                rect.set_height(h)
            time_text.set_text('t = %i' % (i + 1))
            if i == t - 1:
                plt.savefig('%s/final.png' % loc)

            return ax,

        ani = animation.FuncAnimation(fig, update_fig, frames=t, blit=True,
                                      interval=interval, repeat=False)
        writer = animation.FFMpegWriter()
        ani.save(filename='%s/animation.mp4' % loc, fps=fps, writer=writer)
	plt.close(fig)
