from game.casting.actor import Actor


class Score(Actor):
    """
    The way a player tracks their greed. 
    
    The responsibility of the score is to track a player's greed.

    Attributes:
        _score (string): The player's score which updates based on if they touch a gem or a rock.
    """
    def __init__(self):
        super().__init__()
        self._score = 0
        
    def get_score(self):
        """Gets the player's score.
        
        Returns:
            string: The score.
        """
        return self._score
    
    def set_score(self, score):
        """Updates the score to the given one.
        
        Args:
            score (string): The given score.
        """
        self._score = score