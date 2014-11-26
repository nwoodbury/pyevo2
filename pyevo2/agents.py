"""
These really don't do much anymore, but exist for closer compatibility of the
old pyevo.
"""
from matplotlib.colors import ColorConverter


class Agent:
    """
    Base class defining an agent.

    Parameters
    ----------
    color : matplotlib color; e.g. str in {'r', 'g', 'y', etc.}
        The color to draw this agent.
    name : str
        The name of this agent.
    """

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def draw(self):
        """
        Returns an (r, g, b) tuplet for matplotlib to draw this agent.
        """
        colors = ColorConverter().colors
        return colors[self.color]


class AlwaysCooperateAgent(Agent):
    pass


class AlwaysDefectAgent(Agent):
    pass


class TitForTatAgent(Agent):
    pass


class NotTitForTatAgent(Agent):
    pass
