import pandas as pd


def load_payoffs(game, gamma):
    """
    Loads the payoff matrix for the game `game` played with gamma = `gamma`.

    This payoff matrix should be saved in
    pyevo2/payoffs/<game>_<100 * gamma>.csv. This function should be called
    from a file located at the pyevo root.

    Parameters
    ----------
    game : str
        The name of the game to load. Likely 'prisoners_dilemma', 'stag_hunt',
        etc. or 'bogus' for testing.
    gamma : number
        The gamma at which the game is played. Likely 0.95 or 0.99
    """
    name = '%s_%i' % (game, int(gamma * 100))
    return pd.read_csv('payoffs/%s.csv' % name, index_col=0)
