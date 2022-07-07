from constants import *
from game.scripting.action import Action


class DrawPaddle2Action(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        paddle = cast.get_first_actor(PADDLE_TWO_GROUP)
        body = paddle.get_body()

        if paddle.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = paddle.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)