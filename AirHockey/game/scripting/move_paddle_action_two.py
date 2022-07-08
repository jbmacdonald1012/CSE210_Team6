from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MovePaddleActionTwo(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        paddle = cast.get_first_actor(PADDLE_TWO_GROUP)
        body = paddle.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        
        position = position.add(velocity)


        if x < 0:
            position = Point(0, position.get_y())
        elif x > (SCREEN_WIDTH - PADDLE_WIDTH):
            position = Point(SCREEN_WIDTH - PADDLE_WIDTH, position.get_y())
        elif y < 0:
            position = Point(position.get_x(), 0)
        elif y > (SCREEN_HEIGHT - PADDLE_HEIGHT):
            position = Point(position.get_x(), SCREEN_HEIGHT - PADDLE_HEIGHT)
            
        body.set_position(position)