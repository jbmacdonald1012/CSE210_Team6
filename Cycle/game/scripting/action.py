class Action:
    """ A thing that is done.

    Completes something integral to the game. One method is used and should be overridden by derived classes.
    """

    def execute(self, cast, script):
        """ Executes something integral to the game. 
        
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of actions in the game.
        """
        