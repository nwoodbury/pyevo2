import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class ImitationGame:
    """
    Runs a game on a given board using imitation dynamics.

    Parameters
    ----------
    board : Board
        The board to run the game on.
    payoffs : pandas.DataFrame
        The dataframe giving payoffs for two types of agents playing each
        other.
    savedir : str
        The directory, relative to <root>/out, where the figs and animation
        will be saved.
    """

    def __init__(self, board, payoffs, savedir):
        self.board = board
        self.payoffs = payoffs
        self.savedir = savedir

    def update(self):
        """
        Runs the dynamics for a single round, updating which position on the
        board belongs to which agent.
        """
        # Pass 1: compute average payoffs
        for x in range(30):
            for y in range(30):
                self._average_payoffs(x, y)

        # Pass 2: Determine which strategy will become next round
        for x in range(30):
            for y in range(30):
                self._best_neighbor(x, y)

        # Pass 3: Switch to new strategy
        for x in range(30):
            for y in range(30):
                self._update_strategy(x, y)

    def _average_payoffs(self, x, y):
        """
        Computes and stores (in the agent) the average payoff received by
        the agent at (x, y) by playing each of its neighbors.
        """
        agent = self.board.at(x, y)

        tot_payoff = 0
        count_neighbors = 0
        for d in self.board.dirs:
            ex, ey = self.board.get_coord_at_dir(x, y, d)
            if ex is None or ey is None:
                continue
            enemy = self.board.at(ex, ey)

            # enemy indexed first (selects column with enemy name), then
            # agent (selects row with agent name), as per the payoffs def.
            tot_payoff += self.payoffs[enemy.name][agent.name]
            count_neighbors += 1
        agent.curr_payoff = tot_payoff / float(count_neighbors)

    def _best_neighbor(self, x, y):
        """
        The agent at x, y looks at its own current payoff and the payoff of
        all neighbors to determine which strategy it will switch to.
        """
        agent = self.board.at(x, y)

        best_payoff = agent.curr_payoff
        best_strat = agent.name
        for d in self.board.dirs:
            ex, ey = self.board.get_coord_at_dir(x, y, d)
            if ex is None or ey is None:
                continue
            enemy = self.board.at(ex, ey)
            e_payoff = enemy.curr_payoff
            if e_payoff > best_payoff:
                # Only switch if strictly greater
                best_payoff = e_payoff
                best_strat = enemy.name
        agent.next_strat = self.board.init_agent(best_strat)

    def _update_strategy(self, x, y):
        agent = self.board.at(x, y)
        self.board.set_agent(x, y, agent.next_strat)

    def run(self, t, interval=1, fps=2):
        """
        Runs the game, animating the results.

        Parameters
        ----------
        t : int
            The number of timesteps for which the game will run.
        interval : int
            DEPRICATED.
            The milliseconds between frames. If the simulation needs to be
            run more quickly, lower this number. The saved animation's speed
            will not change. Defaults to 100.
        fps : int
            Changes the framerate of the saved animation. Does not change the
            speed of the simulation.
        """
        fig = plt.figure(figsize=(12, 12))
        M = self.board.draw()
        im = plt.imshow(M, interpolation='none', origin='lower',
                        extent=(0, 29, 0, 29))

        loc = 'out/%s' % self.savedir
        if not os.path.exists(loc):
            os.makedirs(loc)

        ax = fig.gca()

        time_text = ax.text(0.02, 0.95, 'Initialization',
                            transform=ax.transAxes)

        ticks = np.arange(0, 30)
        plt.xlim((0, 29))
        plt.ylim((0, 29))
        ax.set_xticks(ticks)
        ax.set_yticks(ticks)

        plt.savefig('%s/initial.png' % loc)

        def update_fig(i):
            self.update()
            M = self.board.draw()
            im.set_array(M)
            time_text.set_text('t = %i' % (i + 1))
            if i == t - 1:
                plt.savefig('%s/final.png' % loc)

            return im, ax

        ani = animation.FuncAnimation(fig, update_fig, frames=t, blit=True,
                                      interval=interval, repeat=False)
        writer = animation.FFMpegWriter()
        ani.save(filename='%s/animation.mp4' % loc, fps=fps, writer=writer)
	plt.close(fig)
