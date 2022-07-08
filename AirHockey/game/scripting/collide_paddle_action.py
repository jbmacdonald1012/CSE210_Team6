from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollidePaddleAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        puck = cast.get_first_actor(PUCK_GROUP)
        paddle = cast.get_first_actor(PADDLE_ONE_GROUP)
        
        puck_body = puck.get_body()
        paddle_body = paddle.get_body()

        if self._physics_service.has_collided(puck_body, paddle_body):
            puck.bounce_y()
            puck.bounce_x()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)    