from constants import *
from game.casting.actor import Actor

class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._score_1 = 0
        self._score_2 = 0
    def add_points_1(self, points):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._score_1 += 1

    def add_points_2(self, points):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._score_2 += 1

    def get_score_1(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._score_1
        
    def get_score_2(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._score_2
   
    def reset(self):
        """Resets the stats back to their default values."""
        self._score = 0