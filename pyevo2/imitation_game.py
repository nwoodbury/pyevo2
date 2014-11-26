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
        pass

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
