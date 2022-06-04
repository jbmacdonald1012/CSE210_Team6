from game.casting.actor import Actor


class Score(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a score about itself.

    Attributes:
        _score (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._score = ""
        
    def get_score(self):
        """Gets the artifact's score.
        
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