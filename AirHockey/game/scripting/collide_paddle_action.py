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
        paddle_2 = cast.get_first_actor(PADDLE_TWO_GROUP)
        
        puck_body = puck.get_body()
        paddle_body = paddle.get_body()
        paddle_body_2 = paddle_2.get_body()
        
        paddle_velocity = paddle_body.get_velocity()
        paddle_velocity_x = paddle_velocity.get_x()
        paddle_velocity_y = paddle_velocity.get_y()

        paddle_velocity_2 = paddle_body_2.get_velocity()
        paddle_velocity_2_x = paddle_velocity_2.get_x()
        paddle_velocity_2_y = paddle_velocity_2.get_y()

        if self._physics_service.has_collided(puck_body, paddle_body):
            puck.bounce_y(paddle_velocity_y)
            puck.bounce_x(paddle_velocity_x)
            paddle.stop_moving_collision()
            sound = Sound(SLIDE_HIT)
            self._audio_service.play_sound(sound)  

        if self._physics_service.has_collided(puck_body, paddle_body_2):
            puck.bounce_y(paddle_velocity_2_y)
            puck.bounce_x(paddle_velocity_2_x)
            paddle_2.stop_moving_collision()
            sound = Sound(SLIDE_HIT)
            self._audio_service.play_sound(sound)  