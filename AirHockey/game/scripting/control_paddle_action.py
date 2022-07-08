from constants import *
from game.scripting.action import Action


class ControlPaddleAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        paddle = cast.get_first_actor(PADDLE_ONE_GROUP)
        if self._keyboard_service.is_key_down(A_KEY): 
            paddle.swing_left()
        elif self._keyboard_service.is_key_down(D_KEY): 
            paddle.swing_right()
        elif self._keyboard_service.is_key_down(W_KEY): 
            paddle.swing_up()
        elif self._keyboard_service.is_key_down(S_KEY): 
            paddle.swing_down()
        else: 
            paddle.stop_moving()        