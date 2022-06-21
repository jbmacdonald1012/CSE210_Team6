from game.scripting.action import Action

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """
    def __init__(self,VideoService):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = VideoService

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score1 = cast.get_first_actor('Player 1')
        score2 = cast.get_first_actor('Player 2')
        cycle1 = cast.get_first_actor('cycle1')
        cycle2 = cast.get_first_actor('cycle2')
        segments = cast.get_segments()
        messages = cast.get_actors('messages')

        self._video_service.clear_buffer()
        self._video_service.draw_actor(cycle1)
        self._video_service.draw_actor(cycle2)
        self._video_service.draw_actors(segments)
        self._video_service.draw_actor(score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
