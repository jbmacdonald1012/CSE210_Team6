from constants import *
from game.scripting.action import Action


class MovePuckAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        puck = cast.get_first_actor(PUCK_GROUP)
        body = puck.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
