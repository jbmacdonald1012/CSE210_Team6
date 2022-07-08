from constants import *
from game.scripting.action import Action


class ControlPaddleActionTwo(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        paddle = cast.get_first_actor(PADDLE_TWO_GROUP)
        if self._keyboard_service.is_key_down(J_KEY): 
            paddle.swing_left()
        elif self._keyboard_service.is_key_down(L_KEY): 
            paddle.swing_right()
        elif self._keyboard_service.is_key_down(I_KEY): 
            paddle.swing_up()
        elif self._keyboard_service.is_key_down(K_KEY): 
            paddle.swing_down()
        else: 
            paddle.stop_moving()   